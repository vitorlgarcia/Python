# Desafio 4 - Criar uma classe livro onde é possível avançar e retroceder páginas, além de mostrar a página atual.

from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Você acabou de abrir o livro [red]{self.titulo}[/red] que tem [green]{self.paginas}[/green] páginas no total. Você está na [yellow]página {self.pagina_atual}[/yellow][/].")

    def avancar_pagina(self, quantidade=1):
        if not self.FimLivro(self.pagina_atual, quantidade, self.paginas):
            print(f"Avançando [green]{quantidade}[/green] página(s)...")
            for i in range(quantidade):
                print(f":arrow_forward: pag {self.pagina_atual+1}", end=' ')
                self.pagina_atual += 1
                sleep(0.5)
            print(f"\nVocê está na página [yellow]{self.pagina_atual}[/yellow]")

        else:
            print(f"Avançando [green]{quantidade}[/green] página(s)...")
            count = 0
            while self.pagina_atual < self.paginas:
                print(f":arrow_forward: pag {self.pagina_atual+1}", end=' ')
                self.pagina_atual += 1
                count += 1
                sleep(0.5)
            print(f"\n:warning: [red]Você avançou {count} página(s) e chegou ao final do livro![/red]")

    def FimLivro(self, pagina_atual, quantidade, paginas):
        if pagina_atual + quantidade > paginas:
            return True
        

l1 = Livro("O Senhor dos Anéis", 20)
l1.avancar_pagina(7)
l1.avancar_pagina(3)
l1.avancar_pagina(15)
l1.avancar_pagina(5)