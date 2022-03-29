import socket
import sys
HOST='127.0.0.1'
PORT=9999

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST,PORT))
except:
    print('ERRO DE BIND')
    sys.exit()

s.listen(5)

while True:
    print(f'aguardando conexões em : {PORT}')
    conn, addr = s.accept()
    print(f'recebi uma conexao de: {addr}')
    while True:
        data = conn.recv(1024)
        print(f'recebi {len(data)} bytes')
        if not data:
            break
        print(data)

print(f'o cliente encerrou')
conn.close()
