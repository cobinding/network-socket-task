from socket import *

# serverName, serverPort: 내가 접속할 ip, port

serverName = ''
serverPort = 15000
clientSocket = socket(AF_INET,SOCK_DGRAM)

m = input('Input lowercase sentence:')

clientSocket.sendto(m.encode(),(serverName, serverPort))
print('전송 완료')
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()