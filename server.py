#!/usr/bin/env python

import socket

sock = socket.socket()
host = socket.gethostname()
port = 8081
sock.bind((host, port))

sock.listen(5)
while True:
    conn, addr = sock.accept()
    message = conn.recv(1024)
    if message:
        print 'Server got:', message
        conn.send(message)
    #conn.send('Thank you for connecting')
    conn.close()
    
'''sock = TicTacToeSocket()
host = socket.gethostname()
port = 8080
sock.bind(host, port)

sock.listen(5)
while True:
    conn, addr = sock.accept()
    conn.send('connection!')
    conn.close()'''

