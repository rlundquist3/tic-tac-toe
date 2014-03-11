#!/usr/bin/env python

import socket
from Tkinter import Tk, Frame, BOTH, Canvas

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background='white')
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Tic-Tac-Toe")
        self.pack(fill=BOTH, expand=1)
        
        '''canvas = Canvas(self)
        canvas.create_rectangle(100, 0, 105, 300, outline='#0fb', fill='#0fb')
        canvas.create_rectangle(200, 0, 205, 300, outline='#0fb', fill='#0fb')
        canvas.pack(fill=BOTH, expand=1)'''
        
        
        

def main():
    
    sock = socket.socket()
    host = socket.gethostname()
    port = 8080
    sock.connect((host, port))
    
    sock.send('Let me come play!')
    message = sock.recv(1024)
    if message:
        print 'Client got:', message
        #print len(message)
        #print message
    sock.close()
    
    root = Tk()
    root.geometry('300x300+300+300')
    app = Example(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()

'''sock = TicTacToeSocket()
host = socket.gethostname()
port = 8080

sock.connect(host, port)'''
