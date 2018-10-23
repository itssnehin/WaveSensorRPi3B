def main():
	# Main function to sense a wave
	
	time.sleep(0.1)
	value = mcp.read_adc(1) # channel 1 used
	print("Value: " + str(value))
 

#Globals
#GPIO.cleanup()
Time = []

ch1 = [0]*16 # Channel for the knob
GPIO.setmode(GPIO.BCM)
interval = 0 # Time passed

    # Software SPI configuration (in BCM mode):
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

if __name__ == '__main__':
	main()