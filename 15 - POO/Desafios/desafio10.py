# HERANÇA E ABSTRAÇÃO
# Fazer uma tabela de calculo de frete de Caminhão, Drone e Moto. Caminhão só aceita frete acima de 50km e Drones não aceitam frete acima de 10km.
from abc import ABC, abstractmethod
from rich import print, inspect
from rich.table import Table

class Transporte(ABC):
    def __init__(self, distancia,):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete():
        pass


class Moto(Transporte):
    fator = 0.50 # método da classe. Sempre que for referenciado, deve ser usado a seguinte sintaxe: "Moto.fator" (classe.atributo)
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        return f"R${(self.distancia * Moto.fator):0.2f} Reais"


class Caminhao(Transporte):
    fator = 1.20 
    def __init__(self, distancia):
            super().__init__(distancia)

    def calc_frete(self):
        if self.distancia < 50:
             self.frete = 0
             return "Raio mínimo de 50km"
        else:
             return f"R${(self.distancia * Caminhao.fator):0.2f} Reais "
             

class Drone(Transporte):
    fator = 9.50
    def __init__(self, distancia):
            super().__init__(distancia)

    def calc_frete(self):
        if self.distancia > 10:
            self.frete = 0
            return "Raio máximo de 10km"
        else:
            return f"R${(self.distancia * Drone.fator):0.2f} Reais "

def main():
    dist = 25

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)] # lista que salva os valores de frete de cada transporte.
    

    tabela = Table(title="Tabela de Fretes")
    tabela.add_column("Distancia")
    tabela.add_column("Tipo de Transporte")
    tabela.add_column("Valor do Frete")

    for item in viagem:
         tabela.add_row(f"{dist}km", f"{type(item).__name__}", f"{item.calc_frete()}") # type(item).__name__ é uma sintaxe nova que retorna o nome da classe. Dentro do laço for, o item indica qual é o indice da lista viagem a ser descrita.
         
    print(tabela)

if __name__ == "__main__":
    main()