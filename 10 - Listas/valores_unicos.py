# Adiciona numeros não repetidos em uma lista que não possui tamanho pré-definido

continuar = ''
lista = []
valor = 0

while continuar != 'N':
    valor = int(input("Digite um valor: "))

    if valor not in lista:
        lista.append(valor)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não vou adicionar...")
    
    continuar = input("Quer continuar? [S/N]").upper().strip()[0]

lista.sort()
print("Você digitou os valores {}".format(lista))

