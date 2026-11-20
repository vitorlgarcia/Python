# HERANÇA E ABSTRAÇÃO
# Calcular o salário de um trabalhador horista e mensalista, tomando os descontos do INSS. Salario minimo e o percentual de INSS já foram definidos inicialmente.

from abc import ABC, abstractmethod
from rich import inspect, print
from rich.panel import Panel

class Funcionario(ABC):
    sal_min = 1612
    desconto_inss = 7.5
    def __init__(self, nome = None):
        self.nome = nome
        self.salario_bruto = 0 
        self.salario = 0

    @abstractmethod
    def calc_salario(self):
        pass

    def analisar_sal(self):
        base = self.salario / Funcionario.sal_min
        mensagem = f"O salário de [blue]{self.nome}[/] ({self.__class__.__name__}) é de R$[green]{self.salario:.2f}[/] e corresponde a [yellow]{base:.1f} salários mínimos[/]" # percebi que, mesmo o atributo self.salario não sendo declarado na classe mãe (somente declarado na classe filha), ele pode ser chamado em um dos métodos da classe mãe normalmente.
        # "self.__class__.__name__" chama o nome da classe

        painel = Panel(mensagem, title="Análise de Salário", width=50)
        print(painel)
        

class Horista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, qtd_horas = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = qtd_horas
        self.salario_bruto = self.valor_hora * self.horas_trabalhadas

    def calc_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.desconto_inss / 100)


class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto = Funcionario.sal_min):
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    def calc_salario(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.desconto_inss/100)


def main():
    f1 = Horista("Jose",12, 190)
    f1.calc_salario()
    f1.analisar_sal()

    f2 = Mensalista("Joana", 7500)
    f2.calc_salario()
    f2.analisar_sal()

if __name__ == "__main__":
    main()