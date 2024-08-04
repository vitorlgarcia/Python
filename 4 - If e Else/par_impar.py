import datetime

# descobre se o numero digitado é par ou impar

numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print("O numero é par")

else:
    print("O numero é impar")


# Preço da passagem 

viagem = int(input("Digite quantos km será sua viagem: "))

if viagem <= 120:
    print(" O preço da sua viagem será de R${:.2f} reais".format(viagem * 0.5))

else:
    print("Preço promocional em viagens acima de 120km. O preço será de R${:.2f} reais".format(viagem * 0.45))


# calcular se o ano é bissexto
ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual:"))

if ano == 0:
    ano = datetime.date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO".format(ano))

else:
    print("O ano {} NÃO é BISSEXTO".format(ano))

