# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt("Digite um n: ")

def leiaInt(msg):
    num = input(msg)
    while True:
        if num.isnumeric():
            return num
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m") #033[0;31m para mostrar cor vermelha!!!
            num = input(msg)

print("-"*40)
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")