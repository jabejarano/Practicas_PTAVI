#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""
 # módulo en Python que simplifica la tarea de implementar servicios en Internet
import socketserver
import sys
import time
import json


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    dicc = {}


    def register2json(self):
        """
        Escribir diccionario.
        En formato json en elfichero registered.json.
        """
        with open('registered.json', 'w') as jsonfile:
            json.dump(self.dicc, jsonfile, indent=4)



    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        linea = ''
        for line in self.rfile:
            linea += line.decode('utf-8')
        if linea != '\r\n':
            print("El cliente nos manda ", linea)
            (peticion, address, sip, expires) = linea.split()
            if peticion == 'REGISTER':
                IP = self.client_address[0]
                # Me quedo con el segundo objeto (derecha de ':')
                user = address.split(':')[1]
                # Tiempo de ahora mas el que tarda en darte de baja
                Time = time.time() + int(expires)
                # Convierto a Horas minutos segundos
                TimeExp = time.strftime('%Y-%m-%d %H:%M:%S',
                                        time.gmtime(Time))

                ahora = time.strftime('%Y-%m-%d %H:%M:%S',
                                        time.gmtime(time.time()))
                self.dicc[user] = {'address': IP, 'expires': TimeExp}
                userDelete = []
                for user in self.dicc:
                    if ahora >= self.dicc[user]['expires']:
                        userDelete.append(user)
                for user in userDelete:
                    del self.dicc[user]
                self.register2json()
                print(self.dicc)

if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the EchoHandler class to manage the request
    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)

    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
