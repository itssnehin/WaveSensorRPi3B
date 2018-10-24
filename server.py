import subprocess
import os
import time
# Function to start the raspberry pi
def start(tolerance):
	global start
	run = subprocess.Popen(['python', 'prac7.py', tolerance])
	print("Running")
	start = True

# Function to stop the raspberry pi
def stop():
	global start
	end = subprocess.Popen(['exit()'])
	print("Stopped!")
	start = False

start = False # State of whether the Raspberry Pi has been connnected to or not
device = input("Enter the address of the Raspberry Pi <username>@address: \n") # Contains the IPv4 Address of Pi
server = input("Enter the user and address of this machine <username>@address : \n") # Contains the IPv4 Address of this PC

print("Attempting to connect to the RPi...")
p = subprocess.Popen(["ssh", device])
os.system('clear')
print('Connected!')

os.system('clear')

while(1):

	os.system('clear')
	print("          Options:               ")
	print("---------------------------------")
	print("1. Change tolerance")
	print("2. Import data logs")
	print("3. Start the Application")
	print("4. Stop the application")
	print("5. Exit")
	ans = input(" ")

	if (ans == 1):
		stop()
		tolerance = int(input("Enter the tolerance (Recommended 10-30 value)"))
		start(tolerance)
	elif(ans == 2):
		if connnected:
			transfer = subprocess.Popen(['scp', 'logs.txt', server + ":"])
		else:
			print("Start the application first!")
			time.delay(2)
	elif(ans == 3):
		start()
	elif(ans == 4):
		stop()
	elif(ans == 5):
		exit()
	else:
		print("Enter a valid choice")


