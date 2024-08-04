# Saber se nasci em uma cidade chamada SANTO

cidade = input("Em que cidade vocẽ nasceu? ").strip()  # Caso for digitado espaços antes e depois da cidade, o comando strip deixa apenas o nome da cidade
cidade = cidade.lower()
santo = "santo" in cidade
print(santo)


# Saber se tem "Silva" no nome

nome = input("Digite seu nome completo: ")
nome = nome.lower()
silva = "silva" in nome
print("Seu nome tem silva? {}".format(silva))

# Quantas vezes a palavra "A" aparece na frase
frase = input("Digite qualquer frase: ").strip()
frase = frase.lower()
print("A letra A aparece {} vezes na frase".format(frase.count("a")))
print("A primeira letra A apareceu na posição {}".format(frase.find("a")+1))
print("A ultima letra A aparece na posicao {}".format(frase.rfind("a")+1))


# Achar o primeiro e ultimo nome da pessoa
nomeCompleto = input("Digite seu nome completo: ").strip()
lista = nomeCompleto.split() # Divide o nome completo em indices de uma lista. Ex: [vitor, lopes, garcia]
ultimoNome = len(lista) # mostra o comprimento da lista. Uma lista que possui 3 indices, por exemplo, vai ter comprimento 3 --> [0, 1, 2] nomes
print("Seu primeiro nome é {}".format(lista[0]))
print("Seu último nome é {}".format(lista[ultimoNome-1])) # O -1 é porque uma lista sempre começa com o índice 0. Uma lista de N índices vai do índice 0 até N-1.