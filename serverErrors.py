
# Send error message to client to indicate that a key or keys
# that were input were invalid in the form:


# If key is too short or long
# 	"The key "123" is too short/long. Keys must be 3 - 10 char."
# If it is the incorrect key for a file
# 	"Incorrect key for 'potato.txt' entered"
# If no key is entered
# 	"Please enter a key. If a key is not applicable place '#'
# 	in the key paramater"
def getKeyError():
	errorMsg = "ERR Key error"
	return errorMsg




# Send error message to client to indicate that a file or files
# that were input were invalid in the form depending on the errorCode
# that throws it:

# If errorCode indicates GET command the following is sent
# 	"No files on network_waffle has the name 'potato_milkshake.txt'"  
# If errorCode indicates UPLOAD command the following is sent
# 	"File name 'potato_milkshake.txt' is already used. Please try
# 	a different file name." 

# "The key "245" is not a valid key for any files on the server"
def getFileError():
	errorMsg = "ERR File error"
	return errorMsg


# Send an error message to the client to indicate that the command
# used is incorrect.

# "'APPLE' is not a valid command. Use HELP command to view the 
# commands"
def getCommandError():
	errorMsg = "ERR Command error"
	return errorMsg