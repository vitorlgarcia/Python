# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: 1 - Quantas pessoas foram cadastradas, 2 - Uma listagem com as pessoas mais pesadas, 3 - Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()
maiorpeso = menorpeso = 0
gordinhos = list()
magrinhos = list()

while True:
    nome = input("Nome: ")
    dados.append(nome)
    peso = float(input("Peso: "))
    dados.append(peso)

    if menorpeso == 0:
        menorpeso = peso
    if peso > maiorpeso:
        maiorpeso = peso
    if peso < menorpeso:
        menorpeso = peso

    pessoas.append(dados[:]) # Não esquecer do fatiamento para copiar listas dentro de lista
    dados.clear()

    continuar = input("Quer continuar? [S/N]").upper().strip()[0]

    if continuar == 'N':
        break


print(f"Ao todo, você cadastrou {len(pessoas)} pessoas")


for p in pessoas:
    if p[1] == menorpeso:
        magrinhos.append(p[0])
    if p[1] == maiorpeso:
        gordinhos.append(p[0])

print(f"O maior peso foi de {maiorpeso}Kg. Peso de {gordinhos}")

print(f"O menor peso foi de {menorpeso}Kg. Peso de {magrinhos}")