"""
7) Sabendo da existência da nova placa Mercosul, e que um sistema precisa saber qual o
tipo da placa em questão, faça um algoritmo que receba uma placa e imprima qual o
padrão da placa informada e a versão correspondente da mesma placa no outro
padrão.

Considerações:
A placa informada, deverá ser validada, aceitando somente letras maiúsculas de A
a Z (sem acentos), números positivos e estar no formato AAA9999 ou AAA9A99.
Caso a placa informada não cumpra esses critérios, o algoritmo deverá imprimir
“formato inválido”.

Exemplo 1:
- Para a Placa ABC1234:
- Padrão: Brasil;
- Correspondente : ABC1C34.

Exemplo 2:
- Para a Placa ABC1C34:
- Padrão: Mercosul;
- Correspondente : ABC1234.
"""

import re

placa = {
    "0" : "A",
    "1" : "B",
    "2" : "C",
    "3" : "D",
    "4" : "E",
    "5" : "F",
    "6" : "G",
    "7" : "H",
    "8" : "I",
    "9" : "J"
}

brasil = 0
mercosul = 0


placa_informada = str(input("Digite a placa: "))

lista_placa = list(placa_informada)

regex = r"^[A-Z]{3}[0-9]{4}|([A-Z]{3}[0-9]{1}[A-Z]{1}[0-9]{2})$"
if not re.fullmatch(regex, placa_informada.upper()):
  print("formato inválido")

for i, v in enumerate(lista_placa):
  for chave, valor in placa.items():


     if v.isdigit():
        if lista_placa[4] == chave:
            lista_placa[4] = valor
            brasil += 1

     if lista_placa[4] == valor:
            lista_placa[4] = chave
            mercosul += 1


transformado = "".join(lista_placa) #não me recordava como usar o join, então pesquisei

print(f"Para a Placa {placa_informada}")
if brasil == 1:
 print(f"Padrão: Brasil")
if mercosul == 1:
   print(f"Padrão: Mercosul")
print(f"Correspondente: {transformado}")
