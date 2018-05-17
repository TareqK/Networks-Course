
import socket 
import sys
import json
def encrypt(s,text):
	s=int(s)
	result = ''   
	for i in range(len(text)):
		char = text[i]
		# Encrypt uppercase characters
		if (char.isupper()):
			result += chr((ord(char) + s-65) % 26 + 65)
		# Encrypt lowercase characters
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)
	return result
if __name__ == "__main__": 
	result = ""
	s = socket.socket()# create a socket   
	port = 8080 # define the port       
	s.bind(('localhost', port)) # bind the socket to localhost and port 8080
	s.listen(5) #listen for 5 connections maximum   
	while True:# forever
		c, addr = s.accept() #accept the connection, with socket c and address addr
		while True :# forever on C
			try :
				data = (c.recv(4096))#check for data and if the socket has closed
				if not data :#if the socket has closed
					raise# throw a new error
				else :#otherwise
					jsonArray = json.loads(str.decode(data))#parse the incoming data
					c.send(encrypt(jsonArray['num'],jsonArray['text']))#return the encrypted data to the client
			except :#catch any error thrown
				print("connection closed")#print a message
				c.close()#close the connection
				break#exit the while loop
	
