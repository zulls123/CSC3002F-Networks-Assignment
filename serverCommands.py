from utility import *
import hashlib
'''
File contains methods which execute the client's commands.

By this point the command has been confirmed to be valid
and the command may be executed.
'''
#handle uploads
def executeExit(connectionSocket):
	connectionSocket.close()

# Method sends available open filenames to the client

# If a key was entered, it sends the filenames protected
# by that key in addition to the open filenames
def executeQuery(connectionSocket, commandTokens):
	filename = commandTokens[1]
	key = commandTokens[2]

	final = ""
	openFiles = getFileLines("open_files.txt")
	for line in openFiles:
		final = final + line.strip() + ","

	final = final[:-1]
	if (key != "#"):
		final = final + "|"
		keyFiles = getFileLines(key+".txt")
		for line in keyFiles:
			final = final + line.strip() + ","
		final = final[:-1]

	message = final
	connectionSocket.send( message.encode() )


# Method sends requested file to the client

# Server first waits for confirmation that the client is
# ready to receive the file.

# A hashcode is sent as well to confirm that the file 
# received by the client is identical to the one the
# server sent

def executeGet(connectionSocket, commandTokens):
	filename = commandTokens[1]
	key = commandTokens[2]

	#allow user to download files
	while (1):
		


# Method receives file sent by the client

# Server first sends confirmation that it is ready to receive
# the file.

# A hashcode is received as well to confirm that the file 
# received by the server is identical to the one the client
# sent
def executePost(connectionSocket, commandTokens):
	filename = commandTokens[1]
	key = commandTokens[2]

	# #receive file
	# #receive file name
	print("Receiving filename.")
	file = open(filename,"wb")
	# #connectionSocket.send("Filename received.".encode())
	

	# # #receive file data
	data = connectionSocket.recv(4096).decode()
	file.write(data)
	connectionSocket.send("File uploaded".encode())

	# #get hash from client
	received_hash = connectionSocket.recv(1024).decode()
	print(received_hash)

	# #read file contents and put into hash
	file_contents = bytearray()
	file_contents+=data

	# # #compare computed and received hash
	# # #compute hash of received file
	hash_object = hashlib.sha256()
	hash_object.update(data)
	computed_hash = hash_object.hexdigest()

	print(computed_hash)

	# #if received_hash == computed_hash:
	# # 	print("SUCCESSFUL")
	
	
	



	#file.close()

	# # #new method to receive file
	# received_hash = connectionSocket.recv(1024).decode()
	# # #print received hash
	# print("Received hash: ", received_hash)

	# # #receive file contents
	# file_contents = bytearray()
	# while True:
	# 	data = connectionSocket.recv(1024).decode()
	# 	if not data:
	# 		break
	# 	file_contents+=data

	# # #compare computed and received hash
	# # #compute hash of received file
	# hash_object = hashlib.sha256()
	# hash_object.update(file_contents)
	# computed_hash = hash_object.hexdigest()

	# print("Computed hash:" , computed_hash)

	# if received_hash == computed_hash:
	# 	print("SUCCESSFUL")
	# else:
	# 	print('UNSUCCESSFUL')




	


#if __name__ == "__main__":
 #   main()
