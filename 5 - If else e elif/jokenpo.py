import random
from time import sleep  # importa o método sleep do módulo time

computador = random.randint(1,3)
jogadas = ("PEDRA", "PAPEL", "TESOURA")
print(''' Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA ''')
opcao = int(input("Qual é a sua jogada? "))

if opcao > 3:
    opcao = 3  # Caso o usuário digitar uma opção maior do que 3, o programa vai ajustar para 3, pois assim não vai ter erro no programa devido ao estouro dos indices do vetor jogadas que são 3.


# USANDO IFs para mostrar a jogada do PC e do usuário também daria certo, mas ficaria muito longo
###################################################
#if computador == 1:
#    jogadapc = "PEDRA"
#elif computador == 2:
#    jogadapc = "PAPEL"
#elif computador == 3:
#    jogadapc = "TESOURA"
#else:
#    jogadapc = "Jogada inválida!"

#if opcao == 1:
#    jogadausuario = "PEDRA"
#elif opcao == 2:
#    jogadausuario = "PAPEL"
#elif opcao == 3:
#    jogadausuario = "TESOURA"
#else:
#    jogadausuario = "JOGADA INVALIDA!"
####################################################

if (computador == 1 and opcao == 1) or (computador == 2 and opcao == 2) or (computador == 3 and opcao == 3):
    resultado = "EMPATE"

elif computador == 1 and opcao == 3:
    resultado = "COMPUTADOR VENCE"

elif computador == 1 and opcao == 2:
    resultado = "JOGADOR VENCE"

elif computador == 2 and opcao == 1:
    resultado = "COMPUTADOR VENCE"

elif computador == 2 and opcao == 3:
    resultado = "JOGADOR VENCE"

elif computador == 3 and opcao == 1:
    resultado = "JOGADOR VENCE"

elif computador == 3 and opcao == 2:
    resultado = "COMPUTADOR VENCE!"

else:
    resultado = "Não valeu!!!"

print("JO")
sleep(1)  # apenas para dar 1 segundo de pausa para causar aquela emoção no jogo!!!

print("KEN")
sleep(1)

print("PO!!!")
print('-=' * 15)
print("Usuário jogou: {}".format(jogadas[opcao - 1])) # lembrando que o vetor tem indices [0, 1, 2]
print("Computador jogou: {}".format(jogadas[computador - 1])) # por isso coloquei -1 no índice
print('-=' * 15)
print(resultado)
