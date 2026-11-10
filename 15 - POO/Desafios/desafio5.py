# Desafio 5 - Fazer uma tabela de jogos favoritos de um jogador, com o nome real e o nick do jogador. A tabela deve ser exibida em ordem alfabética dos jogos favoritos.

from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def adicionar_favorito(self, jogo):
        self.favoritos.append(jogo) # acrescenta o jogo à lista de favoritos do jogador.
        self.favoritos = sorted(self.favoritos, key=str.lower) # inicialmente eu coloquei self.favoritos.sort() mas o sort() não coloca em ordem alfabética se mesclar letras maísculas e minúsculas e não aceita o argumento key. Então eu usei sorted() que retorna uma nova lista ordenada e atribuí a self.favoritos. O argumento key indica que a chave escolhida para a ordenação é a própria string convertida para minúscula, garantindo uma ordenação alfabética correta independentemente do caso das letras.

    def ficha(self):
        if len(self.favoritos) == 0:
            print(f":warning: [red]Você não tem jogos favoritos ainda![/red]")
        else:
            conteudo = f"Nome real: [green]{self.nome}[/green]\n" # o conteúdo é uma string que vai armazenar as informações. Na primeira vez que for usada, é usado o operador de atribuição simples (=) para criar a variável e atribuir o valor inicial. Nas próximas vezes, é usado o operador de adição e atribuição (+=) para concatenar novas informações à string existente.
            conteudo += f"Jogos favoritos: \n"
            for jogo in self.favoritos:
                conteudo += f" :video_game: [blue]{jogo}[/blue]\n"

        print(Panel(conteudo, title=f"Jogador: {self.nick}", width=34))


j1 = Gamer("Jose", "hulk42045")
j1.adicionar_favorito("GTA VI")
j1.adicionar_favorito("EA FC 27")
j1.adicionar_favorito("Tomb Raider")
j1.adicionar_favorito("american Truck Simulator")
j1.ficha()