#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""
import sys
import socket

# Constantes. Dirección IP del servidor y contenido a enviar
try:
    server = sys.argv[1]
    port = int(sys.argv[2])
    peticion = sys.argv[3]
    address = sys.argv[4]
    expires = sys.argv[5]
except IndexError:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")
# ["hola", "pepe", "es", "lunes"]
# "hola pepe es lunes"

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((server, port))
    print("Enviando:", peticion.upper() + ' sip:' + address + ' SIP/2.0')
    print("Expires: " + expires)
    #Enviamos al servidor nuestra peticion
    my_socket.send(bytes(peticion.upper() + ' sip:' + address + ' SIP/2.0\r\n '
                         + expires,'utf-8') + b'\r\n\r\n')

    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
