#!/usr/bin/python3

import sys
import calcoo

class CalculadoraHija(calcoo.Calculadora):


    def mult( self, op1, op2):

        return op1 * op2


    def div(self, op1, op2):
            try:
                return  op1 / op2
            except ZeroDivisionError:
                sys.exit("Division by zero is not allowed.")


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    calcu = CalculadoraHija()

    if sys.argv[2] == "multiplicar":
        result = calcu.mult(operando1,operando2)
    elif sys.argv[2] == "dividir":
        result = calcu.div(operando1, operando2)
    elif sys.argv[2] == "suma":
        result = calcu.sumar(operando1, operando2)
    elif sys.argv[2] == "restar":
        result = calcula.restar(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir')

    print(result)
