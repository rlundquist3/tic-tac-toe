#!/usr/bin/env python

import socket
from Tkinter import Tk, Frame, BOTH, Canvas

class Grid(Frame):
    def __init__(self, parent):
        self.sock = socket.socket()
        self.host = socket.gethostname()
        self.port = 8080
        self.sock.connect(('', self.port))
        
        self.sock.send('Let me come play!')
        self.message = self.sock.recv(1024)
        if self.message:
            print 'Client got:', self.message
            self.icon = self.message
        
        if self.icon == 'X':
            self.otherIcon = 'O'
        else:
            self.otherIcon = 'X'
        
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        
        self.dimension = 100
        self.cells = {}
        self.used = list()
        for i in range(9):
            self.used.append('n')
        
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
                self.cells[row, column] = self.canvas.create_rectangle(x1, y1, x2, y2, outline='#000')
                self.canvas.bind('<ButtonRelease-1>', self.cellClick)
        
        self.canvas.pack(fill=BOTH, expand=1)
        
    def cellClick(self, event):
        print 'Click at', event.x, ',', event.y
        row = event.y/self.dimension
        column = event.x/self.dimension
        print ('%d %d' %(row, column))
        self.sock.send('%d %d' %(row, column))
        self.update(row, column, self.icon)
    
    def update(self, row, column, icon):
        x = column*self.dimension + self.dimension/2
        y = row*self.dimension + self.dimension/2
        
        if self.used[3*row + column] == 'n':
            self.canvas.create_text(x, y, text=icon)
            self.used[3*row + column] = self.icon
            if self.checkWin(3*row + column):
                print 'winner!'
        
        print 'Used:', self.used
        
        if icon == self.icon:
            self.wait()
        
    def wait(self):
        while True:
            conn, addr = self.sock.accept()
            message = conn.recv(1024)
            if message:
                print 'Client', self.icon, 'got', message
                #self.update()
                break
    
        
    def checkWin(self, cell):
        #Top row
        if cell <= 2:
            if self.used[0] == self.used[1] and self.used[0] == self.used[2]:
                print 'top row win'
                return True
        #Middle row
        if cell >= 3 and cell <=5:
            if self.used[3] == self.used[4] and self.used[3] == self.used[5]:
                print 'middle row win'
                return True
        #Bottom row
        if cell >= 6:
            if self.used[6] == self.used[7] and self.used[6] == self.used[8]:
                print 'bottom row win'
                return True
        #Left column
        if cell%3 == 0:
            if self.used[0] == self.used[3] and self.used[0] == self.used[6]:
                print 'left column win'
                return True
        #Middle column
        if cell%3 == 1:
            if self.used[1] == self.used[4] and self.used[1] == self.used[7]:
                print 'middle column win'
                return True
        #Right column
        if cell%3 == 2:
            if self.used[2] == self.used[5] and self.used[2] == self.used[8]:
                print 'right column win'
                return True
        #Top-left diagonal
        if cell%4 == 0:
            if self.used[0] == self.used[4] and self.used[0] == self.used[8]:
                print 'top-left diagonal win'
                return True
        #Top-right diagonal
        if cell == 2 or cell == 4 or cell == 6:
            if self.used[2] == self.used[4] and self.used[2] == self.used[6]:
                print 'top-right diagonal win'
                return True
    

def main():
    
    root = Tk()
    root.geometry('300x300+300+300')
    app = Grid(root)
    root.mainloop()
    
    app.sock.close()
    
if __name__ == '__main__':
    main()
