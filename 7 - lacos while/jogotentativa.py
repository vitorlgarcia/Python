from random import randint

numeropc = randint(1,10)

numeromeu = int(input(''' Sou seu computador...
Acabei de pensar em um número de 0 a 10.
Ser[a que você consegue adivinhar qual foi?
Qual é o seu palpite? '''))

tentativa = 0
while numeromeu != numeropc:
    if numeromeu < numeropc:
        print("Mais... Tente mais uma vez.")
        numeromeu = int(input("Qual é o seu palpite? "))
        tentativa += 1

    elif numeromeu > numeropc:
        print("Menos... Tente mais uma vez.")
        numeromeu = int(input("Qual é o seu palpite? "))
        tentativa += 1

print("Acertou com {} tentativas! Parabéns".format(tentativa))
