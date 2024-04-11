from socket import *

# 민서 ip : 175.213.35.145
# 형섭 ip : 192.168.75.101

serverName = '175.213.35.145'
serverPort = 15000
clientSocket = socket(AF_INET,SOCK_DGRAM)

m = input('Input lowercase sentence:')

clientSocket.sendto(m.encode(),(serverName, serverPort))
print('전송 완료')
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()