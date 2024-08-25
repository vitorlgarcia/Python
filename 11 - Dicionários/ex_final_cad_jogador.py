# Aprimore o desafio do cad_jogador para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador.

jogador = dict()
cadastro = list()
gols = list()

while True:
    gols.clear()
    jogador['nome'] = input("Nome do Jogador: ")
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    total = 0

    for i in range(0, partidas):
        gols.append(int(input(f"Quantos gols na partida {i+1}? ")))
        total += gols[i]

    
    jogador['gols'] = gols[:] # Copiando a lista de gols do jogador dentro do dicionário dele
    jogador['total'] = total

    cadastro.append(jogador.copy()) # Copiando o dicionario recem feito dentro de uma lista

    while True:
        continuar = input("Quer continuar? ").upper().strip()[0] # Validação para usuário digitar apenas S ou N para continuar ou não
        
        if continuar not in "SN":
            print("ERRO! Digite S para SIM continuar ou N para NÃO continuar")
        
        else:
            break
    
    if continuar == "N":
        break

print("=-" * 30)

print("Cod Nome            gols        total")
print("-" * 40)

for i, n in enumerate(cadastro):
    print(f"{i:>3} ", end = '')
    for v in n.values():
        print(f"{str(v):<15}", end= '')   # o str() é para deixar v como string e <15 é para alocar tudo no cando esquerdo dentro de um total de 15 caracteres (espaços vazios) vindo depois 

    print("")

while True:
    print("-" * 40)
    dados = int(input("Mostrar dados de qual jogador? (999 para parar)"))
    if dados == 999:
        break

    elif dados >= len(cadastro):
        print("Número inválido. Digite o número do jogador que aparece na lista: ")
    
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {cadastro[dados]['nome']}")

        for i, n in enumerate(cadastro[dados]['gols']):
            print(f" No jogo {i+1} fez {n} gols")


print("<< VOLTE SEMPRE >>")

