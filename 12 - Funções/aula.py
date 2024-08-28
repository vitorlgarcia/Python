# Aula de funções no python

def lin(txt):
    print("=-" * 30)
    print(txt)
    print("=-" * 30)

lin("Sua mensagem Python")


def soma(a, b):
    print(a + b)

soma(2, 5)
soma(3, 2)

def contador(* num):   # Usando o asteristico antes da variável de parâmetro, ela adiciona a quantidade de números que for passado para ela e coloca tudo dentro de uma tupla
    for valor in num:
        print(f"{valor} ", end='')
    print("FIM")

contador(2, 6)
contador(3, 4, 7, 9)
contador(2, 4, 8)


def dobra(lst):
    p = 0
    while p < len(lst):
        lst[p] *= 2
        p += 1

lista = [1, 2, 6, 5, 4]
print(lista)
dobra(lista)
print(lista)


def soma(* valores):
    total = 0
    for numero in valores:
        total += numero
    
    print(f"Somandos os valores {valores} o resultado é {total}")


soma(2, 5, 8)
soma(1, 7)
soma(6, 88, 9, 5, 4, 2, 4)