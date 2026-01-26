# Aprimoramento da classe Pessoa com métodos de instancia

# Declaração de uma classe chamada 'Pessoa'
class Pessoa:
    """
    Essa classe cria um objeto do tipo Pessoa com atributos nome, idade e sexo.

    Para criar um objeto do tipo Pessoa, você pode passar os seguintes parâmetros:
    - n: Nome da pessoa (string)
    - i: Idade da pessoa (inteiro)
    - s: Sexo da pessoa (string)
    """
    # Docstring da classe Pessoa acada de ser criada.

    # Método construtor que inicializa os atributos da classe
    def __init__(self, n = "", i = 0, s = ""):
        self.nome = n          # Atributo para o nome da pessoa
        self.idade = i        # Atributo para a idade da pessoa
        self.sexo = s          # Atributo para o sexo da pessoa


    # Método de instancia
    def aniversario(self):
        self.idade += 1  # Incrementa a idade da pessoa em 1 ano

    def mensagem(self):
        return f'Olá, eu sou {self.nome}, tenho {self.idade} anos e sou do sexo {self.sexo}.'
    
    def __str__(self):
        return "Comando print aplicado ao objeto Pessoa. Assim você pode personalizar a mensagem exibida quando o objeto é impresso."
    
    def __getstate__(self):
        return f"Estado do objeto Pessoa: nome={self.nome}, idade={self.idade}, sexo={self.sexo}"
    
    
# declaração de Objeto
p1 = Pessoa("Mariazinha", 26, "Feminino")
p1.aniversario()
print(p1.mensagem())

p2 = Pessoa("Joãozinho", 22, "Masculino")
p2.aniversario()
print(p2.mensagem())


# Algumas formas de apresentar os dados dos objetos e classes.

print(p1.__doc__) # Dunder attribute: Imprime a documentação do objeto p1 da classe Pessoa. A documentação está definida na docstring da classe. Essa docstring explica como criar um objeto do tipo Pessoa e quais parâmetros são necessários. Ela foi criada no momento da definição da classe, logo após a declaração da classe, usando os três aspas duplas (""").
# Você pode acessar essa documentação usando o atributo especial __doc__ de qualquer classe usando o mesmo comando acima.

print(p1) # Dunder Method: Comando print aplicado ao objeto p1 da classe Pessoa. Assim você pode personalizar a mensagem exibida quando o objeto é impresso. # Para isso, você deve definir o método especial __str__ DENTRO da classe. Esse método retorna a string que será exibida quando o objeto for impresso.

print(p2.__getstate__()) # Dunder Method: Retorna o estado do objeto p2 da classe Pessoa. Para isso, você deve definir o método especial __getstate__ DENTRO da classe. Esse método retorna uma representação do estado atual do objeto.

print(p1.__class__) # Dunder attribute: Imprime a classe do objeto p1. O atributo especial __class__ retorna a classe à qual o objeto pertence. Nesse caso, ele retornará <class '__main__.Pessoa'>, indicando que p1 é uma instância da classe Pessoa.

print(p2.__dict__) # Dunder attribute: Imprime o dicionário de atributos do objeto p2. O atributo especial __dict__ retorna um dicionário que contém todos os atributos do objeto e seus respectivos valores. Nesse caso, ele retornará algo como {'nome': 'Joãozinho', 'idade': 23, 'sexo': 'Masculino'}, mostrando os atributos e valores atuais do objeto p2.