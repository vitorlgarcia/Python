# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: O primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(n, show):
    i = n
    fator = 1
    print("-"* 30)
    while i >= 1:
        fator *= i
        
        if show == True:
            print(f"{i}",end="")
            if i > 1:
                print(" x ",end="")
            else:
                print(" = ", end="")
        i -= 1
    
    return fator
    

print(fatorial(7, show=True))