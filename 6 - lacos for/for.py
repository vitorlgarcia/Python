from time import sleep

lista = ("banana", "pera", "uva", "maça", "salada mista", "manga")
for i in lista:
    print(i)

# Exercicio de contagem regressiva
for i in range(10,-1,-1): # Coloquei -1 no range final para que o comando conte até 0 (lembrando que em vetores e no comando range o ultimo elemento não é considerado)
    print(i)
    sleep(0.5)

print("ACABOUUU !!!")


# Contagem de 1 até 50 apenas mostrando numeros pares
for i in range(0,50):
    if i % 2 == 0:
        print(i)
print("ACABOUUU!!!!")


# Contagem de numeros impares e multiplos de 3 que vão de 0 até 500
soma = 0
contador = 0
for i in range(0,501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
        contador += 1

print(" Soma de todos os {:.0f} numeros é igual a {:.0f}".format(contador, soma))