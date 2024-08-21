teste = list()   # teste = [] também cria uma lista em branco
teste.append("Gustavo")
teste.append(40)

galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)

print(galera)  # [['Maria', 22], ['Maria', 22]]

# LEMBRE-SE que ao copiar uma lista simplesmente usando o sinal de atribuição (=) ou adicionando uma lista em outra usando append, uma lista fica dependente da outra. O correto é copiar uma lista usando o fatiamento "[:]". Assim uma lista não vai ser apontada para a lista de origem (não será dependente dela).

teste = list()   # teste = [] também cria uma lista em branco
teste.append("Gustavo")
teste.append(40)

galera = list()
galera.append(teste[:]) # sinal de fatiamento indicando copia do começo ao fim da lista "[:]"
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)  # [['Gustavo', 40], ['Maria', 22]]



# Selecionando indices e subíndices de uma lista composta

pessoas = [["Joao", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]

print(pessoas[0][0])  # "Joao"
print(pessoas[2][1])  # 13
print(pessoas[3])     # ['Maria', 45]


# Usando laço de for para apresentar informações da lista composta

for p in pessoas:
    print(f"{p[0]} tem {p[1]} anos de idade.")



# Obtendo informações para montar uma lista composta:

humanos = []
dado = []
totalmaior = totalmenor = 0

for i in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input("Idade: ")))
    humanos.append(dado[:]) # Não esquecer de copiar usando o [:], pois a lista "dado" será limpa usando o método clear e o print(humanos) iria mostrar os vetores zerados
    dado.clear()

print(humanos)


for i in humanos:
    if i[1] > 18:
        print(f"{i[0]} é maior de idade")
        totalmaior += 1
    else:
        print(f"{i[0]} é menor de idade")
        totalmenor += 1

print(f"Temos um total de {totalmaior} pessoa(s) maior(es) de idade e {totalmenor} pessoa(s) menor(es) de idade")

