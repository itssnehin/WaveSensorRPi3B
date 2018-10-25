import subprocess
import os
import time
import socket


host = '192.168.1.15'
port = 5560

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
flag = True
while flag:
	print("Options:")
	print("1. Change tolerance")
	print("2. Import data logs")
	print("3. Start/Reset the Application")
	print("4. Stop the application")
	print("5. Exit")
	command = str(input(" ")).strip()
	s.send(str.encode(str(command)))
	reply = s.recv(1024)
	os.system('clear')
	print(reply.decode('utf-8'))

	# need to set value
	if (command == '1'):
		tolerance = input("")
		s.send(str.encode(str(tolerance)))
		reply = s.recv(1024)
		print(reply.decode('utf-8'))
		#send msg to server
	if (command == '2'):
		reply = s.recv(1024)
		print(reply.decode('utf-8'))
	if(command == '5'):
		flag = False
		break
    
s.close()
