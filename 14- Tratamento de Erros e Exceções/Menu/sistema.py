from lib.interface import * # Do módulo interface que está dentro da pasta lib, importe todas funções. Fazendo a importação desse modo, não é necessário chamar a função cabecalho como "lib.interface.cabecalho()"
from lib.arquivo import * # Do módulo arquivo que está dentro da pasta lib, importe todas funções.
from time import sleep


cabecalho("SISTEMA ARQUIVO V1.0")

arq = 'cursoemvideo.txt'

if arquivoexiste(arq):
    lerarquivo(arq)
else:
    print("Arquivo não encontrado!")
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção para listar o conteudo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabecalho("NOVO CADASTRO")
        nome = input("Nome: ")
        idade = leiaint("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[31mERRO! Digite um opção válida!\033[m")
    sleep(2)
