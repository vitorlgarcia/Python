# Segunda aula sobre funções em Python

help() # Interactive help (ajuda interativa): É uma função interna que abre um terminal python que oferece ajuda para o endentimento de diversos comandos, bibliotecas ou funções em Python. Seria uma espécie de dicionário onde você digita o que será pesquisado.

help(print) # Aqui a função a help já mostra direto na tela qual é o objetivo da função print.

# OUTRO MODO DE BUSCAR DOCUMENTAÇÃO DE UMA FUNÇÃO OU COMANDO:

print(input.__doc__)

# ---------------------------------------------------------------------------------------------------

def contador (ini, final, pulo):
# """"""                                # Docstring (documentação usada para auxiliar no comando help)
# -> Faz uma contagem e mostra na tela.                 
# :param ini: inicio da contagem.
# param final: final da contagem.
# param pulo: passo da contagem
# return: Sem retorno.
# Função criada por Vitor Garcia estudando o curso em video
# """"""
# No Visual Studio Code não está funcionando o Dosctring igual está mencionado no curso, mas, basicamente, docstring se trata de uma documentação criada pelo dono da função, onde é colocado tudo sobre a função criada. Essa documentação será puxada quando outro usuário pesquisar a função atraves do help().  Ex:  help(contador)  -> Aparecerá tudo que foi escrito entre as aspas duplas colocadas três vezes.
    c = ini
    while c <= final:
        print(f"{c}", end=" ")
        c += pulo
    print("FIM!")

contador(1, 10, 1)

# --------------------------------------------------------------------------------------------------

# PARAMETRO OPCIONAL

def somar(a=0, b=0, c=0):      # Caso não for passado nenhum parametro para a função, eles recebem automaticamente o valor zero (ou qualquer valor estabelecido via código).
    s = a + b + c
    print(f"A soma vale {s}")


somar(3, 2, 5)  # A soma vale 10
somar(8, 4) # A soma vale 12 (pois c não recebeu parâmetro e recebeu o 0 automaticamente -> Opcional)
somar() # S soma vale 0 ("a", "b" e "c" receberam valor 0 por parâmetro opcional, pois não receberam nenhum valor por parâmetro).

# ----------------------------------------------------------------------------------------------------

# ESCOPO DE VARIÁVEIS

def teste(b):
    a = 8       # dentro das funções existe o que chamamos de variáveis locais
    b += 4      # Aqui toda variável criada só existe DENTRO da função.
    c = 2
    print(f"A dentro vale {a}") # a variável "a" é local e tem o valor 8. Não é a mesma que a variável global "a" criada fora da função teste
    print(f"B dentro vale {b}") # "b" é o parametro que recebeu o numero 5 da variável global e foi somada a ela + 4, passando, então, a valer 8. Ela não existe fora da função
    print(f"C dentro vale {c}") # "c" é variavel local que tem valor 2.


a = 5 # essa já é uma variável global e existe tanto fora como dentro da função
teste(a)
print(f"A fora vale {a}") # variavel global que tem o valor 5

# Conforme já foi mencionado, a variável "a" criada fora da função e dentro da função são DISTINTAS. Para fazer com que uma variável com o mesmo nome da global seja colocada dentro da função e que a mesma seja também considerada global, é necessário escrever "global" antes dela, conforme exemplo:

def teste2(b):
    global x # variavel local é a mesma que a variavel global
    x = 7    # Passa a valer 7
    y = 2
    z = 4

x = 3 # inicialmente tem o valor 3, mas depois recebe valor 7 dentro da função.
teste2(x)
print(f"X fora vale {x}") # vale 7, uma vez que dentro da função foi considerada global e alterada de 3 para 7.


# ----------------------------------------------------------------------------------------------------

# RETORNO DE VALORES:

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f   # retorna para o programa principal uma variável trabalhada dentro da função

f1 = fatorial(5)  # variavel f1 recebe o valor que será retornado da variavel f dentro da função
f2 = fatorial(4) # Mesma coisa que f1. Porém agora o parâmetro enviado para a função é o 4.
f3 = fatorial(8) # nova variavel recebe valor do fatorial de 8.

print(f"Os resultados são {f1}, {f2} e {f3}") # Os resultados são 120, 24 e 40.320