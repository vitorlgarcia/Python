# Módulo moeda criada para ser importada dentro do arquivo principal.py. Esse módulo possui as funções aumentar, diminuir, dobro e metade.

def aumentar(valor = 0, porcent = 0):
    aumentado = valor * (1 + porcent/100)  # aumenta em 10% o valor inicial
    return aumentado


def diminuir(valor = 0, porcent = 0):
    diminuido = valor * (1 - porcent/100)  # diminui em 10% o valor inicial
    return diminuido


def dobro(valor = 0):
    dobrado = valor * 2  # dobra o valor inicial
    return dobrado


def metade(valor = 0):
    metade = valor/2  # reduz a metade o valor inicial
    return metade

def formatacao(valor=0, moeda= 'R$'):
    return f"{moeda}{valor:.2f}".replace('.', ',')