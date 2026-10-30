# Lista de Exercícios de Lógica e Programação em Python

Este repositório reúne 7 exercícios práticos de lógica de programação, manipulação de dados, expressões regulares e Programação Orientada a Objetos (POO) em Python. 

---

## Estrutura do Projeto

| Arquivo | Exercício | Conceitos Abordados |
| :--- | :--- | :--- |
| [`ex01_salario_liquido.py`](./ex01_salario_liquido.py) | **1. Cálculo de Salário Líquido** | Funções, operadores aritméticos, formatação de strings |
| [`ex02_valores_inteiros.py`](./ex02_valores_inteiros.py) | **2. Validação de Valores Inteiros** | Estruturas condicionais (`if`/`else`), operadores lógicos e relacionais |
| [`ex03_cedulas.py`](./ex03_cedulas.py) | **3. Decomposição em Cédulas** | Listas, laço `for`, divisão inteira (`//`), entrada de dados (`input`) |
| [`ex04_equacao.py`](./ex04_equacao.py) | **4. Resolução de Equação Linear** | Funções, tratamento de condição de contorno ($A + B = 0$) |
| [`ex05_sequencia_numeros.py`](./ex05_sequencia_numeros.py) | **5. Avaliação de Sequência Numérica (1 a N)** | Laços aninhados, divisores (número perfeito), múltiplos, biblioteca `math` |
| [`ex06_pato.py`](./ex06_pato.py) | **6. Modelagem de um Pato (POO)** | Classes, atributos, construtor (`__init__`), métodos |
| [`ex07_placa_mercosul.py`](./ex07_placa_mercosul.py) | **7. Conversor de Placas (Brasil / Mercosul)** | Dicionários, Expressões Regulares (`re`), manipulação de listas e strings |

---

## Descrição dos Exercícios

### 1. Salário Líquido (`ex01_salario_liquido.py`)
Calcula o salário líquido de um trabalhador a partir da quantidade de horas trabalhadas por dia, do valor da hora e dos dias trabalhados no mês, aplicando um desconto de 3% sobre o salário bruto.

### 2. Validação de 4 Valores Inteiros (`ex02_valores_inteiros.py`)
Recebe 4 valores inteiros (`A`, `B`, `C`, `D`) e verifica se atendem simultaneamente às condições:
- `B > C` e `D > A`
- `(C + D) > (A + B)`
- `C` e `D` positivos
- `A` par

Retorna `"Valores aceitos"` ou `"Valores não aceitos"`.

### 3. Decomposição em Notas / Cédulas (`ex03_cedulas.py`)
Lê um valor inteiro e calcula a menor quantidade possível de cédulas (`200`, `100`, `50`, `20`, `10`, `5`, `2` e `1`) necessárias para compor esse valor.

### 4. Equação Linear $AX + BX + C = 1$ (`ex04_equacao.py`)
Recebe os coeficientes inteiros `A`, `B` e `C` e calcula o valor de `X` na equação $AX + BX + C = 1$. Caso $A + B = 0$, informa `"solução impossível"`.

### 5. Sequência de Números de 1 a N (`ex05_sequencia_numeros.py`)
Recebe um número inteiro positivo `N` e avalia cada número de `1` até `N`, classificando-o caso seja:
- **Número perfeito** (soma dos divisores próprios igual ao número)
- **Múltiplo de 3**
- **Múltiplo de 5**
- **Raiz quadrada inteira**

### 6. Programe um Pato (`ex06_pato.py`)
Implementa a classe `Pato` com os atributos `nome`, `fase` (ex.: `"filhote"` ou adulto) e `fome`, além dos métodos `atividade()` e `comer()`.

### 7. Placa Brasil ↔ Mercosul (`ex07_placa_mercosul.py`)
Valida uma placa informada nos formatos `AAA9999` (Padrão Brasil) ou `AAA9A99` (Padrão Mercosul) utilizando expressões regulares (`re`) e realiza a conversão do 5º caractere entre número e letra correspondente.

---

## Como Executar

Certifique-se de ter o **Python 3** instalado em sua máquina.

Para executar qualquer um dos exercícios individualmente no terminal:

```bash
python ex01_salario_liquido.py
python ex02_valores_inteiros.py
python ex03_cedulas.py
python ex04_equacao.py
python ex05_sequencia_numeros.py
python ex06_pato.py
python ex07_placa_mercosul.py
```
