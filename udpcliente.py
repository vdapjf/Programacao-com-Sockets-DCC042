from socket import * 
import socket

serverName = 'localhost'
serverPort = 12456
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Servidor objetivo: ', serverName)
print('Port:', serverPort)
print('\n')


num1 = input ('Digite o primeiro numero: ')
num2 = input ('Digite o segundo numero: ')
operador = input ('Selecione um operador (+ / * -): ')

clientSocket.sendto(num1.encode(),(serverName,serverPort))
clientSocket.sendto(num2.encode(),(serverName,serverPort))
clientSocket.sendto(operador.encode(),(serverName,serverPort))

resp,serverAddress = clientSocket.recvfrom(2048)

print('Resultado: ', resp.decode())

clientSocket.close()
print('Conexao encerrada')

