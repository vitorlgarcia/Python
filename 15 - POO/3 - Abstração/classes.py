from abc import ABC, abstractmethod # trata-se de uma biblioteca do python para transformar as classes em abstratas, uma vez que o Python não possui isso nativamente.

class Pessoa(ABC): # Chamando a biblioteca ABC, faz com que a classe Pessoa seja abstrata. Agora ela não pode ser instanciada. Será apenas uma classe padrão em que as demais classes vão herdar características (atributos) e ações (métodos).
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self): # Obriga, à todas as classes filhas, que tenham o método estudar com as suas respectivas ações individuais. Isso faz com que todas as subclasses tenham um método em comum, porém que realize ações exclusivas de cada classe.
        pass

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)  # Chama o construtor da superclasse Pessoa
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome} está fazendo matrícula no curso de {self.curso}, turma {self.turma}.")

    def estudar(self):
        print(f"{self.nome} está estudando {self.curso} na turma {self.turma}")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)  # Chama o construtor da superclasse Pessoa
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"{self.nome} está dando aula de {self.especialidade}.")

    def estudar(self):
        print(f"{self.nome} é especialista em {self.especialidade} em nível de {self.nivel}")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)  # Chama o construtor da superclasse Pessoa
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} bateu o ponto no setor {self.setor}.")

    def estudar(self):
        print(f"{self.nome} se especializa para a área de {self.setor}")