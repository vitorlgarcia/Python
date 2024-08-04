from datetime import datetime

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("O primeiro número é MAIOR!")

elif n1 < n2:
    print("O segundo número é MAIOR!")

else:
    print("Os dois números são iguais!")



# Alistamento militar

anoAtual = datetime.now()
anoAtual = int(anoAtual.strftime("%Y"))

anoNascimento = int(input("Digite o ano que nasceu: "))
idade = anoAtual - anoNascimento

print("Quem nascem em {} tem {} anos em {}".format(anoNascimento, idade, anoAtual))

if idade < 18:
    print("Ainda faltam {} anos para o alistamento".format(18 - idade))
    print("Seu alistamento será somente em {}".format(anoAtual + (18 - idade ))) # para saber o ano de alistamento eu somei o ano atual com a diferença de 18 com a idade. Quem tem, 16 anos, por exemplo, só se alista dois anos depois (18 - 16) + ano atual. 

elif idade > 18:
    print("Já se passaram {} anos do seu alistamento".format(idade - 18)) # uma pessoa com 20 anos, por exemplo, já passaram 2 anos do alistamento
    print("Seu alistamento foi no ano de {}".format(anoAtual - (idade - 18))) # exemplo: 20 anos - 18 anos = 2 anos atrás em relação ao ano atual.

else:
    print("Esse ano você precisa se alistar!!")