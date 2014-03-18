#!/usr/bin/env python

import socket
import thread
from Tkinter import Tk, Frame, BOTH, Canvas
import tkMessageBox

class Grid(Frame):
    def __init__(self, parent):
      self.sock = socket.socket()
      self.host = ''
      self.buf = 1024
      self.port = 8888
      self.sock.connect((self.host, self.port))

      self.purple = '#130d38'
      self.green = '#239d60'

      self.sock.send('Let me come play!')
      self.message = self.sock.recv(self.buf)
      if self.message:
          print 'Client got:', self.message
          self.icon = self.message

      Frame.__init__(self, parent, background='white')
      self.parent = parent

      self.dimension = 100
      self.cells = {}
      self.used = list()
      for i in range(9):
          self.used.append('n')

      self.lock = thread.allocate_lock()
      self.lastTimestamp = 0

      if self.icon == 'X':
        self.turn = True
      else:
        self.turn = False

      self.initUI()

    def initUI(self):
      self.parent.title('Tic-Tac-Toe')
      self.pack(fill=BOTH, expand=1)

      self.canvas = Canvas(self)
      for row in range(3):
        for column in range(3):
          x1 = column*self.dimension
          y1 = row*self.dimension
          x2 = x1 + self.dimension
          y2 = y1 + self.dimension
          self.cells[row, column] = self.canvas.create_rectangle(x1, y1, x2, y2, outline=self.purple)
          self.clickId = self.canvas.bind('<ButtonRelease-1>', self.cellClick)

      self.canvas.pack(fill=BOTH, expand=1)

      if self.icon == 'O':
        self.recvMove()

    def cellClick(self, event):
      print 'click'
      row = event.y/self.dimension
      column = event.x/self.dimension
      print ('%d %d' %(row, column))
      self.sendMove(3*row + column)

    def sendMove(self, index):
      print 'sending'
      self.sock.send('%d %s' %(index, self.icon))
      info = self.sock.recv(self.buf).split()
      print 'Client received:', info
      if float(info[3]) - self.lastTimestamp > 2:
        index = int(info[0])
        #self.canvas.unbind('<ButtonRelease-1>', self.clickId)
        self.update(index/3, index%3, info[1], info[3])
        self.recvMove()
      else:
        print 'not using received'

    def recvMove(self):
      print 'listening'
      info = self.sock.recv(self.buf).split()
      print 'Client received:', info
      index = int(info[0])
      self.update(index/3, index%3, info[1], info[3])
      #self.clickId = self.canvas.bind('<ButtonRelease-1>', self.cellClick)

    def update(self, row, column, icon, timestamp):
      x = column*self.dimension + self.dimension/2
      y = row*self.dimension + self.dimension/2

      if self.used[3*row + column] == 'n':
        self.canvas.create_text(x, y, text=icon, fill=self.purple, font='Verdana 18 bold italic')
        self.cellsUsed += 1
        self.used[3*row + column] = icon
        self.checkWin(3*row + column)

      self.lastTimestamp = timestamp
      self.canvas.update_idletasks()
      print 'Used:', self.used
      print 'time: %s' %self.lastTimestamp

    def checkWin(self, cell):
      win = False
      winCells = list()
      #Top row
      if cell <= 2:
        if self.used[0] == self.used[1] and self.used[0] == self.used[2]:
          print 'top row win'
          for i in range(3):
            winCells.append(i)
          win = True
      #Middle row
      if cell >= 3 and cell <=5:
        if self.used[3] == self.used[4] and self.used[3] == self.used[5]:
          print 'middle row win'
          for i in range(3, 6):
            winCells.append(i)
          win = True
      #Bottom row
      if cell >= 6:
        if self.used[6] == self.used[7] and self.used[6] == self.used[8]:
          print 'bottom row win'
          for i in range(6, 9):
            winCells.append(i)
          win = True
      #Left column
      if cell%3 == 0:
        if self.used[0] == self.used[3] and self.used[0] == self.used[6]:
          print 'left column win'
          for i in range(0, 7, 3):
            winCells.append(i)
          win = True
      #Middle column
      if cell%3 == 1:
        if self.used[1] == self.used[4] and self.used[1] == self.used[7]:
          print 'middle column win'
          for i in range(1, 8, 3):
            winCells.append(i)
          win = True
      #Right column
      if cell%3 == 2:
        if self.used[2] == self.used[5] and self.used[2] == self.used[8]:
          print 'right column win'
          for i in range(2, 9, 3):
            winCells.append(i)
          win = True
      #Top-left diagonal
      if cell%4 == 0:
        if self.used[0] == self.used[4] and self.used[0] == self.used[8]:
          print 'top-left diagonal win'
          for i in range(0, 9, 4):
            winCells.append(i)
          win = True
      #Top-right diagonal
      if cell == 2 or cell == 4 or cell == 6:
        if self.used[2] == self.used[4] and self.used[2] == self.used[6]:
          print 'top-right diagonal win'
          for i in range(2, 7, 2):
            winCells.append(i)
          win = True

      if win:
        self.markWin(winCells)
        self.endGame(self.used[cell])

    def markWin(self, *winCells):
      cellList = winCells[0]
      print winCells
      print cellList
      for cell in cellList:
        print cell
        self.canvas.itemconfigure(self.cells[cell/3, cell%3], fill=self.green)

    def endGame(self, winningIcon):
      tkMessageBox.showinfo('Game Over!', 'Player %s wins!' %winningIcon)
      self.sock.close()


def main():

    root = Tk()
    root.geometry('300x300+300+300')
    app = Grid(root)
    root.mainloop()

    app.sock.close()

if __name__ == '__main__':
    main()
