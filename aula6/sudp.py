import socket
import sys

porta = int(input('Digite a porta em que sera hospedado: '))

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

try:
    s.bind(('',porta))
except:
    print('Erro de bind.')
    sys.exit()

while True:
    input('Aperte [Enter] para continuar...')
    data,addr = s.recvfrom(1024)
    print(f'o IP: ({addr}) enviou a mensagem: "{data}"')

print('O servidor encerrou')
s.close()