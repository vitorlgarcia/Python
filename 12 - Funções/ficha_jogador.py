# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: O nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog="<desconhecido>",goles=0): # parametro opcional: se não for enviado nada para esses parametrros, o jogador é chamado de '<desconhecido>' e os gols são iguais a zero.
    print(f"O jogador {jog} fez {gols} gol(s) no campeonato.")


jogador = input("Nome do jogador: ")
gols = input("Numero de Gols: ")

if gols.isnumeric():  # identifica se o numero de gols foi digitado como número. Ex: 5 (não pode escrever "cinco")
    gols = int(gols) # caso foi numérico, transformar ele em um inteiro (input sempre transforma tudo em string)

else:
    gols = 0 # caso não foi digitado um algarismo, considera a variavel gols como 0

if jogador.strip() == '':  # Caso a variável jogador não recebeu nenhum caracter...
    ficha(goles=gols) # envie para a função somnete o numero de gols digitados

else:
    ficha(jogador,gols) # caso foi digitado algo na variável "jogador", envie os parametros nome do jogador e os gols dele também.