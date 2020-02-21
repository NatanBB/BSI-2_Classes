import socket
import psutil

menu = True
while menu:
    serverName='192.241.197.67'
    serverPort=12000

    clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    clientSocket.connect((serverName,serverPort))
    print (clientSocket)
    cpu=psutil.disk_usage('/') #Uso de disco
    # cpu=psutil.cpu_times()
    memoria=psutil.virtual_memory()

    message = (str(cpu)+ " KAKOKARREGADO " +str(memoria))
    print ("\nMensagem enviada: " , message)
    clientSocket.send(bytes(message,"utf-8"))
    modifiedMessage=clientSocket.recv(1024)
    print ('From Server', modifiedMessage.decode('utf-8'))

    clientSocket.close()
