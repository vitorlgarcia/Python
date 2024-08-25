# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá tambem o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

trabalhador = dict()

trabalhador['nome'] = input("Nome: ")
nascimento = int(input("Ano de nascimento: "))
trabalhador['idade'] = datetime.now().year - nascimento
trabalhador["registro"] = int(input("Carteira de Trabalho (0 não tem): "))

if trabalhador['registro'] > 0:
    trabalhador['contratacao'] = int(input("Ano de contratação: "))
    trabalhador['salario'] = float(input("Salário: R$ "))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratacao'] + 35) - datetime.now().year)

print("=-" * 30)

for k, v in trabalhador.items():
    print(f"{k} tem o valor {v}")