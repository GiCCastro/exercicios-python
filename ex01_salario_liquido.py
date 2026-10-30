"""
1) Faça um algoritmo que calcule o salário líquido de um trabalhador em função da
quantidade de horas por dia, do preço da hora trabalhada e dos dias trabalhados no mês.
Considerar um desconto de 3% sobre o salário bruto.
"""

def salario_liquido(horas_do_dia, preco_da_hora, dias_do_mes):

  bruto = (horas_do_dia * preco_da_hora) * dias_do_mes

  liquido = bruto - (3/100 * bruto)

  return liquido

resultado = salario_liquido(8, 20, 26)
print(f"O salário líquido resultou em R${resultado:.2f}")
