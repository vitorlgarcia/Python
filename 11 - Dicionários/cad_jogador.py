# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
jogador['nome'] = input("Nome do jogador: ")


partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
gols = list()
total = 0

for i in range(0, partidas):
    gols.append(int(input(f"Quantos gols na partida {i+1}? ")))
    total += gols[i]

jogador['gols'] = gols[:]  # Sempre lembrar de copiar uma lista para outra dessa forma
jogador['total'] = total

print("=-" * 30)
print(jogador)
print("=-" * 30)

for k, v in jogador.items():
    print(f"o campo {k} tem valor {v}")

print("=-" * 30)

print(f"O jogador {jogador["nome"]} jogou {partidas} partidas") 

for i, n in enumerate(jogador['gols']):     # laço de for que fará a iteração da lista contida dentro do dicionário. Não esquecer do "enumerate" para que seja apresentado o número do índice e valor de cada item da lista
    print(f"Na partida {i}, fez {n} gols")

print("foi um total de {} gols".format(jogador['total'])) # mostrando os dados usando .format() para relembrar