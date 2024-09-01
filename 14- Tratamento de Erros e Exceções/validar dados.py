# Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiafloat() com a mesma funcionalidade

def leiaint(msg):  
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError): # ValueError se for digitado o numero como "cinco", "sete". E será erro do tipo TypeError se o tipo do valor digitado for diferente de 'int'.
            print("\033[31mErro! Formato de número não aceito. Digite novamente\033[m")
        
        except KeyboardInterrupt:
            print("Entrada de dados interrompida pelo usuário.")
            break

        else:
            return n

num = leiaint("Digite um numero: ")
print(f"O numero digitado foi {num}")
