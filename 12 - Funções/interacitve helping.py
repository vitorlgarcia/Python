# Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará. Importante: Use cores!


c = ('\033[m',  # 0 - Sem cores
     '\033[0;30;41m' # 1 - Vermelho
     '\033[0;30;42m' # 2 - Verde
     '\033[0;30;43m' # 3 - Amarelo
     '\033[0;30;44m' # 4 - Azul
     '\033[0;30;45m' # 5 - Roxo
     '\033[0;30'     # 6 - Branco
     )

def ajuda(coman):
    titulo(f"Acessando o manual do comando \'{coman}\'", 4)
    print(c[6],end='')
    help(coman)
    print(c[0], end='')

def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print("~" * tamanho)
    print(f" msg")
    print("~" * tamanho)
    print(c[0], end='')


# Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)

titulo("Até logo", 1)