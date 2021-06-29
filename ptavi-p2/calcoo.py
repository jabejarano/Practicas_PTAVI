#!/usr/bin/python3

import sys

class Calculadora():

    def sumar(self,op1, op2):
        return op1 + op2


    def restar(self,op1, op2):
        return op1 - op2


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calcu = Calculadora()

    if sys.argv[2] == "suma":
        result = calcu.sumar(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = calcu.restar(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
