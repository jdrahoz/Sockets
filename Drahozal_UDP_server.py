
# ----------------------------------- #
#
#	Drahozal_UDP_server.py
#
#	EECS 563 Socket Programming
# 	UDP Server
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
	print "UDP server @", str (serverIP) + ":" + str (serverPort)
	print " ----------\n"

	while True:

		# get input
		message = raw_input ("Please enter the statement:	")

		# establish connection
		serverPort = int (serverPort)
		clientSocket = socket (AF_INET, SOCK_DGRAM)

		# send & receive
		clientSocket.sendto (message, (serverIP, serverPort))
		recvMessage, serverAddress = clientSocket.recvfrom (BUFF_SIZE)
		print "Return text from the server:	", recvMessage, "\n"

		# close connection
		clientSocket.close ()

# server side
def server (serverPort):

	# establish connection
	serverPort = int (serverPort)
	serverSocket = socket (AF_INET, SOCK_DGRAM)
	serverSocket.bind (('', serverPort))

	while True:

		# receive & send
		message, clientAddress = serverSocket.recvfrom (1024)
		serverSocket.sendto (message.upper (), clientAddress) # to uppercase

# ----------------------------------- #

# run main program
run ()

# ----------------------------------- #
