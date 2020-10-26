from socket import * 
import socket  
  
serverName = "localhost"
serverPort = 3030

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
clientSocket.connect((serverName, serverPort)) 
print('Conectado ao chat' + serverName + 'com port', serverPort)
print('Aguarde a mensagem do servidor')
print('Digite \'Sair\' quando quiser encerrar a conexao')

while True: 
  
    mensagemServidor = clientSocket.recv(2048)
    print('Servidor:')
    print(mensagemServidor.decode())
    print('\n')
    if mensagemServidor.decode() == 'Adeus':
        break

    print('Cliente:') 
    mensagem = input("")
    if mensagem == 'Sair':
        clientSocket.send('Adeus'.encode())
        break
    print('\n')
    clientSocket.send(mensagem.encode()) 

clientSocket.close() 
print('Conexao encerrada')

