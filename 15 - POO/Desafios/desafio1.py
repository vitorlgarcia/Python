# Desafio 1 - crie uma classe Funcionario com os atributos nome, setor e cargo. Crie um método apresentacao que retorne uma string formatada apresentando o funcionário. Em seguida, crie dois objetos da classe Funcionario e chame o método apresentacao para cada um deles.

from rich import print # Importa o print da biblioteca rich para impressão formatada. Certifique-se de que a biblioteca rich está instalada via pip (pip install rich)

class Funcionario:
    # Atributos da classe Funcionario
    empresa = "Curso em Video"  # Atributo de classe, compartilhado por todos os objetos da classe

    def __init__(self, nome, setor, cargo):
        # Atributos de instância, específicos para cada objeto da classe
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentacao(self):
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.empresa}."
    

c1 = Funcionario("Vitor", "TI", "Analista de Suporte")
c1.empresa = "Tech Solutions"  # Modificando o atributo de classe para o objeto c1. Repare que isso não afeta o atributo de classe para outros objetos da classe Funcionario.
print(c1.apresentacao())

c2 = Funcionario("Maria", "Recursos Humanos", "Gerente de RH")
print(c2.apresentacao())