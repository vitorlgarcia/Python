from rich import print # Importa o print da biblioteca rich para impressão formatada.
from rich.panel import Panel # Importa a classe Panel da biblioteca rich para criar painéis formatados.

class Churrasco:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade
    
    def analisar(self):
        consumo = 0.4
        custo = 82.40
        comprar = self.quantidade * consumo
        preco = comprar * custo

        texto = f"Analisando [green]{self.titulo}[/] com [blue]{self.quantidade} participantes[/]\n" f"Cada participante comerá {consumo:.3f}Kg e cada Kg custa R${custo:.2f}\n" f"Recomendo comprar [blue]{consumo * self.quantidade: .2f}Kg[/] de carne\n" f"Custo total será de [green]R${preco:.2f}[/]\n" f"Cada pessoa pagará [yellow]R$ {preco / self.quantidade:.2f}[/] para participar"

        caixa = Panel(texto, title=f"{self.titulo}", width=60)
        print(caixa)

c1 = Churrasco("Churrasco de Aniversário", 15)
print(c1.analisar())