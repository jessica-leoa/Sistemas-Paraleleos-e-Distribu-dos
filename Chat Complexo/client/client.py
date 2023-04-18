import threading
import socket

class Client:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.channels = []
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def connect(self, host, port):
        self.socket.connect((host, port))
        self.connected = True

    def send_message(self, channel_name, message):
        pass # implementar

    def join_channel(self, channel_name):
        pass # implementar

    def leave_channel(self, channel_name):
        pass # implementar

    def logout(self):
        pass # implementar

    def receive_messages(self):
        pass # implementar

if __name__ == "__main__":
    username = input("Digite seu nome de usuário: ")
    password = input("Digite sua senha: ")
    client = Client(username, password)
    client.connect("localhost", 8080)
