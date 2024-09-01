# Módulo moeda criada para ser importada dentro do arquivo principal.py. Esse módulo possui as funções aumentar, diminuir, dobro e metade.

def aumentar(valor = 0, porcent = 0, formatar = False):
    aumentado = valor * (1 + porcent/100)  # aumenta em 10% o valor inicial
    return aumentado if formatar is False else formatacao(aumentado)  # É retornado apenas o valor da variavel "aumentado" se não for passado o parametro TRUE para a variavel "formatar". Caso for passado "TRUE", é chamada a função formatacao onde apresentará o resultado com a formatação monetária exigida no brasil.


def diminuir(valor = 0, porcent = 0, formatar = False):
    diminuido = valor * (1 - porcent/100)  # diminui em 10% o valor inicial
    return diminuido if formatar is False else formatacao(diminuido) # É o mesmo retorno com condição descrito anteriormente


def dobro(valor = 0, formatar = False):
    dobrado = valor * 2  # dobra o valor inicial
    return dobrado if formatar is False else formatacao(dobrado) # É o mesmo retorno com condição descrito anteriormente


def metade(valor = 0, formatar = False):
    metade = valor/2  # reduz a metade o valor inicial
    return metade if formatar is False else formatacao(metade)

def formatacao(valor=0, moeda= 'R$'):
    return f"{moeda}{valor:.2f}".replace('.', ',')


def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',','.').strip()  # Aqui o mesmo input "Digite um preço" que aparece no programa principal é escrito novamente enquanto a variavel "valido" é False. Se o usuário digitou virgula (,) para separar inteiro da fração, o replace vai colocar ponto (.), pois é assim que o python entende a fração. E a função strip vai tirar qualquer espaço a mais (além da escrita).
        if entrada.isalpha():
            print(f"\033[0;31mErro! {entrada} é um Preço inválido\033[m")
        else:
            valido = True
            return float(entrada)

def resumo(valor, taxared, taxaaument):
    print("-"*30)
    print("RESUMO DO VALOR".center(30))
    print("-"*30)
    print(f"Preço analisado: {formatacao(valor)}")
    print(f"Dobro do preço: {dobro(valor, True)}")
    print(f"Medate do preço: {metade(valor, True)}")
    print(f"{taxaaument}% de aumento: {aumentar(valor, taxaaument, True)}")
    print(f"{taxared}% de redução: {diminuir(valor, taxared, True)}")
    print("-"*30)
