#!/usr/bin/env python

import socket
import thread
import time

def newThread(conn, icon):
  print '%s thread started' %icon
  conn.send(icon)
  players[icon] = conn
  print players

  while True:
    message = conn.recv(buf)
    print '%s thread received: %s' %(icon, message)
    if message != 'Let me come play!':
      broadcast(message)
    time.sleep(10)
    print '%s thread listening' %icon

def broadcast(info):
  print 'broadcast %s' %info
  for name, conn in players.items():
    conn.send(info)

sock = socket.socket()
host = ''
buf = 1024
port = 8888
sock.bind((host, port))
icon = 'X'
players = {}

sock.listen(2)
while True:
    conn, addr = sock.accept()
    thread.start_new_thread(newThread, (conn, icon))
    if icon == 'X':
        icon = 'O'
    else:
        icon = 'X'

    '''for name, conn in players.items():
      message = conn.recv(buf)
      print 'server received: %s' %message
      if message:
        broadcast(message)'''
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
