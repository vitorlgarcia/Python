# O rich é uma biblioteca Python para impressão formatada no terminal, que suporta cores, estilos de texto, tabelas, painéis e muito mais.

from rich import print # Importa o print da biblioteca rich para impressão formatada. Certifique-se de que a biblioteca rich está instalada via pip (pip install rich)
from rich.panel import Panel # Importa a classe Panel da biblioteca rich para criar painéis formatados.
from rich.text import Text # Importa a classe Text da biblioteca rich para manipulação avançada de texto formatado.
from rich.table import Table # Importa a classe Table da biblioteca rich para criar tabelas formatadas.
from rich import inspect # Importa várias funcionalidades da biblioteca rich para impressão formatada, criação de painéis, tabelas e inspeção de objetos.
from rich.traceback import install # Importa a funcionalidade de instalação de traceback da biblioteca rich para melhorar a impressão de erros.

install() # Instala o traceback do rich para melhorias na impressão de erros.

caixa = Panel("[green]Esse daqui é um painel de exemplo[/] :+1:", title="Título Rich Painel", subtitle="subtitulo rich Painel", width=50, border_style="blue") # Cria um painel com borda azul, título e subtítulo e largura de 50 caracteres. O texto dentro do painel é verde e contém um emoji de polegar para cima.

print(caixa)

tabela = Table(title="Tabela de Preços") # Cria uma tabela com o título "Tabela de Preços"
tabela.add_column("Produto", justify="left", style="green", no_wrap=True) # Adiciona uma coluna "Produto" com alinhamento à esquerda, estilo verde e sem quebra de linha
tabela.add_column("Preço", justify="right", style="green") # Adiciona uma coluna "Preço" com alinhamento à direita e estilo verde.

tabela.add_row("Lápis", "R$ 1,50") # Adiciona uma linha com o produto "Lápis" e preço "R$ 1,50"
tabela.add_row("Caderno", "R$ 15,00") # Adiciona uma linha com o produto "Caderno" e preço "R$ 15,00"
tabela.add_row("Mochila", "R$ 120,00") # Adiciona uma linha com o produto "Mochila" e preço "R$ 120,00"

print(tabela)

inspect(int, all=True) # Inspeciona a classe int e imprime todos os seus atributos e métodos disponíveis usando a biblioteca rich para formatação.

def divisao (a, b):
    return a / b

divisao(10, 0) # Isso causará um erro de divisão por zero, e o rich melhorará a impressão do traceback.