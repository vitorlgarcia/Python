# Digita 3 numeros e descobre quem é o maior e o menor
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if n1 <= n2 and n1 <= n3:
    menor = n1

elif n2 <= n1 and n2 <= n3:
    menor = n2

elif n3 <= n1 and n3 <= n2:
    menor = n3

print("O menor numero é {}".format(menor))

if n1 >= n2 and n1 >= n3:
    maior = n1

elif n2 >= n1 and n2 >= n3:  # elif = else if (então se)
    maior = n2

elif n3 >= n1 and n3 >= n2:
    maior = n3

print("O maior numero é {}".format(maior))



# Calculo aumento de salario
salario = float(input("Digite o salário: "))

if salario <= 1250:
    salarioNovo = salario * (1 + 0.15)

else:
    salarioNovo = salario * (1 + 0.10)

print("Seu novo salario passará a ser R${:.2f} reais".format(salarioNovo))



# Analisar se tres retas conseguem formar um triangulo

lado1 = int(input("Digite a reta de numero 1: "))
lado2 = int(input("Digite a reta de numero 2: "))
lado3 = int(input("Digite a reta de numero 3: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Os seguimentos acima PODEM FORMAR TRIANGULO")

else:
    print("Os seguimentos NÃO podem formar triângulo")
    