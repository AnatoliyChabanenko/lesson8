
from lesson30.lesson30_3 import caesar
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 65432)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(1024).decode()

            data = caesar(int(data[-1::]), data[:-1])
            print(f'{data}')
            if data:
                connection.sendall(data.encode())
            else:
                print('no data from', client_address)
                break

    finally:
        connection.close()