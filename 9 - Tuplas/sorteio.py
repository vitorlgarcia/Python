from random import randint

sorteados = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))

print("Os valores sorteados foram: ", end="")

for n in sorteados:
    print(f"{n} ", end="")

print("")
print(f"O maior valor sorteado foi {max(sorteados)}")
print(f"O menor valor sorteado foi {min(sorteados)}")