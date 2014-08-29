#import socket


#TCP_IP = '127.0.0.1'
#TCP_PORT = 5005
#BUFFER_SIZE = 1024
#MESSAGE = "Hell"

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((TCP_IP, TCP_PORT))
#s.send(MESSAGE)


#print "received data:"


import socket 
import sys 
import binascii
import struct

while 1:

	host = '192.168.137.182' 
	port = 5005 
	size = 1024 
	s = None 
	try: 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		s.connect((host,port)) 
	except socket.error, (value,message): 
		if s: 
			s.close() 
		print "Could not open socket: " + message 
		sys.exit(1) 
		
	MSG = raw_input("Enter something: ")
	message = map(ord,MSG)
	values = []
	values.append(len(MSG))
	values.extend(message)
	values = bytearray(values)
	#packer = struct.Struct('I 2s f')
	#packed_data = packer.pack(*values)
	print values
	s.sendall(values) 
	data = s.recv(size) 
	s.close() 
	print 'Received:', data
