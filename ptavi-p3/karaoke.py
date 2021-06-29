#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import json
import sys
import smallsmilhandler
from xml.sax import make_parser


class karaokelocal:

    def __init__(self, archivo):
        try:
            archivo = sys.argv[1]
            parser = make_parser()
            smil = smallsmilhandler.SmallSMILHandler()
            parser.setContentHandler(smil)
            parser.parse(open(archivo))
            self.all = smil.get_tags()

        except FlieNotFoundError:
            sys.exit('File not found')

    def __str__(self):
        r = ''
        for frase in self.all:
            for atributo in frase:
                if frase[atributo] != "":
                    r += atributo + "=" + "'" + frase[atributo] + "'" + '\t'
            r += '\n'
        return r


    def to_json(self, smil): #Crea y guarda el fichero json#
        ficherojson = ''     #Inicializa el nombre del fichero#
        if ficherojson == '':  #Si no le damos nombre al fichero mantiene el nombre del smil#
            ficherojson = smil.replace('.smil', '.json') #Cambia la extensión del fichero#

        with open(ficherojson, 'w') as f:  #Abrimos el fichero json en modo write#
            json.dump(self.all, f, indent = 4) #json.dump es una función dentro del json la cual pasa un objeto a formato json#

    def do_local(self):
        for frase in self.all:
            for atributo in frase:
                if atributo == 'src':
                    if frase[atributo].startswith('http://'): #frase[atributo] es un link busca la última / y es direccion
                        direccion = frase[atributo].split('/')[-1]
                        urllib.request.urlretrieve(frase[atributo]) #funcion para descargar archivo que esta en ese directorio de internet#
                        frase[atributo] = direccion

if __name__ == "__main__":
    """
        main program
    """

    try:
        archivo = sys.argv[1]
        karaoke = karaokelocal(archivo)

    except:
        sys.exit('usage error: python3 karaoke.py file.smil')
    print(karaoke)
    karaoke.to_json(archivo)
    karaoke.do_local()
    karaoke.to_json('local.smil')
    print(karaoke)
