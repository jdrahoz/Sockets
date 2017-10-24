
# ----------------------------------- #
#
#	Drahozal_TCP_server.py
#
#	EECS 563 Socket Programming
# 	TCP Server
#
# ----------------------------------- #

# imports
from socket import *
import sys

# constants
BUFF_SIZE = 1024

# ----------------------------------- #

# run main program
def run ():

	# client
	if (len (sys.argv) == 3):
		client (sys.argv[1], sys.argv[2])

	# server
	elif (len (sys.argv) == 2):
		server (sys.argv[1])

	# other
	else:
		print "ERROR: invalid arguments\n"

# ----------------------------------- #

# client side
def client (serverIP, serverPort):

	print " ----------"
	print "TCP server @", str (serverIP) + ":" + str (serverPort)
	print " ----------\n"

	while True:

		# get input
		message = raw_input ("Please enter the statement:	")

		# establish connection
		serverPort = int (serverPort)
		clientSocket = socket (AF_INET, SOCK_STREAM)
		clientSocket.connect ((serverIP, serverPort))

		# send & receive
		clientSocket.send (message)
		recvMessage = clientSocket.recv (BUFF_SIZE)
		print "Return text from the server:	", recvMessage, "\n"

		# close connection
		clientSocket.close ()

# server side
def server (serverPort):

	# establish connection
	serverPort = int (serverPort)
	serverSocket = socket (AF_INET, SOCK_STREAM)
	serverSocket.bind (('', serverPort))
	serverSocket.listen (1)

	while True:

		# receive & send
		connectionSocket, addr = serverSocket.accept ()
		message = connectionSocket.recv (BUFF_SIZE)
		connectionSocket.send (message.upper ()) # to uppercase

		# close connection
		connectionSocket.close ()

# ----------------------------------- #

# run main program
run ()

# ----------------------------------- #
