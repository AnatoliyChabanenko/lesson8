import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    slovo = input(f'введите слово:' )
    chislo = input(f'введите число на сколько сдвинуть 0-10:' )
    s.send(slovo.encode())
    s.send(chislo.encode())
    data = s.recv(1024)

print(f'заодированое слово {data}' )
