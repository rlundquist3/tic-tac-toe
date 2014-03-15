#!/usr/bin/env python

import socket

sock = socket.socket()
host = socket.gethostname()
port = 8080
sock.bind(('', port))

icon = 'X'

sock.listen(2)
while True:
    conn, addr = sock.accept()
    message = conn.recv(1024)
    if message:
        print 'Server got:', message
        if message == 'Let me come play!':
            conn.send(icon)
            if icon == 'X':
                icon = 'O'
            else:
                icon = 'X'
    #conn.send('Thank you for connecting')
    #conn.close()

