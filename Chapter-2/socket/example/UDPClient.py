from socket import *


# 设置服务器的ip和端口号
serverName = '172.20.10.7'
serverPort = 12000
# 创建客户端的socket, 分别指示ipv4和UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 设置要发送的报文
message = input("Input lowercase sentece:")
# 将报文从字符串编码为字节, 并发送到目的地址
clientSocket.sendto(message.encode(), (serverName, serverPort))
# 接收, 2048是缓存长度
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# 解码为字符串并打印
print(modifiedMessage.decode())
# 关闭socket
clientSocket.close()

