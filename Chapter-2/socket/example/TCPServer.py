from socket import *

serverPort = 12030
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
# 开始聆听请求, 最大为1
serverSocket.listen(1)
print("The server is ready to recive")
while True:
    # 当客户端请求连接时, 接收并分配一个专用的新的socket
    connectionSocket, addr = serverSocket.accept()
    # 此后都是新的socket与用户相互发送数据
    sentenct = connectionSocket.recv(1024).decode()
    capitalizedSentece = sentenct.upper()
    connectionSocket.send(capitalizedSentece.encode())
    connectionSocket.close

