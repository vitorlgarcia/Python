# Declaração de uma classe chamada 'Pessoa'
class Pessoa:
    # Método construtor que inicializa os atributos da classe
    def __init__(self):
        self.nome = ""          # Atributo para o nome da pessoa
        self.idade = 0        # Atributo para a idade da pessoa
        self.sexo = ""          # Atributo para o sexo da pessoa


    # Método de instancia
    def aniversario(self):
        self.idade += 1  # Incrementa a idade da pessoa em 1 ano
    
    def mensagem(self):
        return f'Olá, eu sou {self.nome}, tenho {self.idade} anos e sou do sexo {self.sexo}.'
    
    
# declaração de Objeto
p1 = Pessoa()
p1.nome = "Mariazinha"
p1.idade = 26
p1.sexo = "Feminino"
p1.aniversario()
print(p1.mensagem())

p2 = Pessoa()
p2.nome = "Joãozinho"
p2.idade = 22
p2.sexo = "Masculino"
p2.aniversario()
print(p2.mensagem())