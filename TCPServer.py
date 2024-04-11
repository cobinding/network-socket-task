from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print("받은 sentence : ", sentence)
    
    capitalizedSentence = sentence.upper()
    print("보낼 sentense : ", capitalizedSentence)
    
    connectionSocket.send(capitalizedSentence)
    print("보내기")
    
    connectionSocket.close()
    print("닫기")
    