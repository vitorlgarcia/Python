import random
numero = int(input("Em que numero eu pensei? (de 0 até 5) "))
print("PROCESSANDO...")

numerosorteado = random.randint(0,5)
if numero == numerosorteado:
    print("PARABÉNS! Você conseguiu me vencer!")

else:
    print("GANHEI! Eu pensei no número {} e não no {}".format(numerosorteado, numero))