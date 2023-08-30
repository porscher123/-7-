

客户端

```python
from socket import *
import sys
import time
clientSocket = socket(AF_INET, SOCK_DGRAM)
# 设置socket的超时时间, 到时间会抛异常
clientSocket.settimeout(1)
if __name__ == '__main__':
    server_host = sys.argv[1]
    print(server_host)
    for i in range(1, 11):
        t1 = time.perf_counter()
        clientSocket.sendto("ping".encode(), (server_host, 12000))
        success = False
        # 定时
        while time.perf_counter() - t1 <= 1:
            message, serverAddress = clientSocket.recvfrom(2048)
            if (message != ""):
                RTT = time.perf_counter() - t1
                print("Ping " + str(i) + "  " + format(RTT, '.3f')  + "s")
                success = True
                break
        if success == False:
            print("Request timed out\n")
clientSocket.close()
```

验证

```
$ python3 UDPPingClient.py 172.20.10.7
```

```
Ping 1  0.003s
Ping 2  0.002s
Ping 3  0.002s
Ping 4  0.002s
Traceback (most recent call last):
  File "UDPPingClient.py", line 14, in <module>
    message, serverAddress = clientSocket.recvfrom(2048)
socket.timeout: timed out
```



