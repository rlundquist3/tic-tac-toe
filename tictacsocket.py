#!/usr/bin/env python

import socket

class TicTacToeSocket:
    
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
            
    def connect(self, host, port):
        self.sock.connect((host, port))
        
    def accept(self):
        self.sock.accept()
        
    def sendMsg(self, msg):
        total = 0
        while total < MSGLEN:
            sent = self.sock.send(msg[total:])
            if sent == 0:
                raise RuntimeError('socket connection broken')
            total = total + sent
            
    def recvMsg(self):
        msg = ''
        while len(msg) < MSGLEN:
            part = self.sock.recv(MSGLEN-len(msg))
            if part == '':
                raise RuntimeError('socket connection broken')
            msg = msg + part
        return msg
    
    