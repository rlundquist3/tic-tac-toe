#!/usr/bin/env python

import socket
import thread

def newThread(icon):
  print '%s thread started' %icon
  conn.send(icon)
  players[icon] = conn

def broadcast(info):
  print 'broadcast %s' %info
  for name, conn in players.items():
    conn.send(info)

sock = socket.socket()
host = ''
buf = 1024
port = 8080
sock.bind((host, port))

icon = 'X'

sock.listen(2)
while True:
    conn, addr = sock.accept()
    thread.start_new_thread(newThread, (icon))
    if icon == 'X':
        icon = 'O'
    else:
        icon = 'X'

    for name, conn in players.items():
      message = conn.recv(buf)
      if message:
        broadcast(message)
    '''while True:
        message = conn.recv(buf)
        if message:
            print 'Server got:', message
            if message == 'Let me come play!':
                conn.send(icon)
                if icon == 'X':
                    icon = 'O'
                else:
                    icon = 'X'
            else:
                conn.send(message)'''
    #conn.send('Thank you for connecting')
    #conn.close()
