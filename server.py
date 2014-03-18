#!/usr/bin/env python

'''
Riley Lundquist
Tic-Tac-Toe
March 17, 2014

server.py

This is the server for a two-player networked tic-tac-toe
game. It listens for connections from two clients, and starts
a thread for each to listen for plays and broadcast them to
the other player.
'''

import socket
import thread
import time

#Threads for clients start here. Listens for messages and
#calls method to broadcast them.
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
      broadcast(info)

#Broadcasts moves to clients
def broadcast(info):
  print 'broadcast %s' %info
  for name, conn in players.items():
    conn.send(info)

#Sets up socket
sock = socket.socket()
host = ''
buf = 1024
port = 8888
sock.bind((host, port))
icon = 'X'
players = {}

#Accepts up to two connections and begins a thread for each
sock.listen(2)
while True:
    conn, addr = sock.accept()
    thread.start_new_thread(newThread, (conn, icon))
    if icon == 'X':
        icon = 'O'
    else:
        icon = 'X'
