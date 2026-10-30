"""
3) Faça um algoritmo que receba um valor inteiro. Dado o valor, calcule o menor número
de notas (cédulas) possíveis no qual o valor pode ser decomposto. As notas consideradas
são de 200, 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas
necessárias.
"""

valor = int(input("Digite um valor inteiro:"))
print(f"\nPara {valor}:")

cedulas = [200, 100, 50, 20, 10, 5, 2, 1]

for c in cedulas:
  total = valor // c
  valor = valor - ((total) * c)
  print(f"- {total} nota(s) de R${c:.2f}")
