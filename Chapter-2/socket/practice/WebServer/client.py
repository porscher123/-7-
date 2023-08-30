from socket import *
import sys

def getRequestHeader(filename, server_host):
    url = 'GET ' + filename + ' HTTP/1.1\nHost: ' + str(server_host) 
    return url
if __name__ == '__main__':
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((server_host, server_port))
    httpRequest = getRequestHeader(filename, server_host)
    clientSocket.send(httpRequest.encode())
    httpResponse = clientSocket.recv(2048)
    print(httpResponse.decode())
    clientSocket.close()
