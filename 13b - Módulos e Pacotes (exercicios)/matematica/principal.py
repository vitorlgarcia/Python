# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

val = int(input("Escreva um valor qualquer: R$"))

print(f"A medade de {moeda.formatacao(val)} é: {moeda.formatacao(moeda.metade(val))}")
print(f"O dobro de {moeda.formatacao(val)} é: {moeda.formatacao(moeda.dobro(val))}")
print(f"10% de desconto de {moeda.formatacao(val)} resulta em: {moeda.formatacao(moeda.diminuir(val, 10))}")
print(f"10% de aumento de {moeda.formatacao(val)} resulta em: {moeda.formatacao(moeda.aumentar(val, 10))}")


