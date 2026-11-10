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
        nomeformatado = f"{self.nome.center(30, ' ')}" # Centraliza o nome do produto em uma largura de 30 caracteres, preenchendo com espaços.
        precoformatado = f"R$ {self.preco:.2f}".center(30, ' ') # Formata o preço com duas casas decimais e centraliza em uma largura de 30 caracteres, preenchendo com espaços.
        conteudo = f"{nomeformatado}\n{'-' * 30}\n{precoformatado}" # Cria o conteúdo da etiqueta, incluindo o nome do produto, uma linha de separação com 30 caracteres e o preço formatado.
        caixa = Panel(conteudo, title="Produto", width=34)

        return caixa


p1 = Produto("Camiseta", 50.00)
print(p1.etiqueta())

p2 = Produto("Calça Jeans", 120.00)
print(p2.etiqueta())