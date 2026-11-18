from pessoa import Pessoa # Importa a classe Pessoa do módulo pessoa.py

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)  # Chama o construtor da superclasse Pessoa
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"{self.nome} está dando aula de {self.especialidade}.")
