# Analisando numero e dizendo quanto milhar, centena, dezena e unidade tem

numero = int(input("Informe um número "))
unidade = numero // 1 % 10   # divide o numero por 1 e depois por 10. É guardado o resto da divisao por 10. ex: [numero = 4678] divido por 1 é 4678 e o resto da divisão por 10 é "8"
dezena = numero // 10 % 10 # divide o numero por 10 e depois por 10. É guardado o resto da divisao por 10. ex: [numero = 4678] dividido por 10 é 467 e o resto da divisão por 10 é "7"
centena = numero // 100 % 10 # divide o numero por 100 e depois por 10. É guardado o resto da divisao por 10. ex: [numero = 4678] dividido por 100 é 46 e o resto da divisão por 10 é "6"
milhar = numero // 1000 % 10 # divide o numero por 1000 e depois por 10. É guardado o resto da divisao por 10. ex: [numero = 4678] dividido por 1000 é 4 e o resto da divisão por 10 é "4"
print("Analisando o numero {}".format(numero))
print("Unidade: {}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar: {}".format(milhar))
