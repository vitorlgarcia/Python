# Desafio 6 - Desafio da caneta colorida. Fazer uma classe Caneta que tenha os atributos cor. A classe deve ter um método escrever que recebe um texto como parâmetro e imprime na tela o texto escrito com a cor da caneta.

import rich
from rich import print

class Caneta:
    destampada = False

    def __init__(self, cor):
        self.cor = cor

    def destampar(self):
        self.destampada = True
        print(f":pencil2: A caneta foi destampada!")

    def tampar(self):
        self.destampada = False
        print(f":pencil2: A caneta foi tampada!")

    def escrever(self, texto):
        if self.destampada:
            print(f"[bold {self.cor}]{texto}[/bold {self.cor}]")
        else:
            print(f":warning: A caneta está tampada!")

c1 = Caneta("blue")
c1.escrever("Olá, mundo!")
c1.destampar()
c1.escrever("Está é uma caneta azul")

c2 = Caneta("red")
c2.destampar()
c2.escrever("Esta é uma caneta vermelha!")
