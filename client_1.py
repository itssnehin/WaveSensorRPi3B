import subprocess
import os
import time
import socket


host = 'raspberrypi'
port = 5560

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    print("Options:")
    print("1. Change tolerance")
    print("2. Import data logs")
    print("3. Start the Application")
    print("4. Stop the application")
    print("5. Exit")
    command = input(" ")
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply.decode('utf-8'))
    if(command == '5'):
    	break
    
s.close()
