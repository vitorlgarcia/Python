# Soma a quantidade de numero que você for colocando

numero = int(input("Digite um número[999 para parar]: "))
contador = 0
soma = 0

while numero != 999:
    contador += 1
    soma += numero
    numero = int(input("Digite um número[999 para parar]: "))

print("Você digitou {} numeros e a soma entre eles foi {}".format(contador, soma))
