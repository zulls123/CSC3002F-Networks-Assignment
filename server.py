import socket
import sys
from serverChecks import *
from serverCommands import *
from utility import *

'''
Main method which runs a file storage server which one client can 
connect to at a time. Server provides the client with commands to
retrieve data, upload data and query what files are available.

Files may have an open or protected state. Protected files can only
be accessed or viewed if the client provides the file's key. 
	- A key functions as a password

If the server encounters any errors while running, the appropriate
error along with explanation is sent to the client.

'''
def getCheckResponse(commandTokens):
	commandStatus = ""
	commandCode = commandTokens[0]

	if ( len(commandTokens) !=3 ):
		commandStatus ="BAD|message does not have 3 parameters"

	elif ( commandCode == "GET"):
		commandStatus = getGetCheckResponse(commandTokens)

	elif ( commandCode == "QUERY"):
		commandStatus = getQueryCheckResponse(commandTokens)

	elif ( commandCode == "POST"):
		commandStatus = getPostCheckResponse(commandTokens)

	else:
		commandStatus = "BAD|note a valid command type"

	return commandStatus

def executeCommand(connectionSocket, commandTokens):
	commandCode = commandTokens[0]
	if ( commandCode == "EXIT"):
		print("exit")
		executeExit(connectionSocket)

	elif ( commandCode == "GET"):
		print("get")
		executeGet(connectionSocket, commandTokens)

	elif ( commandCode == "QUERY"):
		print("query")
		#executeQuery(connectionSocket, commandTokens)
		
	elif ( commandCode == "POST"):
		print("post")
		executePost(connectionSocket, commandTokens)

def main():

	#-----------server setup----------------------
	serverIP = socket.gethostbyname( socket.gethostname() )	
	serverPort = 7777
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket.bind( (serverIP, serverPort) )  #2 sets of brackets as .bind takes a tuple argument
	serverSocket.listen(1)	#only listens for one client

	print("networks_waffle started!")
	print("Server IP: " +serverIP)
	#while True:


	#client connects to server
	connectionSocket, connectionAddress = serverSocket.accept() 


	# This while loop allows the server to receive commands more than
	# once when a client connects. Server exits the loop when it receives
	# the EXIT command from the client.
	while True:
		# 	INITIAL COMMUNICATION STAGE
		#		- receiving the clients command
		#		- during this stage, server sends one message


		# Commands sent by client should have " " as a delimeter
		clientCommand = connectionSocket.recv(1024).decode()
		commandTokens = clientCommand.split()
		commandCode = commandTokens[0]


		# 	VALIDATION STAGE
		#		- checks if command is valid
		#		- during this stage, server sends one message
		commandStatus=getCheckResponse(commandTokens)
		connectionSocket.send(commandStatus.encode())



		commandStatusTokens = commandStatus.split("|")
		counter = 0
		commandSuccessful = False

		if ( commandStatusTokens[0] == "BAD"):
			print("Invalid Command")
		# 	 EXECUTION STAGE
		#		- amount of client-server communication depends on the
		#		command being executed
		else:
			if (commandStatusTokens[1] == "EXIT"):
				executeExit(commandTokens)
				break
			else:
				executeCommand(connectionSocket, commandTokens)

	print("connection closed")

if __name__ == "__main__":
	main()

	
# if ( commandStatusTokens[0] == "OK"):
# 	while (counter <2 and not commandSuccessful):
# 		counter +=1
# 		if (commandStatusTokens[0] == ("OK")):
# 			executeCommand(connectionSocket, commandTokens)
# 		response = connectionSocket.recv(1024).decode()
# 		a = response.split("|")
# 		if (a[0] == OK):
# 			commandSuccessful = True

# 	if (counter==3):
# 		connectionSocket.send("BAD|Command not successful 3 times. try again".encode())
# else:
# 	print("Invalid command")
# 	continue