from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("The server is ready to receive.")

while 1:
    print('전송 연결')
    message, clientAddress = serverSocket.recvfrom(2048)
    print('받은 내용', message, clientAddress)
    modifiedMessage = message.upper()
    print('전송')
    serverSocket.sendto(modifiedMessage, clientAddress)
    print('전송 완료')