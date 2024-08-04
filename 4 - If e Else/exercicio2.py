# Teste velocidade: Se estiver acima de 80km/h, mostrar mensagem de multado e apresentar o valor da multa que é de R$ 7,00 por cada Km acima do limite
velocidade = int(input("Qual é a velocidade que está dirigindo? (km/h) "))
if velocidade <= 80:
    print("Continue dirigindo com segurança")

else:
    print("Você foi multado por excesso de velocidade")
    multa = (velocidade - 80) * 7 # Considera somente o excedente da velociade que pagará o valor da multa de R$ 7,00 para cada km que ficar acima dos 80km/h
    print("Valor da multa: R${:.2f} reais".format(multa))

print("Tenha uma bom dia!")
