"""
-------------------------------
    CLIENT UDP
-------------------------------
"""
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip = '10.150.10.137'
porta = 9999
while True:
    if ('' == ip):
        ip = input('Digite o IP: ')
    if ('' == porta):
        porta = int(input('Digite a porta de destino: '))
    msg = input('Digite a mensagem a ser transmitida: ')
    s.sendto(msg.encode(), (ip,porta))
