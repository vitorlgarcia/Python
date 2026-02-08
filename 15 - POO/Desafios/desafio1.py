# Desafio 1 - crie uma classe Funcionario com os atributos nome, setor e cargo. Crie um método apresentacao que retorne uma string formatada apresentando o funcionário. Em seguida, crie dois objetos da classe Funcionario e chame o método apresentacao para cada um deles.

from rich import print # Importa o print da biblioteca rich para impressão formatada. Certifique-se de que a biblioteca rich está instalada via pip (pip install rich)

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentacao(self):
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa Curso em Video."
    

c1 = Funcionario("Vitor", "TI", "Analista de Suporte")
print(c1.apresentacao())

c2 = Funcionario("Maria", "Recursos Humanos", "Gerente de RH")
print(c2.apresentacao())