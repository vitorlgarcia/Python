# Faça um programa que tenha uma função chama maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior

def maior(* numeros):
    print("=-" * 30)
    print("Analisando os valores passados...")
    print(f"{numeros} Foram informados {len(numeros)} valores ao todo.")
    if len(numeros) == 0:
        print("O maior valor informado foi 0")
    else:
        print(f"O maior valor informado foi {max(numeros)}")
    

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()