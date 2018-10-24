import RPi.GPIO as GPIO
import time
import os
import Adafruit_MCP3008
import subprocess
import sys
import 
#detect a falling signal
#def checkWave():

def main():
	# Main function to sense a wave
	global interval, light, mcp, counter
	print("Expose to light for 5s!")
	time.sleep(1)


	#get an average value for light on (HIGH)
	for i in range(1,6):

		time.sleep(1)
		os.system("clear")
		print(str(i) + "s")
		light.append(mcp.read_adc(1))

	os.system('clear')
	highVal = sum(light)/5
	print("Light average value: " + str(highVal))
	time.sleep(0.5)
	print("Ready!")

	while(1):
		
		time.sleep(0.1)
		final = mcp.read_adc(1) # channel 1 used

		#print(final)
		

		if (final > (highVal + tolerance)):
			os.system('clear')
			print("Wave started")

			while (final > (highVal + tolerance)):

				#print(final)
				time.sleep(0.05)
				interval += 0.05
				final = mcp.read_adc(1)

				
			counter += 1
			Time.append(interval)
			os.system('clear')
			print("Wave ended")
			print(str(interval) + "s")
		
		
		

		interval = 0

		 		


#Globals
#GPIO.cleanup()
print("Setting up")
time.sleep(2)
light = []
Time[]	# Array of time taken of each wave
speed[] = []# Array to work out speed of waves
setup = []
ch1 = [0]*16 # Channel for the knob
GPIO.setmode(GPIO.BCM)
interval = 0 # Time passed
counter = 0
    # Software SPI configuration (in BCM mode):
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

#Server setup needs to be done
for eachArg in sys.argv:
	data
f = open('logs.txt')

os.system("clear")
if __name__ == '__main__':
	main()