# Vamos criar um menu em Python, usando modularização

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt)
    print(linha())

def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[34m")
        c += 1
    print(linha())
    opc = leiaint("\033[32mSua opção: \033[m")
    return opc

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