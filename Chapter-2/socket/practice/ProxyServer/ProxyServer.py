from socket import *
import sys
if len(sys.argv) <= 1:
    print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
serverPort = 8888
serverIP = sys.argv[1]
tcpSerSock.bind(('', serverPort))
tcpSerSock.listen(1)
# Fill in end.
while 1:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    # message = # Fill in start. # Fill in end.
    message = tcpCliSock.recv(1024).decode()
    print("message: " + message)
    # Extract the filename from the given message
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print("filename: " + filename)
    fileExist = "false"
    filetouse = "/" + filename
    print("filetouse: " + filetouse)
    try:
        # Check wether the file exist in the cache
        f = open(filetouse[1:], "r") 
        outputdata = f.read() 
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.0 200 OK\r\n") 
        tcpCliSock.send("Content-Type:text/html\r\n")
        # Fill in start.
        tcpCliSock.send("Content-Length: " + len(outputdata) + "\r\n")
        tcpCliSock.send(outputdata + "\r\n")
        # Fill in end.
        print('Read from cache') 
    # Error handling for file not found in cache
    except IOError:
        if fileExist == "false": 
            # Create a socket on the proxyserver
            # c = # Fill in start. # Fill in end.
            c = socket(AF_INET, SOCK_STREAM)
            
            hostn = filename.replace("www.","",1) 
            print("hostn: " + hostn) 
            try:
                print("-----1-------------------")
                # Connect to the socket to port 80
                # Fill in start.
                c.connect((hostn, 80))
                print("-----2-------------------")

                # Fill in end.
                # Create a temporary file on this socket and 
                #   ask port 80 for the file requested by the client
                fileobj = c.makefile('r', 0) 
                print("-----3-------------------")
                

                fileobj.write("GET "+"http://" + filename + " HTTP/1.0\n\n") 
                print("ok------------------")
                # Read the response into buffer
                # Fill in start.
                fileobj.write(c.recv(1024).decode())
                print("fileobj: " + fileobj)
                # Fill in end.
                # Create a new file in the cache for the requested file. 
                # Also send the response in the buffer to client socket
                #    and the corresponding file in the cache
                tmpFile = open("./" + filename,"wb") 
                # Fill in start.
                tmpFile.write(fileobj)
                tcpCliSock.send(fileobj.encode())
                # Fill in end.
            except: 
                print("Illegal request") 
        else:
            pass
            # HTTP response message for file not found
            # Fill in start.
            fnf = "HTTP/1.1 404 Not Found \r\n\r\n";
            html = "<html><head><title> 404 Not Found 1</title></head><body><h1>404 Error</h1><p> The page you requested was not found</p></body></html>\r\n"
            tcpSerSock.send(fnf.encode())
            tcpSerSock.send(html.encode())
            # Fill in end.
    # Close the client and the server sockets 
    tcpCliSock.close() 
# Fill in start.
tcpSerSock.close()
# Fill in end

# http://192.168.118.128:8888/www.oj.daimayuan.top/courses
# 192.168.118.128