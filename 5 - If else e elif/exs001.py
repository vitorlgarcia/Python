# Calcular financiamento e aprovação de casa baseado no salario e no tempo de emprestimo

valorCasa = float(input("Valor da casa: "))
salario = float(input("Salario do comprador: "))
financiamento = int(input("Quantos anos de financiamento? "))

parcelas = valorCasa / (financiamento * 12)

print("Para pagar uma casa de R${:.2f} reais em {} anos a prestação será de R${:.2f} reais".format(valorCasa, financiamento, parcelas))

print("Parcela máxima que você pode pagar, baseado no seu salario: R${:.2f} reais".format(salario * 0.3))

if (parcelas < salario * 0.3):
    print("\033[0;32mParabéns! Vocẽ conseguirá adquirir sua casa nova!\033[m") # \o33[m formata as cores, estilo e fundo das palavras no python. Ver a configuração correta na imagem colocada nessa mesma pasta
    

else:
    print("\033[0;31mInfelizmente você não pode comprar nessas condições\033[m")