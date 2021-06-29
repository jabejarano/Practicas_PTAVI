#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
# Cliente UDP simple.
# Dirección IP del servidor.
try:
    METODO = sys.argv[1]
    ADDRESS = sys.argv[2].split(':')[0]
    SERVER = ADDRESS.split('@')[1]
    PORT = int(sys.argv[2].split(':')[1])
except IndexError:
    sys.exit("Usage: client.py ip puerto register sip_ADDRESS expires_value")

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((SERVER, PORT))

    print("Enviando: " + METODO.upper() + ' sip:' + ADDRESS + ' SIP/2.0')
    my_socket.send(bytes(METODO.upper() + ' sip:' + ADDRESS + ' SIP/2.0',
                         'utf-8') + b'\r\n\r\n')
    try:
        data = my_socket.recv(1024)
    except ConnectionRefusedError:
        sys.exit("Error en la conexion")
    recb = data.decode('utf-8').split()
    print('Recibido -- ', data.decode('utf-8'))
    print(recb)
    if METODO == "INVITE":
        if recb[2] == "Trying" and recb[5] == "Ringing" and recb[8] == "OK":
            my_socket.send(bytes("ACK sip:" + ADDRESS + " SIP/2.0", "utf-8")
                           + b"\r\n\r\n")
    if METODO == "BYE":
        if data.decode('utf-8') == "SIP/2.0 200 OK\r\n\r\n":
                print("terminando socket...")
print("Fin.")
