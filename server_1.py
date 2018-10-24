import socket
import prac7

host = ''
port = 5560

storedValue = "You are connected to the raspberry pi"

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

def tolerance():
    reply = "State new tolerance value: "
    prac7.set_tolerance()
    return reply

def datalogs():
    reply = "Printing the average frequency of the of the wave after every 10 waves: "
    prac7.printFreq()
    
    return reply

def start():
    reply = "Starting application"
    prac7.main()
    
    return reply

def stop():
    reply = "Stopping application"
    prac
    return reply

def shutdown():
    reply = "Shutting down"

def dataTransfer(conn):
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
            reply = tolerance()
            conn.sendall(str.encode(reply))
            data = conn.recv(1024) # receive the data
            data = data.decode('utf-8')
        elif command == '2':
            reply = datalogs()
        elif command == '3':
            reply = start()
        elif command == '4':
            reply = stop()
        elif command == '5':
            reply = shutdown()
            print("Our server is shutting down.")
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
    except:
        break
