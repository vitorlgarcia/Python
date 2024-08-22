# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

lista = []
i = 0
jogos = int(input("Quantos jogos você quer que eu sorteie? "))

print(F"SORTEANDO {jogos} JOGOS")

while i < jogos:  # Enquanto não foi feito o numero total de jogos pedidos, continue o sorteio
    for int in range(0, 6):      # Sorteio dos 6 numeros da mega sena
        sorteio = randint(1, 60) # O sorteio é feito entre os numeros 1 e 60
        while sorteio in lista: # Enquanto estiver sorteando numero repetido, volta ao sorteio
            sorteio = randint(1, 60)

        lista.append(sorteio)
    
    lista.sort()    # Organiza os numeros sorteados em ordem crescente
    print(f"Jogo {i+1}: {lista}") 
    lista.clear()
    i += 1