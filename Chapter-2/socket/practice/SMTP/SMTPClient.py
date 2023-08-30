from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.163.com'


# Create socket called clientSocket and establish 
#   a TCP connection with mailserver
#Fill in start 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO m18143664811@163.com\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
 

def getMailFrom(source):
    return "MAIL FROM: <" + source +">\r\n"
def getRcptTo(target):
    return "RCPT TO: <" + target + ">\r\n"

login = "auth login\r\n"
clientSocket.send(login.encode())
res = clientSocket.recv(1024).decode()
print(res)

user = "MTgxNDM2NjQ4MTFAMTYzLmNvbQ==\r\n"
clientSocket.send(user.encode())
res = clientSocket.recv(1024).decode()
print(res)

pwd = "TFRMWUxaUldUTk1TRlRCUA==\r\n"
clientSocket.send(pwd.encode())
res = clientSocket.recv(1024).decode()
print(res)

# Send MAIL FROM command and print server response.
# Fill in start
local = getMailFrom("m18143664811@163.com")
clientSocket.send(local.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
# Fill in end
# Send RCPT TO command and print server response. 
# Fill in start
friend = getRcptTo("2415571314@qq.com")
clientSocket.send(friend.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
# Fill in end
# Send DATA command and print server response. 
# Fill in start
cmd = "DATA\r\n"
clientSocket.send(cmd.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
# Fill in end
# Send message data.
# Fill in start
from_user = 'from: <18143664811@163.com>\r\n'
to_user = 'to: <2415571314@qq.com>\r\n'
subject = 'subject: test\r\n'
clientSocket.send(from_user.encode())
clientSocket.send(to_user.encode())
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())
# Fill in end
# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
# Fill in end
# Send QUIT command and get server response.
# Fill in start
clientSocket.send("QUIT".encode())
recv = clientSocket.recv(1024).decode()
print(recv)
# Fill in end
