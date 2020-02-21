import socket

serverPort=12000

serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print ('O servidor está ligado')

while 1:
	connectionSocket,addr=serverSocket.accept()
	message=connectionSocket.recv(1024)
	arquivo=open('arquivo','a')
	arquivo.write("Cliente: "+str(addr)+ " ; "+str(message.decode('utf-8'))+"\n\n")
	modifiedMessage=("Gravado com sucesso!")
	connectionSocket.send(bytes(modifiedMessage,"utf-8"))
	print (addr)
	print (modifiedMessage)
	arquivo.close()
	connectionSocket.close()