# Numeros primos
numero = int(input("Digite um número qualquer: "))
contador = 0
for i in range(1, numero+1):
    if numero % i == 0:
        contador += 1
        print(" \033[33m{}\033[m".format(i), end = " -> ")
    else:
        print(" \033[32m{}\033[m".format(i), end = " -> ")

if contador > 2:
    print("")
    print("Esse numero NÃO é primo!")

else:
    print("")
    print('Esse numero é SIM numero primo!')