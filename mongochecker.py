import pymongo
import sys

host = sys.argv[1]
port = int(sys.argv[2])

	
# Timeout is to make sure it doesn't load for too long. 5 seconds should be enough
client = pymongo.MongoClient(host,port,serverSelectionTimeoutMS=5000)

try:
	client.database_names()
	print "Server is vulnerable!"
except Exception as e:
	error = str(e)
	
	if pymongo.errors.ConnectionFailure:
		print "Reasons for no connection:"
		print "MongoDB is not accessable to the public."
		print "There is no MongoDB instance."
		print "The server could be really slow."
		print "Or the wrong port is being used."
	# Have mercy on me for using this if statement
	if "authorized" in error and "execute" in error:
		print "Auth is required to access this MongoDB instance. Which means that it's secure :p"
		
	
	# The pass is used so that the long exception is not printed
	pass
