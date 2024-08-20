# Crie um programa que vai ler vários numeros e colocar em uma lista. Depois disso, mostre: 1 - Quantos números foram digitados, 2 - A lista de valores, ordenada de forma descrescente. 3 - Se o valor 5 foi digitado e está ou não na lista.

lista = []
continuar = ''

while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    continuar = input("Quer continuar? [S/N] ").upper().strip()[0]
    if continuar in "N":
        break

print(f"Você digitou {len(lista)} elementos.")

lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são: {lista}")

if 5 in lista:
    print("O valor 5 FOI encontrado na lista!")

else:
    print("O valor 5 NÃO foi encontrado na lista!")