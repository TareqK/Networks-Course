import socket 
import sys
import json
import time
if __name__ =="__main__":
	port=8080#reserve the port
	socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM);#create a socket
	socket.connect(('localhost',port))#connect to the server
	while True :#forever
		try :
			s = input('inser a number between 1-25 : ')#ask user for offset
			text = input('Insert text : ');#ask user for string
			data=dict()#reserve a new dictionary/hashmap
			data['num'] =s;#add the offset with key 'num'
			data['text'] =text;#add the text with key 'text'
			socket.send(str.encode(json.dumps(data)))#send the data encoded as json
			received = socket.recv(4096)#receive the response
			if not received  :# if there is no response
				raise#throw an error
			else :#otherwise
				my_string = received.decode("utf-8")#decode the received bytes into string
				print(my_string)#print the string
		except :#catch any error
			print("exiting")#print a message
			break;#exit the while loop
	socket.close()#close the socket
			
		
