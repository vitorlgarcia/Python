preco = float(input("Preço das compras: R$"))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão    
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input("Qual é a opção? "))

if opcao == 1:
    print("10% de desconto!! Você só vai pagar R${:.2f} reais".format(preco * (1 - 0.1)))

elif opcao == 2:
    print("5% de desconto!! Você só vai pagar R${:.2f} reais".format(preco * (1 - 0.05)))

elif opcao == 3:
    print("Preço normal! O valor continua sendo R${:.2f} reais parcelados em 2x de R${:.2f} reais".format(preco, (preco / 2)))

elif opcao == 4:
    parcela = int(input("Em quantas vezes deseja parcelar? "))
    preco = preco * (1 + 0.2)
    print("Modalidade tem 20% de juros e assim vai para R${:.2f} reais".format(preco))
    print("Pagamento confirmado em {} vezes de R$ {:.2f} reais".format(parcela, (preco / parcela)))

else:
    print("OPÇÃO INVÁLIDA!!!")