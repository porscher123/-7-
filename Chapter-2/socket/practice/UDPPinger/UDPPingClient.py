from socket import *
import sys
import time
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
if __name__ == '__main__':
    server_host = sys.argv[1]
    print(server_host)
    for i in range(1, 11):
        t1 = time.perf_counter()
        clientSocket.sendto("ping".encode(), (server_host, 12000))
        success = False
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