from lib.interface import *

def arquivoexiste(nome): # Função feito para analisar se um arquivo existe ou não. Ele simplesmente abre um arquivo passado como parâmetro.
    try:
        arquivo = open(nome, 'rt') # 'rt' significa "read text" dentro da função open() já existente no python. Essa função abre um arquivo passado como parametro e abre o mesmo.
        arquivo.close() # Comando para fechar o arquivo aberto
    except FileNotFoundError: # Essa exceção trata do erro de arquivo que não foi encontrado. Então se o arquivo passado como parâmetro não existir, é retornado False.
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+') # aqui "wt+" significa "write text" (escrever no txt). Se o arquivo não existir, o sinal de + indica que o arquivo com o mesmo nome passado pelo parâmetro será criado
        arquivo.close()
    except:
        print("Houve um ERRO na criação do arquivo!")
    
    else:
        print(f"Arquivo {nome} criado com sucesso!")

def lerarquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabecalho("Pessoas cadastradas")
        for linha in arquivo:  # laço de for dentro do arquivo txt. A variavel (lista) "dado" vai receber cada cadastro, separando o nome da idade em cada indice da lista.
            dado = linha.split(";") # A separação do nome e numero é feita pelo (;) que divide cada informação.
            dado[1] = dado[1].replace('\n', '')
            print(f"{dado[0]:<30}{dado[1]:>3} anos") # é colocado 30 caracteres de espaço e o nome fica logo no inicio. É dado 3 caracteres de espaço e a idade fica no final
        print(arquivo.read())
    finally:
        arquivo.close()

def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        arquivo = open(arq, 'at')
    except:
        print("House um erro na abertura do arquivo!")
    else:
        try:
            arquivo.write(f"{nome};{idade}\n")
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print(f"Novo registro de {nome} adicionado")
    
    finally:
        arquivo.close()