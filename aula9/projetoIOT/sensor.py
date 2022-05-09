#!/usr/bin/env python3
import socket
import sys

ESTADO = 'OFF'

def interpretaComando(comando, mySocket):
    global ESTADO
    comando = comando.removesuffix('\n')
    print('Recebi o comando', comando.encode())
    if comando.lower() == 'ligar':
        ESTADO = 'ON'
    elif comando.lower() == 'desligar':
        ESTADO = 'OFF'
    elif comando.lower() == 'consulta':
        #print('esqueci de fazer o exercicio 3A')
        string='Estado do sensor ID: '+ESTADO
        mySocket.send(string.encode())
    else:
        print('comando desconhecido: ', comando)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP= input('IP do monitor: ')
PORTA= int(input('Porta do monitor: '))
ID = input('ID do sensor: ')

try:
    s.connect((IP, PORTA))
    #Envia o identificador
    s.send(ID.encode())
except:
    print('erro de conexao')

while True:
    try:
        dados = s.recv(100).decode()
        #print('Esqueci de fazer o exercicio 3B')
        interpretaComando(dados,s)        
    except:
        print('Erro na conexão com o monitor')
        sys.exit()