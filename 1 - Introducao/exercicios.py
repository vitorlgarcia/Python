# Exercicio 1 - sucessor e antecessor
n = int(input("Digite um número "))
print("O número digitado foi o {}. Seu antecessor é o {} e o sucessor é o {}".format(n,(n-1),(n+1)))

# Exercicio 2 - Dobro, triplo e raiz quadrada
n1 = int(input("Digite um numero "))
print("O dobro de {} é {}".format(n1, (n1*2)))
print("O triplo de {} é {}".format(n1,(n1*3)))
print("A raiz quadrada de {} é {:.2f}".format(n1, (n1**(1/2))))


# Exercicio 3 - Média Artmética
v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("E agora o segundo valor: "))
#media = (v1+v2)/2
print("A média entre {} e {} é igual a {:.1f}".format(v1, v2, ((v1+v2)/2)))

# Exercicio 4 - Conversão de unidades (metro)

n2 = float(input("Uma distancia em metros (m): "))
print("A medida de {} corresponde a: ".format(n2))
print("{}km".format(n2/1000))
print("{}hm".format(n2/100))
print("{}dam".format(n2/10))
print("{:.0f}dm".format(n2*10))
print("{:.0f}cm".format(n2*100))
print("{:.0f}mm".format(n2*1000))


# Exercicio 5 - Tabuada
valor = int(input("Digite um valor para calcular a tabuada: "))
print("{} X  1 = {}".format(valor, (valor*1)))
print("{} X  2 = {}".format(valor, (valor*2)))
print("{} X  3 = {}".format(valor, (valor*3)))
print("{} X  4 = {}".format(valor, (valor*4)))
print("{} X  5 = {}".format(valor, (valor*5)))
print("{} X  6 = {}".format(valor, (valor*6)))
print("{} X  7 = {}".format(valor, (valor*7)))
print("{} X  8 = {}".format(valor, (valor*8)))
print("{} X  9 = {}".format(valor, (valor*9)))
print("{} X 10 = {}".format(valor, (valor*10)))

# Exercicio 6 - Conversão Dólar
reais = float(input("Quantos reais você tem na carteira? "))
dollar = float(input("Cotação do dóllar: "))
print("Com R${:.2f} reais você troca por U${:.2f} dólares".format(reais, (reais/dollar)))

# Exercicio 7 - Dimensao parede e litros de tinta
altura = float(input("Altura da parede "))
largura = float(input("Largura da parede "))
print("Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².".format(largura, altura, (largura*altura)))
print("Para pintar essa parede você precisará de {:.2f}l de tinta".format(largura*altura/2))
