lanche = ["hamburguer", "suco", "pizza", "sorvete"]
print(lanche)

lanche[2] = "Coxinha" # Altera o item da lista selecionando o índice do item que será alterado
print(lanche)

lanche.append("cookie") # comando para adicionar um item a uma lista. Será adicionado no final da lista

print(lanche)

lanche.insert(0,"hot dog") # Já o comando insert adiciona no local indicado pelo índice apresentado no começo do comando
print(lanche)

# Comando para apagar os indices da lista:

del lanche[3] # apaga o elemento de indice 3 da lista lanche (lembrando que indices começam no 0)
print(lanche)

lanche.pop(0)
print(lanche) # apaga o primeiro índice da lista lanche. O método pop sem parâmetro apaga o último elemento da lista

lanche.remove("cookie") # o método remove não remove os elementos pelos índices, mas sim apresentando o conteúdo que está presente na lista

print(lanche) # Se o comando remove for usando sem que exista o elemento procurado na lista, o programa irá voltar um erro.


# Para evitar qualquer erro ao tentar removar um elemento pelo nome, usar comando if. Exemplo:
if "suco" in lanche:
    lanche.remove("suco")
print(lanche)

# IMPORTANTE: O método remove vai excluir apenas o primeiro item. Se existisse mais de um item chamado "suco", por exemplo, apenas o primeiro da lista seria excluído.


valores = [5, 8, 7, 4, 2, 9, 3, 1, 0, 6]

valores.sort() # Comando sort organiza os valores do indice em ordem crescente
print(valores)


valores.sort(reverse=True) # Parâmetro reverse faz com que a ordem de valores seja decrescente
print(valores)

letras = ["B", "D", "T", "A", "H", "K", "S", "C", "V"] # A organização também serve com elementos do tipo string ou char. Não somente int ou float
letras.sort()
print(letras)


print(len(valores)) # Comando len (length) apresenta o tamanho da lista




lista = []

for cont in range(0, 5):
    lista.append(int(input("Digite um valor: ")))


for c, v in enumerate(lista): # Comando usado para mostrar o valor (v) e o indice (c) do vetor
    print(f"Na posição {c} encontrei o valor {v}!")

print("Cheguei ao final da lista")


# Particularidade do Python.

a = [2, 3, 4 ,7]
b = a
b[2] = 8
print(f"Lista A: {a}")  
print(f"Lista B: {b}") # Quando uma variável recebe uma lista, é como se o python passasse toda a referencia da lista a variável nova. Assim, se uma variável é alterado com um certo valor, a outra variável também será.

# Existe um modo para não ser criado uma ligação, mas sim uma cópia:

b = a[:]  # assim, se a lista "b" for alterada, a lista "a" não será.

