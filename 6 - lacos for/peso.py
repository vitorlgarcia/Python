pesomin = 0
pesomax = 0
for i in range(1,6):
    peso = float(input("Peso da {}a pessoa (kg): ".format(i)))
    if i == 1:
        pesomax = peso
        pesomin = peso
    if peso >= pesomax:
        pesomax = peso
    if peso <= pesomin:
        pesomin = peso

print("O maior peso lido foi de {}Kg".format(pesomax))
print("O menor peso lido foi de {}Kg".format(pesomin))