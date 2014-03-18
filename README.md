tic-tac-toe
===========

Riley Lundquist
Operating Systems & Networking
March 17, 2014

This is a networked tic-tac-toe game, which allows two users to play against each other on separate machines. The server listens for connections from two clients and starts a separate thread to handle messages from each of them. After receiving a message, it broadcasts it to the opponent.

The clients get their icon (X or O) from the server when they connect. They then take turns making moves (and sending them) when the user clicks on a box in the grid and waiting for the opponent to make a move. Any duplicate moves or attempts to make two turns in a row are rejected. When a player wins the game, the winning boxes in the grid are highlighted, and a dialog declares the winner.

Running the program:
On the server machine, run
	python server.py &
Open one client on the same machine with
	python client.py
Connect to the server machine with the second machine
	ssh <server> -L 8888:localhost:8888
And open the client on that machine with
	python client.py localhost:8888
Clients may connect in any order, but whichever connects first will have the first move.
