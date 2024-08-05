# Jogo do par ou impar com o computador

from random import randint

print("=-" * 25)
print("VAMOS JOGAR PAR OU IMPAR")
print("=-" * 25)

soma = 0
contador = 0
while True:
    computador = randint(0,10)
    usuario = int(input("Diga um valor: "))
    parimpar = input("Par ou Ímpar? [P/I] ").upper().strip()[0]
    soma = usuario + computador
    while parimpar not in "PpIi":
        parimpar = input("Opção inválida! Você quer par ou ímpar? ").upper().strip()[0]
        
    print("-" * 25)
    if soma % 2 == 0:
        print(f"Você jogou {usuario} e o computador {computador}. Total de {soma} DEU PAR")
        if parimpar in "Pp":
            print("Você VENCEU! Vamos Jogar novamente...")
            contador += 1
            print("-" * 25)
                    
        elif parimpar in "Ii":
            print("Você PERDEU!")
            print("=-" * 25)
            break
    
    else:
        print(f"Você jogou {usuario} e o computador {computador}. Total de {soma} DEU IMPAR")
        if parimpar in "Ii":
            print("Você VENCEU! Vamos jogar novamente...")
            contador += 1
            print("-" * 25)
        
        elif parimpar in "Pp":
            print("VOCE PERDEU!")
            print("=-" * 25)
            break

print(f"GAME OVER! Você venceu {contador} vezes")
