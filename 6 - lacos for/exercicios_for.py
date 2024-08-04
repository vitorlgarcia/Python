# Tabuada usando laço de for
numero = int(input("Digite um numero para ver sua tabuada: "))

for i in range(1, 11): # coloquei 11 para a tabuada ir do 0 até o 10
    print("{} x {} = {}".format(numero, i, (numero * i)))

print("FIM !!! ")
print("-="*20)

# Soma apenas numeros pares no range de 1 até 6
soma = 0
contador = 0
for i in range(1,7):
    numero = int(input("Digite um número ({}): ".format(i)))
    if numero % 2 == 0:
        soma += numero
        contador += 1

print("Você informou {} numeros pares e a soma deles é {}".format(contador, soma))
print("FIM")
print("=" * 40)



# Progressão Aritmética
print("=" * 25)
print("     10 TERMOS DE UMA PA     ")
print("=" * 25)

numero = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
soma = 0
pa = numero + (10 - 1) * razao # formula da Progressao aritmética. Queremos o somatório dos numeros com inicio X e razão Y. Como quero saber o somatório até o décimo termo, eu coloquei o 10 na formula e a variavel "pa" fica com o valor da décima somatória dessa Progressão. Aí basta colocar esse valor no laço de for para o laço calcular o somatório até chegar nele.

for i in range(numero, (pa + 1), razao): # aqui coloquei o +1 para o ultimo elemento não ser ignorado
    soma += razao
    print(" {} ".format(i), end = " -> ") # comando end serve para não querbrar linha e colocar e ele coloca o que você desejar ao lado.
print(" ACABOU")