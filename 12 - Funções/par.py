# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
 
from random import randint
from time import sleep


def somaPar(lst):
    totpar = 0
    for i in lst:
        if i % 2 == 0:
            totpar += i
    print(f"Somando os valores pares de {lst}, temos {totpar}")

def sorteia():
    lista = list()
    print("Sorteando 5 valores da lista: ", end='')
    for i in range(0, 5):
        aleatorio = randint(0, 10)
        lista.append(aleatorio)
        print(f"{aleatorio} ", end='')
        sleep(0.5)
        
    print("PRONTO!")
    somaPar(lista)


sorteia()