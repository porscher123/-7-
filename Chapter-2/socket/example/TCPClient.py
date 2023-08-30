from socket import *

serverName = '128.0.0.9'
serverPort = 12000
# SOCK_STREAM表明是TCP连接, 创建客户端socket时不用指定port, 因为os自动帮我们分配prot
clientSocket = socket(AF_INET, SOCK_STREAM)
# 与服务器端建立TCP连接, 3次握手
clientSocket.connect((serverName, serverPort))
message = input("Input lowercase sentece:")
# 发送编码后的分组, 不用传目的地址
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(2048)
print("From Server : ", modifiedMessage.decode())
clientSocket.close()


