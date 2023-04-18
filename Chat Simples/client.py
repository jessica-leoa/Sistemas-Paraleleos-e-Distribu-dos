import socket
import threading

# Configurações do cliente
HOST = 'localhost'
PORT = 5000

# Criando o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
client_socket.connect((HOST, PORT))

def send_message():
    while True:
        # Obtendo a mensagem digitada pelo usuário
        message = ()

        # Enviando a mensagem para o servidor
        client_socket.sendall(message.encode())

def receive_messages():
    while True:
        # Recebe a mensagem do servidor
        message = client_socket.recv(1024).decode()

        # Exibe a mensagem na tela
        print(message)

# Cria threads para enviar e receber mensagens
threading.Thread(target=send_message).start()
threading.Thread(target=receive_messages).start()
