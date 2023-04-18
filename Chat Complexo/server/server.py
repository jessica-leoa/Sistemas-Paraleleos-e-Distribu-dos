import threading
import socket

class Server:
    def __init__(self):
        self.users = []
        self.channels = {}
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('localhost', 8080))
        self.socket.listen(5)

    def start(self):
        while True:
            conn, addr = self.socket.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()

    def handle_client(self, conn, addr):
        print(f"Nova conexão estabelecida: {addr}")
        authenticated_user = None
        current_channel = None
        
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    break
                print(f"Mensagem recebida de {addr}: {data}")
                args = data.split()
                command = args[0]
                
                # Verifica se o usuário está autenticado
                if authenticated_user is None:
                    if command == "register":
                        username, password = args[1], args[2]
                        self.register_user(username, password)
                    elif command == "login":
                        username, password = args[1], args[2]
                        authenticated_user = self.authenticate_user(username, password)
                        if authenticated_user is not None:
                            conn.send(f"Bem-vindo, {authenticated_user['username']}!".encode())
                        else:
                            conn.send("Nome de usuário ou senha incorretos".encode())
                    else:
                        conn.send("Você precisa se autenticar para usar o chat".encode())
                else:
                    if command == "create":
                        channel_name = args[1]
                        self.create_channel(channel_name)
                    elif command == "join":
                        channel_name = args[1]
                        current_channel = self.join_channel(channel_name, authenticated_user)
                        if current_channel is not None:
                            conn.send(f"Bem-vindo ao canal {current_channel['name']}!".encode())
                        else:
                            conn.send(f"Você já está no canal {channel_name}".encode())
                    elif command == "leave":
                        if current_channel is not None:
                            self.leave_channel(current_channel['name'], authenticated_user)
                            conn.send(f"Você saiu do canal {current_channel['name']}!".encode())
                            current_channel = None
                        else:
                            conn.send("Você não está em nenhum canal no momento".encode())
                    elif command == "send":
                        if current_channel is not None:
                            message = " ".join(args[1:])
                            self.send_message(current_channel['name'], authenticated_user, message)
                        else:
                            conn.send("Você precisa entrar em um canal para enviar mensagens".encode())
                    elif command == "list":
                        channel_list = ", ".join(self.channels.keys())
                        conn.send(f"Canais disponíveis: {channel_list}".encode())
                    elif command == "exit":
                        conn.send("Desconectando...".encode())
                        break
                    else:
                        conn.send("Comando inválido".encode())
            except Exception as e:
                print(f"Erro ao lidar com a conexão de {addr}: {e}")
                break

        conn.close()
        print(f"Conexão encerrada: {addr}")
        
# -------------------------------------------------------------------------------------------------------------------------------------------------        

    def register_user(self, username, password):
        pass # implementar

    def authenticate_user(self, username, password):
        pass # implementar

    def create_channel(self, channel_name):
        pass # implementar

    def join_channel(self, channel_name, user):
        pass # implementar

    def leave_channel(self, channel_name, user):
        pass # implementar

if __name__ == "__main__":
    server = Server()
    server.start()
