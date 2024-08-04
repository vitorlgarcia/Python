# Progressão Artmética melhorada onde você pode mostrar quantas séries quer mostrar

print("Gerador de PA")
print("=-" * 20)

p1 = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
numtermos = 10
totaltermos = 0
pa = p1 + numtermos * razao


while numtermos != 0:
    while p1 < pa:
        print("{} -> ".format(p1), end="")
        p1 += razao
        totaltermos += 1
    print("PAUSA")
    numtermos = int(input("Quantos termos você quer mostrar mais? "))
    pa = p1 + numtermos * razao
    
    

print("Progressão finzalizada com {} termos mostrados".format(totaltermos))