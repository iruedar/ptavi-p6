#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import sys
import socketserver


USAGE = 'python3 server.py IP port audio_file'

try:
    IP = sys.argv[1]
    LISTEN_PORT = int(sys.argv[2])
    FILE = sys.argv[3]
except IndexError:
    sys.exit('usage: ' + USAGE)

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            if len(line) == 0:
                break

            METHOD = line.decode('utf-8').split(' ')[0]
            if METHOD == 'INVITE':
                self.wfile.write(b'SIP/2.0 100 Trying\r\n')
                self.wfile.write(b'SIP/2.0 180 Ringing\r\n')
                self.wfile.write(b'SIP/2.0 200 OK\r\n')
                print(METHOD + ' recieved')
            elif METHOD == 'BYE':
                self.wfile.write(b'SIP/2.0 200 OK\r\n')
                print(METHOD + ' recieved')


if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer((IP, LISTEN_PORT), EchoHandler)
    print("Listening...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print('servidor finalizado')
