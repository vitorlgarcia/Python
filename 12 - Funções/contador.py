# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo. Seu programa tem que realizar três contagens através da função criada.

from time import sleep

def contador(ini, final, passo):

    print("=-" * 30)

    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo = 1
    
    print(f"Contagem de {ini} até {final} de {passo} em {passo}")

    if ini < final:
        cont = ini
        while cont <= final:
            print(f"{cont} ", end="")
            sleep(0.5)
            cont += passo
    
    else:
        cont = ini
        while cont >= final:
            print(f"{cont} ", end="")
            sleep(0.5)
            cont -= passo

    print("FIM!")


contador(1, 10, 1)
contador(10, 2, 2)
print("Agora é a sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
