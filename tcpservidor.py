from socket import * 
import socket 

serverName = "localhost"
serverPort = 3030

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serverSocket.bind((serverName, serverPort)) 
serverSocket.listen(1)

print('Aguardando cliente')
conexao, address = serverSocket.accept()

while True:

    print('Servidor:') 
    mensagem = input("")
    print('\n')
    if mensagem == 'Sair':
        conexao.send('Adeus'.encode())
        break

    conexao.send(mensagem.encode())

    mensagemCliente = conexao.recv(2048)
    print('Cliente:')
    print(mensagemCliente.decode())
    print('\n')
    if mensagemCliente.decode() == 'Adeus':
        break
    
serverSocket.close()
print('Conexao finalizada')


