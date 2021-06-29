#!/usr/bin/python3

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):


    def mult(self, op1, op2):

        return op1 * op2


    def div(self, op1, op2):
            try:
                return  op1 / op2
            except ZeroDivisionError:
                sys.exit("Division by zero is not allowed.")

    def operar(self, operador):
        calcoo.Calculadora.operar(self, operador)

        if operador == "multiplicar":
            result = calcuhija.mult(operando1, operando2)
            return result
        elif operador == "dividir":
            result = calcuhija.div(operando1, operando2)
            return result
        else:
            sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir')



if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    calcuhija = CalculadoraHija()
    operador = sys.argv[2]
    solution = calcuhija.operar(operador)

    print(solution)
