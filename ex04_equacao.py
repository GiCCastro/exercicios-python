"""
4) Considerando a expressão: AX + BX + C = 1 .Faça um algoritmo que receba 3 valores
inteiros A, B, e C e calcule o valor de X. Dados os valores caso A e B possuam valor 0 e
C seja diferente de 1 imprimir “solução impossível”.
"""


def valor_x(a, b, c):

  if a+b == 0:
    return "solução impossível"

  return f"O valor de X nesta equação é {(1-c)/(a+b)}"


print(valor_x(1, 1, -1))
