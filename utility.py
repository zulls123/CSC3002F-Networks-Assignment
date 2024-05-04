'''
This file contains methods which are used several times throughout
the different files.
'''

# This method searches for the "checkFor" string within the file
# that was input.

# returns a boolean. True if the string was found.
def isStringInFile( filename, checkFor ):
	file = open( filename, "r")
	fileLines = file.readlines()
	file.close()
	result = False
	for f in fileLines:
		if (checkFor == f.strip()):
			result = True
			break
	return result

# This method returns an array containing all the lines within
# the file that was input
def getFileLines( filename ):
	file = open( filename, "r")
	fileLines = file.readlines()
	file.close()
	return fileLines

# Method controls whether a debug string should be printed or
# not. 

# If the current debug value is more than or equal to the
# debug's string, then it is printed.
def debugPrint(line, debugValue, dubugValueRequired):
	if (dubugValueRequired >= debugValue):
		print(line)