from lesson36.server_1 import Socket
from threading import Thread


class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()
        self.bind(('127.0.0.1', 1234))
        self.listen()
        print('серввер слушает')

        self.users = []

    def set_up(self):
        self.accept_sockets()


    def send_data(self, data):
        if len(self.users) > 0:
            for user in self.users:
                try:
                    user.send(data)
                except:
                    self.users.pop(user)

    def listen_socket(self, lisen_socket=None):
        print('слушаю клиентов')
        while True:
            data = lisen_socket.recv(2048)
            print(f'User send {data}')
            self.send_data(data)

    def accept_sockets(self):
        while True:
            user_soket, address = self.accept()
            print(f'User{address[0]}, connected')
            self.users.append(user_soket)
            listen_accepted_user = Thread(
                target=self.listen_socket,
                args=(user_soket,), daemon=True
            ).start()


if __name__ == '__main__':
    server = Server()
    server.set_up()

