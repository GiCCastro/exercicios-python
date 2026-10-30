"""
5. Construa um algoritmo que recebe um número inteiro positivo N e gere uma
sequência de números inteiros positivos, de 1 a N. O algoritmo deverá avaliar cada
número dessa sequência da seguinte forma:

- Caso seja um número perfeito, imprimir a mensagem “numero perfeito“;
- Caso seja um múltiplo de 3, imprimir “multiplo de 3”;
- Caso seja um múltiplo de 5, imprimir “multiplo de 5”;
- Caso seja um número com a raiz quadrada inteira, imprimir “raiz inteira”.

Considerações:
Um número perfeito é um número cujo a soma de todos os seus divisores
naturais próprios (excluindo ele mesmo) é igual ao próprio número.
Exemplo: 6 pode ser dividido por 1, 2 e 3, e quando você soma esses números o
resultado é 6.
"""

import math
inteiro_positivo = int(input("Digite um valor inteiro positivo"))


for n in range (1, (inteiro_positivo+1)):
  divisor = 0
  teste_raiz = 0

  for d in range(1, n):

    if n % d == 0:
      divisor += d

  print("-"*50)
  print(f"\n*****AVALIAÇÃO DO NÚMERO {n}*****\n")

  if divisor == n:
    print("- número perfeito")

  if n % 3 == 0:
   print("- múltiplo de 3")

  if n % 5 == 0:
   print("- múltiplo de 5")

  raiz = math.sqrt(n)
  if raiz % 1 == 0:
    print("- raiz inteira")

