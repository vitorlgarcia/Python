# fazer uma progressão aritmética, mostrando os 10 primeiros numeros, usando WHILE

print("Gerador de PA")
print("=-" * 15)

p1 = int(input("Primeiro termo: "))
razao = int(input("razão da PA: "))
pa = p1 + 10 * razao  # Formula da progressao artimética adaptada ao laço de while, pois na fórmula é (10 - 1).

while p1 < pa:
    print("{} -> ".format(p1), end="")
    p1 += razao
    

print("FIM")