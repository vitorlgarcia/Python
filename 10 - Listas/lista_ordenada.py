# Cria um programa onde o usuário possa digitar cinco valores numéricos e os cadastre em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela

lista = []
valor = 0
cont = 0

# Vão existir três casos para analisar: 1 - Se é o primeiro número a ser colocado na lista, o programa vai cair no primeiro if e o número será adicionado "no final da lista". 2 - Se o número é maior que o último número da lista, é entendido que o número é o maior numero de todos, vai cair no segundo if (elif) e vai ser "adicionado ao final da lista". 3 - O número será colocado no meio da lista. Daí é feito um laço while que varre do 0 até o comprimento da lista para achar a posição certa do novo número. Enquanto o novo número é maior que as posições iniciais da lista, a variável "cont" vai alterando até o numero novo ser colocado atrás do número maior do que ele.

for i in range(0,5):
    valor = int(input("Digite um valor: "))
    if i == 0:
        lista.append(valor)
        print("Adicionado no final da lista")

    elif valor >= lista[len(lista)-1]:
        lista.append(valor)
        print("Adicionado no final da lista")

    else:
        while cont < len(lista):
            if valor < lista[cont]:
                print(f"Adicionado na posição {cont} da lista")
                lista.insert(cont,valor)
                cont = 0
                break
            
            cont += 1

print("=-"*30)
print(f"A lista, em ordem numérica, é: {lista}")