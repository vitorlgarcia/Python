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
        conteudo = f"{self.nome.center(30, ' ')}" # Centraliza o nome do produto em uma largura de 30 caracteres, preenchendo com espaços.
        conteudo += f"{'-' * 30}" # Adiciona uma linha de separação de 30 caracteres usando o caractere '-'.
        precoformatado = f"R$ {self.preco:.2f}" # Formata o preço do produto para duas casas decimais e adiciona o símbolo de moeda "R$".
        conteudo += f"{precoformatado.center(30, ' ')}" # Centraliza o preço formatado em uma largura de 30 caracteres, preenchendo com espaços.
        caixa = Panel(conteudo, title="Produto", width=34) # Cria um painel com o conteúdo formatado, adicionando um título "Produto" e definindo a largura do painel para 34 caracteres.

        print(caixa)


p1 = Produto("Camiseta", 50.00)
print(p1.etiqueta())

p2 = Produto("Calça Jeans", 120.00)
print(p2.etiqueta())