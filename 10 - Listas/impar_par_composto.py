# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista ÚNICA que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]  # modo de declarar lista onde já são inicializados os índices 0 e 1 desde o inicio

for i in range(0, 7):
    valor = int(input(f"Digite o {i+ 1}o. valor: "))
    
    if valor % 2 == 0:   # saber se o valor digitado é par ou impar (resto da divisão por 2 é 0?)
        lista[0].append(valor)
    else:
        lista[1].append(valor)

lista[0].sort()  # Organizar o indice 0 [parte par] da lista em ordem crescente
lista[1].sort()  # Organizar o indice 1 [parte impar] da lista em ordem crescente

print(lista)

print(f"Os valores pares digitados foram: {lista[0]}")

print(f"Os valores impares digitados foram: {lista[1]}")

