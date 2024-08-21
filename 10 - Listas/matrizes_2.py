# Preencha uma matriz 3x3 e ache a soma dos numeros pares digitados, a soma dos valores da terceira coluna e o maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

par = 0
terceiracoluna = 0
segundalinha = 0

for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(f"Digite um valor para o [{i+1}, {j+1}]: "))
        matriz[i][j] = valor

        if valor % 2 == 0:
            par += valor
        
        if j == 2:
            terceiracoluna += valor
        
        if i == 1:
            if valor > segundalinha:
                segundalinha = valor

print("=-"*40)

for n in range(0, 3):
    print('')
    for m in range(0,3):
        print(f"[{matriz[n][m]:^5}]",end="")

print('')
print("=-"*40)

print(f"A soma dos valores pares é {par}")
print(f"A soma dos valores da terceira coluna é {terceiracoluna}")
print(f"O maior valor da segunda linha é {segundalinha}")

