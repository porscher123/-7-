from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
# 开始聆听请求, 最大为1
serverSocket.listen(1)
print("The server is ready to recive")
# 当客户端请求连接时, 接收并分配一个专用的新的socket
while True:
    connectionSocket, addr = serverSocket.accept()
    # 此后都是新的socket与用户相互发送数据
    sentenct = connectionSocket.recv(10240)
    print('From Server:', sentenct, '\n')
    connectionSocket.close()

