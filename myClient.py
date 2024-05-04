import socket
import sys
import hashlib


def upload_file_with_hash(clientSocket, filename):

	# # #opening and reading the file data
	file = open(filename, 'rb')
	data = file.read(4096)
	
	# # #msg = client.recv(SIZE).decode(FORMAT)
	# # #print (f"[SERVER]: msg")

	# # #sending file data to server
	clientSocket.send(data)


	# # new method
	hash_object = hashlib.sha256()
	# with open (filename, 'rb') as f:
	# 	while True:
	# 		data = f.read(1024)
	# 		if not data:
	# 			break
	hash_object.update(data)
	file_hash = hash_object.hexdigest()

	# # print hash
	print (file_hash)

	# # send hash
	clientSocket.sendall(file_hash.encode())

	# # #send contents of file
	# with open(filename, 'rb') as f:
	# 	while True:
	# 		data = f.read(1024)
	# 		if not data:
	# 			break
	# 		clientSocket.sendall(data)

	 



	#add hash

	#file.close()
	



def receiveQueryResult():
	queryResult = clientSocket.recv(1024).decode()
	tokens = queryResult.split("|")

	output = tokens[0].split("," )
	for l in output:
		print("open       "+l)

	if (len(tokens) == 2):
		output = tokens[1].split("," )
		for l in output:
			print("protected  "+l)
	print("")

def receiveGetFile():
	print("get file")

def sendPostFile():
	print("post file")

def exit(clientSocket):
	clientSocket.close()

def main():
	serverIP = sys.argv[1]
	serverPort = 7777

	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientSocket.connect( (serverIP, serverPort) )

	print(
	'''
You've connected to networks_waffle

Commands:
	GET <filename> <key (if file is protected)>
	QUERY # <key (to view files protected by that key as well)>
	POST <filename> <key (to protect file with key)

	''')


	while True:
		#	INITIAL COMMUNICATION STAGE
		print("Please enter a command:")
		commandToServer = input("")
		commandToServerTokens = commandToServer.split(" ")

		clientSocket.send( commandToServer.encode() )

		#	VALIDATION STAGE
		commandCheck = clientSocket.recv(1024).decode()
		commandCheckTokens = commandCheck.split("|")
		
		print(commandCheckTokens[0])
		if (commandCheckTokens[0] == "BAD"):
			print(commandCheckTokens[1])
		#	EXECUTION STAGE
		else:
			command = commandCheckTokens[1]
			if 	(command == "GET"):
				print("get")
			elif (command == "POST"):
				#print("post")
				upload_file_with_hash(clientSocket,commandToServerTokens[1])
			elif (command == "QUERY"):
				print("query")
			elif (command == "EXIT"):
				clientSocket.send( "OK|#".encode() )
				print("exit")
				break
			else:
				print("unknown error")
			clientSocket.send( "OK|#".encode() )
		print("")


		

if __name__ == "__main__":
	main()