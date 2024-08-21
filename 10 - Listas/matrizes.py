# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f"Digite um valor para o [{i+1}, {j+1}]: "))
        matriz[i][j] = valor


print("=-" * 30)
for n in range(0, 3):
    print('')
    for m in range(0,3):
        print(f"[{matriz[n][m]:^5}]",end="")  # esse "":^5" é para centralizar o texto (^) e considerar 5 caracteres para cada indice da matriz

print("")