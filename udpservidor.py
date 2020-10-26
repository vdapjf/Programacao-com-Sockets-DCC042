from socket import *
import socket

serverName = 'localhost'
serverPort = 12456

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind((serverName,serverPort))

print ('Conexao estabelecida')

while True:

	num1, clientAddress = serverSocket.recvfrom(2048)
	print('Primeiro numero recebido:', num1.decode())

	num2, clientAddress = serverSocket.recvfrom(2048)
	print('Segundo numero recebido:', num2.decode())

	operador, clientAddress = serverSocket.recvfrom(2048)
	print('Operador recebido:', operador.decode())

	print('Calculando...')

	if str(operador.decode()) == '+':
		resp = int(num1.decode()) + int(num2.decode())
		resp = str(resp)
		serverSocket.sendto(resp.encode(),clientAddress)
		break
	elif str(operador.decode()) == '-':
		resp = int(num1.decode()) - int(num2.decode())
		resp = str(resp)
		serverSocket.sendto(resp.encode(),clientAddress)
		break
	elif str(operador.decode()) == '/':
		resp = int(num1.decode()) / int(num2.decode())
		resp = str(resp)
		serverSocket.sendto(resp.encode(),clientAddress)
		break
	elif str(operador.decode()) == '*':
		resp = int(num1.decode()) * int(num2.decode())
		resp = str(resp)
		serverSocket.sendto(resp.encode(),clientAddress)
		break

serverSocket.close()
print("Conexao finalizada")

