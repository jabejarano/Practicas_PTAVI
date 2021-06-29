#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija





if __name__ == "__main__": # Main, Aqui empieza el programa a leer.

    calc = calcoohija.CalculadoraHija()
    f = open(sys.argv[1], "r")
    fichero = f.readlines()

    for line in fichero:
        cadena = line.split(",") #Separar con "," todos los elementos de la linea
        print(cadena)
