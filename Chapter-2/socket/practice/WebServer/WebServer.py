#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverPort = 12001
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end
def responseHeader(text):
    respHeader = '''HTTP/1.1 200 OK 
Connection: keep-alive
Content-Length: ''' + str(len(text.encode('utf-8'))) + '\nContent-Type:text/html\n\n'
    return respHeader
while True:
    #Establish the connection
    print('Ready to serve...')
    # connectionSocket, addr = #Fill in start #Fill in end
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(2048).decode()
        if (message == ""):
            continue
        print(message)
        filename = message.split()[1]
        print("filename = " + filename)
        f = open(filename[1:])
        outputdata = f.read()
        print(outputdata)
        #! Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send(responseHeader(outputdata).encode('utf-8'))
        #Fill in end
        connectionSocket.send(outputdata.encode())
        print("ok")
        connectionSocket.close()
    except IOError:
        #! Send response message for file not found
        #Fill in start
        fnf = "HTTP/1.1 404 Not Found \r\n\r\n";
        html = "<html><head><title> 404 Not Found 1</title></head><body><h1>404 Error</h1><p> The page you requested was not found</p></body></html>\r\n"
        connectionSocket.send(fnf.encode())
        connectionSocket.send(html.encode())
        #Fill in end

        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data