import RPi.GPIO as GPIO
import time
import os
import Adafruit_MCP3008

#detect a falling signal
#def checkWave():


def main():
	# Main function to sense a wave
	global interval, light, mcp, log, speed, groupingNum, avgTime, avgFreq
	flag = 0				# flag is to indicate the pulse has begun and timer is running
	timer = 0				# measures time between the two pulses
	counter = 0
	temp = 0
	print("Calculating average light value of the room fr 5s...")


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
		
		time.sleep(0.01)	# minimal delay
		final = mcp.read_adc(1) # channel 1 used

		tolerance = 10 # tolerance for adc values to fluctuate
		#print(final)
		if (final > (highVal + tolerance)):
			os.system('clear')
			print("Wave started")

			while (final > (highVal + tolerance)):

				#print(final)
				time.sleep(0.01)
				interval += 0.01
				final = mcp.read_adc(1)
				if (flag == 0):
					start = time.time()
					flag = 1	# set flag

				

			os.system('clear')
			print("Wave ended")
			print(str(interval) + "s")
			if (interval > 5):
				break
			log.append(round(interval, 4))
			stop = time.time()
			timer = round(stop - start, 4) 	# round off to 4 decimal points
			speed.append(timer)
			flag = 0			# reset flag
			interval = 0
			counter = counter + 1
			print(counter)

			temp = temp + timer
			if (counter%groupingNum == 0):
				avgTime.append(round(temp/groupingNum, 4))
				avgFreq.append(round(groupingNum/temp, 4))
				temp = 0		# reset temp


	print("Time of waves: ")
	print(log)
	print("Counter: ")
	print(counter)
	print("Time between waves: ")
	print(speed)
	print("Avgerage number of waves per second")
	print(avgFreq)


#Globals
#GPIO.cleanup()
print("Setting up")
light = []
log = []		# stores the duration of the pulse
speed = []		# stores the duration of the wave (shadow)
counter = 0
groupingNum = 10 	# user can set this (this is the number of waves to group for the average speed)
avgTime = []		# average time between 2 waves
avgFreq = []		# average waves in 1 second


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
