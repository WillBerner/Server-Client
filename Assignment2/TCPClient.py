import sys
from socket import *

for line in sys.stdin:
    if len(line) == 0: break


    clientSocket = socket(AF_INET, SOCK_STREAM)
    hostPort = 15132
    host_name = "comp431bfa19"

    clientSocket.connect((host_name, hostPort))

    stream = clientSocket.makefile('rw')

    # write the input line to the server
    stream.write(line)
    stream.flush()

    # read the response lines from the server
    numberOfLines = stream.readline()

    for line in range(int(numberOfLines)):
        response = stream.readline()
        sys.stdout.write(response)
    
    
    # close connection  $
    clientSocket.close()

sys.exit()
