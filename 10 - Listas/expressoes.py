# rie um programa onde o usuário digite uma expressao qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

lista = []
expressao = input("Digite a expressão matemática: ")

for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    
    elif simbolo == ')':
        if len(lista) > 0:   # Se o comprimento da lista for maior que zero, significa que já foi aberto parenteses. Aí é só tirar o parenteses aberto da lista (pop) indicando que ele já foi fechado.
            lista.pop()
        
        else:
            lista.append(')') # se o comprimento da lista não for maior que zero (ou seja, ele é igual a zero), significa que nenhum parenteses foi aberto e um simbolo de fechar parenteses antes de abrir parenteses invalida a expressão matemática. Aí é só colocado uma expressão pra lista não ficar zerada e dá um break para fechar o programa.
            break

if len(lista) == 0:
    print("Sua expressão está válida!")

else:
    print("Sua expressão está errada! ")
