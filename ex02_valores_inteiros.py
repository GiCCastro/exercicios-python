"""
2) Faça um algoritmo que receba 4 valores inteiros A, B, C e D. Dados os valores, se B for
maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de
A e B, e ainda, se ambos, C e D forem positivos e A for par, escrever a mensagem "Valores
aceitos", se não escrever "Valores não aceitos".
"""

def valores_inteiros(a, b, c, d):
  if b > c and d > a:
    if (c+d) > (a+b):
      if  c > 0 and d > 0 and a % 2 == 0:
        return "Valores aceitos"

  else:
        return "Valores não aceitos"

resultado = valores_inteiros(2, 1, 6, 7)
print(resultado)
