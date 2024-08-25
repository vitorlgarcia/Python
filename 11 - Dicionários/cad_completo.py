# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: a) Quantas pessoas foram cadastradas. B) A média de idade. C) Uma lista com as mulheres. D) Uma lista de pessoas com idade acima da média.

pessoa = dict()     # Dicionario chamado de pessoa onde será colocado cada pessoa do cadastro
cadastro = list()   # Lista onde será salva todos os dicionários pessoas

while True:
    pessoa["nome"] = input("Nome: ")
    while True:
        sexo = input("Sexo: [M/F]").upper().strip()[0]    # laço while usado para validar que o usuário vai colocar apenas "M" ou "F". Se for colocado "m" ou "f" é dado um break
        if sexo in "MF":
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    pessoa["sexo"] = sexo
    pessoa["idade"] = int(input("Idade: "))
    cadastro.append(pessoa.copy())  # Copiando o dicionário recem feito dentro da lista

    while True:
        continuar = input("Quer continuar? [S/N]").upper().strip()[0] # Outro laço while validando
        if continuar in "SN":
            break
        print("ERRO! Responda apenas S ou N.")
    
    if continuar == "N":
        break

print(cadastro)

print(f"A) Ao todo foram cadastradas {len(cadastro)} pessoas")

total = 0
for v in cadastro:
    total += v['idade']

media = total / len(cadastro)

print(f"B) A média de idade é de {media} anos.")

print(f"C) As mulheres cadastradas foram: ", end='')

for v in cadastro:  # laço for para entrar na lista. A cada dicionario dentro da lista analisa se o item "sexo" é feminino ou não. Se for feminino, é printado o nome da mulher
    if v['sexo'] == "F":
        print(v['nome'], end=' ')
print("")

print("D) Lista das pessoas que estão acima da média: ")

for n in cadastro: # é feito um laço de for para iterar nos dicionários dentro da lista:
    if n['idade'] >= media: # se a idade do dicionário em questão for maior que a média...
        for k, v in n.items():  # é criado um novo laço for que agora navega em cada item do dicionário para printar todas as chaves e valores da pessoa que tem idade maior do que a média
            print(f"{k} = {v};", end=' ')

        print("")