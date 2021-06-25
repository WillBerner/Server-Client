import sys
from socket import *
import re

# Global parsing variables
inArray = ""
url = ""
request_URL = ""

# Setting up socket connection
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 15132
serverSocket.bind(("", serverPort))

# Listen for up to one connection at once
serverSocket.listen(1)

# Listen to input
while True:
    print('The server is ready to recieve')

    connectionSocket, addr = serverSocket.accept()
    stream = connectionSocket.makefile('rw')

    # read in input line
    message = stream.readline()
    writtenLines = 1
    answerString = ""

    ####################################################

    # Split input by spaces and get url and http
    try:
        inArray = re.split(r'\s', message)
        
        # Get different parts of the request
        url = inArray[1]
        httpVersion = inArray[2]
        getRequest = message[:4]
        request_URL = url
        url = re.split("\/", url)
        del inArray[-1]

    except:
        answerString += "ERROR -- Invalid Method token.\n"
        writtenLines+=1
        break


    if getRequest != "GET ":
        answerString += "ERROR -- Invalid Method token.\n"
        writtenLines+=1

    if httpVersion[:5] != "HTTP/":
        answerString += "ERROR -- Invalid HTTP-Version token.\n"
        writtenLines+=1



    returnMessage = message
    stream.write(str(writtenLines) + "\n")
    stream.write(returnMessage)
    stream.write(answerString)
  
    stream.flush()

    connectionSocket.close()

serverSocket.close()
sys.exit()
