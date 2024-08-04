nome = input("Digite seu nome completo: ")
print("Analisando seu nome...")
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))

NomeSemEspaco = nome.split()   # Divide o nome em indices de uma lista, tendo o espaço como referencia, já que não foi colocado nenhuma outra referencia. Ex: [Vitor, Lopes, Garcia]
NomeSemEspaco = ''.join(NomeSemEspaco) #Junta todos os indices da lista "NomeSemEspaco" em uma só string, pois foi colocado um vazio como referencia. Ex: "VitorLopesGarcia"

print("Seu nome tem ao todo {} letras".format(len(NomeSemEspaco))) #comando len apresenta o comprimento da variavel (o numero de indices)

primeironome = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(primeironome[0], len(primeironome[0])))

