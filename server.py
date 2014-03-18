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
      info = '%s %f' %(message, time.time())
      print 'icon: %s, last: %s' %(icon, last)
      if icon != last:
        broadcast(info)
        print 'sent'
      else:
        print 'not sent'

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
last = ''

sock.listen(2)
while True:
    conn, addr = sock.accept()
    thread.start_new_thread(newThread, (conn, icon))
    if icon == 'X':
        icon = 'O'
    else:
        icon = 'X'
    #conn.send('Thank you for connecting')
    #conn.close()
