from utility import *
'''
Contains methods used to check whether the command sent by the
client is valid or not. 

All these methods return booleans. It returns True if the command
is valid.

Each command has its own set of checks to check due to their
differing nature

Note that when a command is sent and "#" is used in parameter
locations, it means that the parameter should be disregarded.
However, it is not always allowable to disregard a parameter.
'''



def getExitCheckResponse(clientCommandTokens):
	if (len(clientCommandTokens) != 1):
		return "BAD|EXIT command has no parameters"
	else:
		return "OK|EXIT"

'''
Checks whether the GET command sent by the client is valid

GET command must always have a filename parameter and may or may
not have a key parameter.

If no key is entered, the filename requested is searched for 
among the open files. Method returns False if filename is not
found.

If a key is entered, a check is performed to see if any files
are protected by that key. If such a file/s does not exist,
method returns False
'''
def getGetCheckResponse( clientCommandTokens):
	filename = clientCommandTokens[1]
	key = clientCommandTokens[2]
	fileValid = False 
	keyValid = False

	# no filename entered
	if (filename == "#"):
		return "BAD|GET requires a filename"

	# if a key was not input
	if (key == "#"):
		keyValid = True
		if (isStringInFile("open_files.txt", filename)):
			fileValid = True
		else:
			return "BAD|File does not exist"


	# if a key was input
	elif (key != "#"):
		if (isStringInFile("keys.txt", key)):
			keyValid = True
			if (isStringInFile(key+".txt", filename)):
				fileValid = True
			else:
				return "BAD|File with that key does not exist"
		else:
			return "BAD|Key invalid"


	# send result to client
	if (keyValid and fileValid):
		return "OK|GET"
	else:
		return "BAD|unknown error"

'''
Checks whether the QUERY command sent by the client is valid

QUERY command should always have the filename as "#" and may
or may not have a key parameter. If a filename is entered,
method returns False.

If a key is entered, a check is performed to see if any files
are protected by that key. If such a file/s does not exist,
method returns False
'''
def getQueryCheckResponse(clientCommandTokens):
	filename = clientCommandTokens[1]
	key = clientCommandTokens[2]
	keyValid = False


	# filename entered
	if (filename != "#"):
		return "BAD|QUERY cannot have filename parameter"

	# if a key was not input
	if (key == "#"):
		keyValid = True
	
	# if a key was input
	else:
		keyValid = isStringInFile("keys.txt", key)


	# send result to client
	if (keyValid):
		return "OK|QUERY"

	else:
		return "BAD|invalid key"
	
'''
Checks whether the POST command sent by the client is valid

POST command must always have a filename parameter and may or may
not have a key parameter.

The filename input is searched for among all files in the server
to confirm the filename is unique. If it is not unique, method
returns False.
'''
def getPostCheckResponse( clientCommandTokens):
	filename = clientCommandTokens[1]
	key = clientCommandTokens[2]
	fileValid = False 
	keyValid = False


	# no filename entered
	if (filename == "#"):
		return "BAD|POST requires a filename"


	# filename entered
	else:
		fileValid = not isStringInFile("allFiles.txt", filename)
	
		if (fileValid == False):
			return "BAD|Filename used, try a different filename"

	# no key
	if (key == "#"):
		keyValid = True

	# key entered
	else:
		keyValid = True

	# send result to client
	if (keyValid and fileValid):
		return "OK|POST"
	else:
		return "BAD|Unknown error"