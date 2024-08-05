# Faz o cadastro de pessoas até o usuário não querer mais continuar

maiordezoito = 0
homens = 0
mulher20 = 0
continuar = ''

while True:
    print("-" * 25)
    print("CADASTRE UMA PESSOA")
    print("-" * 25)

    idade = int(input("Idade: "))
    sexo = input("Sexo: [M/F]").upper().strip()[0]
    while sexo not in "MF":
        sexo = input("Por favor, insira M para masculino ou F para feminino: ").upper().strip()[0]
    print("-" * 25)

    if idade > 18:
        maiordezoito += 1
    
    if sexo == 'M':
        homens += 1
    
    else:
        if idade < 20:
            mulher20 += 1
    
    continuar = input("Quer continuar? [S/N] ").upper().strip()[0]
    while continuar not in "SN":
        continuar = input("Por favor responda com S de Sim ou N de não: ").upper().strip()[0]
        
    if continuar == 'N':
        break

print(f"Total de pessoas com mais de 18 anos: {maiordezoito}")
print(f"Ao todo temos {homens} homens cadastrados")
print(f"E temos {mulher20} mulheres com menos de 20 anos")

