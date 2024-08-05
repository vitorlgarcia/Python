print("-" * 25)
print("LOJA SUPER BARATÃO")
print("-" * 25)

mil = barato = soma = 0
produtobarato = ''

while True:
    produto = input("Nome do Produto: ")
    preco = float(input("Preço: R$ "))
    soma += preco
    if barato == 0:
        barato = preco
        produtobarato = produto
    elif preco < barato:
        barato = preco
        produtobarato = produto
    
    if preco > 1000:
        mil += 1
        
    continuar = input("Quer continuar? [S/N]").upper().strip()[0]
    while continuar not in "SN":
        continuar = input("Por favor digite S para sim ou N para não: ").upper().strip()[0]
    
    if continuar == "N":
        break

print("O total de compra foi {:.2f}".format(soma))
print(f"Temos {mil} produtos custando mais de R$ 1000,00")
print("O produto mais barato foi {} que custa R${:.2f}".format(produtobarato, barato))