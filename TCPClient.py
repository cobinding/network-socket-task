from socket import *

# serverName, serverPort: 내가 접속할 ip, port
#뭔소리얌
serverName = ''
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