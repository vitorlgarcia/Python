# Exercicio 8 - Desconto no produto

valor = float(input("Qual é o preço do produto? "))
desconto = float(input("Qual percentual de desconto deseja aplicar? "))
#valorfinal = valor - (valor*desconto/100)
valorfinal = valor * (1 - (desconto/100))
print("O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f}".format(valor, desconto, valorfinal))


# Exercicio 9 - Aumento de salario
salario = float(input("Seu salario atual: "))
aumento = float(input("Qual é o percentual de aumento? "))
valorajustado = salario * (1 + (aumento/100))
#valorajustado = salario + (salario*aumento/100)
print("O salario de R${:.2f} reais ajustado em {:.2f}% vai para R${:.2f} reais".format(salario, aumento, valorajustado))


# Exercicio 10 - Conversão de temperatura
tempcelcius = float(input("Qual é a temperatura em Celcius? "))
tempfaren = 9/5 * tempcelcius + 32
print("A temperatura de {:.1f}C corresponde a {:.1f}F".format(tempcelcius, tempfaren))


# Ecercicio 11 - Aluguel de carros
dias = int(input("Quantos dias o carro foi alugado? "))
kmrodado = int(input("QUantos km rodados? "))
totalpagar = dias * 60 + kmrodado * 0.15
print("O total a pagar é de R${:.2f}".format(totalpagar))
