#!/usr/bin/python3

import sys

class Calculadora():

    def sumar(self, op1, op2):

        return op1 + op2


    def restar(self, op1, op2):

        return op1 - op2

    def operar(self, operador):
            if operador == "suma":
                result = calcu.sumar(operando1, operando2)
                return result
            elif operador == "resta":
                result = calcu.restar(operando1, operando2)
                return result
            else:
                return none

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    calcu = Calculadora()
    operador = sys.argv[2]
    solution = calcu.operar(operador)
    if not solution:
         sys.exit('Operación sólo puede ser sumar o restar.')

    print(solution)
