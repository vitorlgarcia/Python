# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from random import randint
from time import sleep  # biblioteca usada para ir dando pausa nos comandos
from operator import itemgetter # função usada para coletar dados dos dicionários. Nesse caso vou coletar os values (valores dos randint) de cada indice dos dicionarios.

jogadores = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)}

for k, v in jogadores.items():
    print(f"O {k} tirou {v} no dado.")
    sleep(0.5)

print("=-" * 30)

print("== RANKING DOS JOGADORES ==")

ranking = list() # Repare que foi gerado uma lista ao inves de dicionários, pois o método itemgetter irá gerar uma lista com os valores coletados do dicionário.

ranking = sorted (jogadores.items(), key=itemgetter(1), reverse=True) # o 1 atribuído ao itemgetter significa que eu quis coletar a parte de "values" de cada "items". O sorted fará com que seja os números sejam organizados do menor para o maior, mas o desafio quer que eu organize do maior para o menor. Por isso foi usado o reverse=True.

for i, n in enumerate(ranking):  # laço de for para percorrer a lista ranking, pegando os indices e valores
    print(f"{i+1}o lugar: {n[0]} com {n[1]}") # a cada iteração o 'n' é igual a uma tupla dentro da lista. (ex: 'jogador2, 6). Então n[0] pega somente a parte "jogador2" da tupla e n[1] pega o "6" da tupla. Já o 'i' é o valor do índice percorrido atualmente a cada iteração.

print(ranking) # Só pedi para printar a lista "ranking" para melhor visualização da lista completa que está sendo percorrida com o laço de for.