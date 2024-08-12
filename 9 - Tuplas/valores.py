# faz usuário digitar 4 valores e verifica quantas vezes apareceu o numero 9, em que posição foi digitado o primeiro valor 3 e quais foram os números pares.

nove = 0
par = 0
num = (int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: ")), int(input("Digite o quarto número: ")))

for i in num:
    if i == 9:
        nove += 1
    if i % 2 == 0:
        par += 1
    if i == 3:
        tres = num.index(3)
        print(f"O número 3 aparece na posição {tres + 1}")

print(f"o numero 9 apareceu {nove} vez(es)")
print(f"Números pares aparecem {par} vez(es)")
print(f"Você digitou os valores {num}")