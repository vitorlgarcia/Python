# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

lista = list()
aluno = list()

while True:
    nome = input("Nome: ")
    aluno.append(nome)
    n1 = float(input("Nota 1: "))
    aluno.append(n1)
    n2 = float(input("Nota 2: "))
    aluno.append(n2)
    media = (n1 + n2)/2
    aluno.append(media)
    lista.append(aluno[:]) # Sempre lembrar da cópia usando fatiamento completo do vetor
    aluno.clear()

    continuar = input("Quer continuar? [S/N]").upper().strip()
    if continuar in "N":
        break

print("=-" * 40)

print(f"{"No.":<4}{"NOME":<10}{"MEDIA":>8}") # ":<4" significa 4 caracteres alinhado a esquerda
print("-" * 25)

for i, valor in enumerate(lista):
    print(f"{i:<4}{valor[0]:<10}{valor[3]:>8.1f}")

while True:
    print("-" * 25)
    estudante = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if estudante == 999:
        break

    while estudante >= len(lista):
        estudante = int(input(f"Não existe esse aluno. Ver um novo número abaixo de {len(lista)}: "))

    print(f"Notas de {lista[estudante][0]} são {lista[estudante][1:3]}") # Dentro do indice da sublista pedida pelo usuário, será mostrado as duas notas do aluno (subindice 1 e 2)

print("FINALIZANDO...")

print("<<< VOLTE SEMPRE >>>")