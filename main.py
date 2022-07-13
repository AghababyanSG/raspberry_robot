import socket  # for socket
import sys
import time

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    print("socket creation failed with error %s" % (err))

# default port for socket
port = 5000

try:
    host_ip = "192.168.31.205"
except socket.gaierror:

    # this means could not resolve the host
    print("there was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip, port))

print("the socket has successfully connected to xaxaliq")


data = "forward"
s.send(data.encode())
