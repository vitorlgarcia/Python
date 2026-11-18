class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

# Não é necessário importar a classe Pessoa aqui, pois ela já está definida neste arquivo.