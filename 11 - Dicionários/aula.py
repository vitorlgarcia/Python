# Dicionários em Python

tupla = ()
lista = []           # Forma de declarar as tuplas, listas e dicionários
dicionario = {}

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)

# print(pessoas[0])  Dará erro, pois não é uma lista. Agora é um dicionário.

print(pessoas['nome'])  # Gustavo

print(f'O {pessoas['nome']} tem {pessoas["idade"]} anos de idade') # O Gustavo tem 22 anos de idade

print(pessoas.values()) # ['Gustavo', 'M', 22]
print(pessoas.keys()) # ['nome', 'sexo', 'idade']
print(pessoas.items()) # [('nome', Gustavo), ('sexo', 'M'), ('idade', 22)]


for k in pessoas.keys():
    print(k)  # nome     # sexo     # idade

for v in pessoas.values():
    print(v)   # Gustavo      # M      # 22


for k, v in pessoas.items():
    print(f"{k} = {v}")  # nome: "Gustavo"     # sexo = M      # idade = 22


del pessoas['sexo'] # Apaga o "sexo: M"
print(pessoas)   # {"nome": Gustavo, "idade": 22}


# Para adicionar um item no dicionário, não é usado o método append() igual nas listas. Basta acrescentar um novo item no dicionario. Exemplo:

pessoas['Naturalidade'] = 'Garça'
print(pessoas)  # {'nome': 'Gustavo', 'idade': 22, 'Naturalidade': 'Garça'}

# Caso já exista um item com o mesmo nome, ele simplesmente será editado:
pessoas['idade'] = 56
print(pessoas) # {'nome': 'Gustavo', 'idade': 56, 'Naturalidade': 'Garça'}


# Criando dicionários dentro de uma lista

brasil = list()  # brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil) # [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'Sao Paulo', 'sigla': 'SP'}]

print(brasil[0]) # {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}

print(brasil[0]['uf']) # 'Rio de Janeiro'
print(brasil[1]['sigla']) # SP


# Copiando dicionários dentro de lista através de informações do usuário:

estado = dict()
brasil = list()
for contador in range(0, 3):
    estado['uf'] = input("Unidade Federativa: ")
    estado['sigla'] = input("Sigla do Estado: ")
    #brasil.append(estado[:])  # essa cópia estará errada, pois o fatiamento completo somente é feito nas variáveis que são listas. Não são feitas nas variáveis do tipo dicionário. Para isso, existe um método específico para copiar os dicionários para dentro das listas ou mesmo duplicar dicionários:

    brasil.append(estado.copy())

print(brasil)

for e in brasil:   # será feita uma iteração em cada dicionário dentro da lista
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}.")  # O campo uf tem valor Sao Paulo / O campo sigla tem falor SP / O campo uf tem valor Paraná...

