from pessoa import Pessoa # Importa a classe Pessoa do módulo pessoa.py

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)  # Chama o construtor da superclasse Pessoa
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} bateu o ponto no setor {self.setor}.")
