# Analisar se tres retas conseguem formar um triangulo e selecionar qual tipo de triangulo é

# EQUILATERO: Todos os lados iguais
# ISÓSCELES: Dois lados iguais
# ESCALENO: Todos os lados diferentes

lado1 = int(input("Digite a reta de numero 1: "))
lado2 = int(input("Digite a reta de numero 2: "))
lado3 = int(input("Digite a reta de numero 3: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print("Os seguimentos acima PODEM FORMAR TRIANGULO")

    if (lado1 == lado2 and lado1 == lado3 and lado2 == lado3):
        print("O triangulo é do tipo EQUILATERO")
    
    elif (lado1 != lado2 and lado2 != lado3 and lado1 != lado3):
        print(" O triangulo é do tipo ESCALENO")
    
    else:
        print("O triangulo é do tipo ISÓSCELES")

else:
    print("Os seguimentos NÃO podem formar triângulo")
    