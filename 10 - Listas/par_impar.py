# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
impar = []
par = []

while True:
    valor = int(input("Digite um número: "))
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

    continuar = input("Deseja continuar? [S/N]").upper().strip()[0]
    if continuar in "N":
        break

lista.sort()
par.sort()
impar.sort()

print("=-" * 25)
print(f"A lista completa é {lista}")
print(f"A lista de pares é {par}")
print(f"A lista de impares é {impar}")
