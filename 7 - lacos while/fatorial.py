# Calcula o fatorial de qualquer número digitado.

from math import factorial

numero = int(input("Digite um número para calcular seu Fatorial: "))
print("Calculando {}!".format(numero), end=" = ")
fatorial = 1
while numero != 0:
    fatorial *= numero
    print(" {} ".format(numero), end="")
    numero -= 1
    if numero == 0:
        print (" ", end="")
    else:
        print("X", end="")
    

print(" = {}".format(fatorial))

# Método mais simples:
# f = factorial(numero)
# print(f)
    