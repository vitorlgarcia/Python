from pessoa import Pessoa # Importa a classe Pessoa do módulo pessoa.py

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)  # Chama o construtor da superclasse Pessoa
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} está fazendo matrícula no curso de {self.curso}, turma {self.turma}.")
