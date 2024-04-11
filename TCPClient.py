from socket import *
# 민서 ip : 175.213.35.145
# 형섭 ip : 192.168.75.91

serverName = '192.168.75.91'
serverPort = 15000
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentence:')

clientSocket.send(sentence.encode())
print('send')
modifiedSentence = clientSocket.recv(1024)
print('받기')
print ('From Server:', modifiedSentence.decode())
clientSocket.close()