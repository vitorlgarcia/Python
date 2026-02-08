# Desafio 2: Etiqueta de Produto
# Crie uma classe Produto com os atributos nome e preco. Crie um método etiqueta que retorne uma string formatada com o nome do produto e seu preço, centralizada em um painel usando a biblioteca rich. Em seguida, crie um objeto da classe Produto e chame o método etiqueta para exibir a etiqueta do produto.

from rich import print # Importa o print da biblioteca rich para impressão formatada. Certifique-se de que a biblioteca rich está instalada via pip (pip install rich)
from rich.panel import Panel # Importa a classe Panel da biblioteca rich para criar painéis formatados.
from rich.align import Align # Importa a classe Align da biblioteca rich para alinhar o conteúdo dentro de painéis ou outros elementos.
from rich.text import Text # Importa a classe Text da biblioteca rich para manipulação avançada de texto formatado.

class Produto:
    def __init__(self,nome, preco):
        self.nome = nome
        self.preco = preco
    
    def etiqueta(self):
        texto = f"{self.nome}\n" f"{'-' * 40}\n" f"{self.preco:.2f}"
        texto_centralizado = Align.center(texto)
        caixa = Panel(texto_centralizado, title="Produto", width=50)

        print(caixa)


p1 = Produto("Camiseta", 50.00)
print(p1.etiqueta())