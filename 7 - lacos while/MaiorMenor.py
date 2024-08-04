# Digite vários números e o programa irá retornar a média, maior e menor número digitado

continuar = 's'
numero = 0
soma = 0
maior = 0
menor = 0
contador = 0
while continuar not in "Nn":
    numero = int(input("Digite um número: "))
    if contador == 0:
        menor = numero
        maior = numero
    soma += numero
    contador += 1
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    
    continuar = input("Você quer continuar? [S/N] ").upper().strip()
    if continuar not in "NnSs":
        continuar = "s"

print("Você digitou {} números e a média foi {:.2f}".format(contador, (soma/contador)))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))