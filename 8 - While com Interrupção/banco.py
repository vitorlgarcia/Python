# usuario digite uma quantia em dinheiro e programa retorna quantas cédulas de cada valor será retornado

print("=" * 25)
print("BANCO CEV")
print("=" * 25)

dinheiro = float(input("Que valor você quer sacar? R$"))

cem = dinheiro // 100
dinheiro = dinheiro % 100
cinquenta = dinheiro // 50
dinheiro = dinheiro % 50
vinte = dinheiro // 20
dinheiro = dinheiro % 20
dez = dinheiro // 10
dinheiro = dinheiro % 10
cinco = dinheiro // 5
dinheiro = dinheiro % 5
dois = dinheiro // 2
dinheiro = dinheiro % 2
um = dinheiro

print("Total de {:.2f} cédulas de R$ 100,00".format(cem))
print("Total de {:.2f} cédulas de R$ 50,00".format(cinquenta))
print("Total de {:.2f} cédulas de R$ 20,00".format(vinte))
print("Total de {:.2f} cédulas de R$ 10,00".format(dez))
print("Total de {:.2f} cédulas de R$ 5,00".format(cinco))
print("Total de {:.2f} cédulas de R$ 2,00".format(dois))
print("Total de {:.2f} cédulas de R$ 1,00".format(um))
print("=" * 25)
print("Volte sempre ao BANCO CEV! Tenha um bom dia!")