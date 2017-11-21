#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import sys
import socket


USAGE = 'python3 client.py method receiver@IP:SIPport'

try:
    SERVER = sys.argv[2].split('@')[1]
    PORT = int(SERVER.split(':')[1])
    METHOD = sys.argv[1]
    IP = SERVER.split(':')[0]
    NICK = sys.argv[2].split('@')[0]
    LINE = METHOD + ' sip:' + NICK + '@' + IP + ' SIP/2.0\r\n'
except IndexError:
    sys.exit('Usage: ' + USAGE)

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((IP, PORT))

    print(LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    
    print(data.decode('utf-8'))
    print("Terminando socket...")

print("Fin.")
