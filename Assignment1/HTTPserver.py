# Will Berner
# © 2019

import sys
import re

inArray = ""
url = ""
request_URL = ""

# 0
# General program sequence delimited by numbers

# 3
# Using regular expressions to check if a url is valid
def checkURL():

    # Check for absolute path
    if (request_URL[0] != "/"):
        print("ERROR -- Invalid Absolute-Path token.")
        return
    
    del url[0]
    for i in range(len(url)):
        if re.match(r'^[A-Za-z0-9_.]+$', url[i]) == None:
            print("ERROR -- Invalid Absolute-Path token.")
            return

    
    # 4
    if len(inArray) <= 4:
    # A valid request was sent - try to respond
        goodRequest()
    else:
        print("ERROR -- Spurious token before CRLF.")
    return

# 5
# A good request was recieved
def goodRequest():
    print("Method = GET")
    print("Request-URL = " + request_URL)
    print("HTTP-Version = " + httpVersion)
    openFile()
    return

# 6
# Try to open the requested file
def openFile():
    if url[-1][-4:] == ".txt" or url[-1][-4:] == ".htm" or url[-1][-5:] == ".html" or url[-1][-4:] == ".TXT" or url[-1][-4:] == ".HTM" or url[-1][-5:] == ".HTML":
        
        # Acceptable file type: try to read in the file
        try:
            with open(url[-1]) as filePath:
                currentline = filePath.readline()
                print(currentline, end = '')
                while currentline:
                    currentline = filePath.readline()
                    print(currentline, end = '')
        except:
            print("404 Not Found: " + request_URL)
    else:
        print("501 Not Implemented: " + request_URL)
    return

# 1
# Looping over an input file
for line in sys.stdin:

    # Split input by spaces and get url and http
    try:
        inArray = re.split(r'\s', line)
        url = inArray[1]
        httpVersion = inArray[2]
        getRequest = line[:4]
        request_URL = url
        url = re.split("\/", url)
        del inArray[-1]
    except:
        print("ERROR -- Invalid Method token.")
        break

    print(line, end = '')
   
################################################

    # Check GET token
    if getRequest != "GET ":
        print("ERROR -- Invalid Method token.")
    
    else:
        
        # 2
        # Check HTTP version
        if httpVersion[:5] == "HTTP/":
            if httpVersion[6:7] == "." and (len(httpVersion) < 9):

                # Check if HTTP has numbers
                firstNum = u"" + httpVersion[5:6]
                secondNum = u"" + httpVersion[7:8]
                if firstNum.isnumeric() and secondNum.isnumeric():
                
                    # HTTP Version is acceptable
                    checkURL()
                    
                else:
                    print("ERROR -- Invalid HTTP-Version token.")
            else:
                print("ERROR -- Invalid HTTP-Version token.")
        else:
            print("ERROR -- Invalid HTTP-Version token.")