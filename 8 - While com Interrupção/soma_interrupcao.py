# Pede ao usuário para adicionar números até digitar 999, o qual é o número designado para interromper o programa.

contador = 0
soma = 0
while True:
    numero = int(input("Digite um valor (999 para parar): "))
    if numero == 999:
        break
    soma += numero
    contador += 1

print(f"A soma dos {contador} valores foi {soma}") # NOVA FORMA de informar variáveis no print. Necessário colocar o "f" antes de abrir as aspas.