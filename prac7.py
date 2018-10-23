import RPi.GPIO as GPIO
import time
import os
import Adafruit_MCP3008

#detect a falling signal
#def checkWave():


def main():
	# Main function to sense a wave
	global interval, light, mcp
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

		tolerance = 10 # tolerance for adc values to fluctuate
		#print(final)
		if (final > (highVal + tolerance)):
			os.system('clear')
			print("Wave started")

			while (final > (highVal + tolerance)):

				#print(final)
				time.sleep(0.05)
				interval += 0.05
				final = mcp.read_adc(1)

				

			os.system('clear')
			print("Wave ended")
			print(str(interval) + "s")
		
		interval = 0

		 		


#Globals
#GPIO.cleanup()
print("Setting up")
time.sleep(2)
light = []

ch1 = [0]*16 # Channel for the knob
GPIO.setmode(GPIO.BCM)
interval = 0 # Time passed

    # Software SPI configuration (in BCM mode):
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

#Server setup

os.system("clear")
if __name__ == '__main__':
	main()