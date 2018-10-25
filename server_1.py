import socket
import prac7
from threading import Thread
import RPi.GPIO as GPIO
import time
import os, sys
import Adafruit_MCP3008
host = ''
port = 5561

storedValue = "You are connected to the raspberry pi"

light = []
log = []        # stores the duration of the pulse
speed = []      # stores the duration of the wave (shadow)
counter = 0
groupingNum = 10    # user can set this (this is the number of waves to group for the average speed)
avgTime = []        # average time between 2 waves
avgFreq = []        # average waves in 1 second
loop = True

ch1 = [0]*16 # Channel for the ldr
GPIO.setmode(GPIO.BCM)
interval = 0 # Time passed
tolerance = 10
    # Software SPI configuration (in BCM mode):
CLK  = 11
MISO = 9
MOSI = 10
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

def main():
    # Main function to sense a wave
    global interval, light, mcp, log, speed, groupingNum, avgTime, avgFreq, tolerance, loop

    flag = 0                # flag is to indicate the pulse has begun and timer is running
    timer = 0               # measures time between the two pulses
    counter = 0
    temp = 0



    print("Calculating average light value of the room for 5s...")
    #get an average value for light on (HIGH)
    #
    light = []
    for i in range(1,6):

        time.sleep(1)
        #os.system("clear")
        #print(str(i) + "s")
        light.append(mcp.read_adc(1))

    os.system('clear')
    highVal = sum(light)/5
    print("Light average value: " + str(highVal))
    time.sleep(0.5)
    print("Ready! " + str(flag))


    while(loop):
        
        time.sleep(0.01)    # minimal delay
        final = mcp.read_adc(1) # channel 1 used

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
                    flag = 1    # set flag

                

            os.system('clear')
            print("Wave ended")
            print(str(interval) + "s")
            if (interval > 5):
                break
            log.append(round(interval, 4))
            stop = time.time()
            timer = round(stop - start, 4)  # round off to 4 decimal points
            speed.append(timer)
            flag = 0            # reset flag
            interval = 0
            counter = counter + 1
            print(counter)

            temp = temp + timer
            if (counter%groupingNum == 0):
                avgTime.append(round(temp/groupingNum, 4))
                avgFreq.append(round(groupingNum/temp, 4))
                temp = 0        # reset temp

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind comlete.")
    return s

def setupConnection():
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def get_tolerance():
    global tolerance
    print("Current tolerance: " + str(tolerance))
    reply = "State new tolerance value: "
    return reply

def set_tolerance(tol):
    global tolerance
    tolerance = int(tol)
    print("New value: " + str(tolerance))

def datalogs():
    reply = "Printing the average frequency of the of the wave after every 10 waves: "
    
    return reply

def start():
    reply = "Starting application"
    global loop
    loop = True
    t = Thread(target=main)
    t.start()
    #prac7.main()
    return reply

def stop():
    global loop
    loop = False
    reply = "Stopped reading"

    return reply
def shutdown():
    global s, loop
    reply = "Shutting down"
    loop = False
    s.close()
    sys.exit()

def dataTransfer(conn):
    global avgFreq
    # A big loop that sends/receives data until told not to.
    while True:
        # Receive the data
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')
        # Split the data such that you separate the command
        # from the rest of the data.
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
        if command == '1':
            reply = get_tolerance()
            conn.sendall(str.encode(reply))
            data = conn.recv(1024) # receive the data
            data = data.decode('utf-8')
            set_tolerance(str(data))
        elif command == '2':
            reply = datalogs()
            conn.sendall(str.encode(reply))
            reply = " ".join(str(x) for x in avgFreq) # Send array of speed in string form
            conn.sendall(str.encode(reply))
        elif command == '3':
            reply = start()
        elif command == '4':
            reply = stop()
        elif command == '5':
            reply = shutdown()
            print("Our server is shutting down.")
            time.sleep(1)
            s.close()
            break
        else:
            reply = 'Unknown Command'
        # Send the reply back to the client
        conn.sendall(str.encode(reply))
        print("Data has been sent!")
    conn.close()
        

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except Exception as e:
        print(e)
        time.sleep(10)
        s.close()
        break


os.system("clear")

#detect a falling signal




