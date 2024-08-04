# Programa que lê o NOME, IDADE E SEXO de 4 pessoas. Depois retorna o media de idade, quem é o homem mais velho e quantas mulheres tem menos de 20 anos.

somaidade  = 0
maioridadehomem = 0
nomedohomem = ''
mulheresabaixovinte = 0
idade = 0
for i in range(0, 4):
    print("---- {}a PESSOA ----".format(i+1))
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper().strip()
    if sexo != 'M' and sexo != 'F':
        sexo = 'M'

    somaidade += idade
    
    if sexo == 'M' and idade >= maioridadehomem:
        maioridadehomem = idade
        nomedohomem = nome
    
    if sexo == 'F' and idade < 20:
        mulheresabaixovinte += 1


media = somaidade / 4

print("A média de idade do grupo é de {:.1f} anos.".format(media))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridadehomem, nomedohomem))
print("Ao todo são {} mulheres com menos de 20 anos".format(mulheresabaixovinte))
