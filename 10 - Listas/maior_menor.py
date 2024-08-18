# Usuário digita 4 numeros e será analisado os maiores e menores numeros da lista, podendo repetir o maior e o menor numero na lista

numeros = []
menor = 0
maior = 0

for i in range(0, 5):
    numeros.append(int(input("Digite um numero válido: ")))

print("=-" * 30)
print(f"Você digitou os valores {numeros}")

menor = min(numeros)
maior = max(numeros) 


print(f"O maior numero é {maior} e ele está na(s) posição(cões) de numero: ", end="")
for i, v in enumerate(numeros):
    if v == maior:
        print(f"{i+1}...", end="")

print("")
print(f"O menor numero é {menor} e ele está nas posição(ções) de numero: ", end="")
for i, v in enumerate(numeros):
    if v == menor:
        print(f"{i+1}...", end="")

print("")

