import socket
import threading

# Configurações do servidor
HOST = 'localhost'
PORT = 5000

# Cria o socket do servidor (Aqui indica q o soquete será usado para comunicacao TCP/IP sobre IPv4)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vinculando o socket do servidor ao endereço e porta especificada
server_socket.bind((HOST, PORT))

# fazendo a conexões
server_socket.listen()

# Lista de clientes conectados
clients = []

def handle_client(client_socket, client_address):
    # Adiciona o novo cliente à lista
    clients.append(client_socket)

    while True:
        try:
            # Recebe a mensagem do cliente
            message = client_socket.recv(1024).decode()

            if not message:
                # Se a mensagem estiver vazia, remove o cliente da lista
                clients.remove(client_socket)
                break

            # Envia a mensagem para todos os clientes conectados, exceto o remetente
            for c in clients:
                if c != client_socket:
                    c.sendall(message.encode())

        except:
            # Se ocorrer um erro, remove o cliente da lista
            clients.remove(client_socket)
            break

    # Fecha o socket do cliente
    client_socket.close()

while True:
    # Aceita conexões de clientes
    client_socket, client_address = server_socket.accept()

    # Cria uma thread para lidar com o cliente
    threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
