peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

print("IMC é: {:.2f}".format(imc))
if imc < 18.5:
    print(" Magreza extrema!")

elif imc <= 24.9:
    print("IMC é normal")

elif imc <= 29.9:
    print("Sobrepeso!")

elif imc <= 34.9:
    print("Obesidade grau 1")

elif imc <= 39.9:
    print("Obesidade grau II")

else:
    print("Obesidade grau III")
