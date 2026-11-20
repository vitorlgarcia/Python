# Herança e Abstração.
# Desafio 8: Implementar o cálculo de perímetro e área de um polígono, dado o número de lados dele.

from abc import ABC, abstractmethod
import math # para usar o pi nos cálculos de perímetro e área do círculo

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, valor_lado = 1): # Repare que no método construtor da subclasse Quadrado só foi exigido o valor dos lados do quadrado. Portanto, ao instanciar um objeto, só é necessário escrever qual é o valor, em milímetros, dos lados do quadrado. Veja, então, que não é necessário pedir a variavel "qtd_lados", uma vez que ela não será exigida na hora de instanciar um objeto no "main". O valor 1 é padrão. Se não for enviado valor, fará o cálculo com 1mm.
        super().__init__(4) # Como um quadrado possui quatro lados, o método construtor que instancia a classe mãe já menciona os 4 lados que um quadrado deve ter. 
        self.lado = valor_lado

    def perimetro(self):
        return self.qtd_lados * self.lado
        
    def area(self):
        return self.lado * self.lado


class Circulo(Poligono):
    def __init__(self, valor_raio = 1):
        super().__init__(0)
        self.raio = valor_raio

    def perimetro(self):
        return 2 * math.pi * self.raio
        
    def area(self):
        return math.pi * self.raio ** 2
    

def main():
    q1 = Quadrado(20)
    q1.perimetro()
    print(f"O perímetro de um quadrado de lados de {q1.lado}mm é {q1.perimetro()}mm")
    q1.area()
    print(f"A área de um quadrado de lado {q1.lado}mm é igual a {q1.area()}mm²")

    c1 = Circulo(3)
    c1.perimetro()
    print(f"O perímetro de um Círulo de raio de {c1.raio}mm é {c1.perimetro():.2f}mm")
    c1.area()
    print(f"A área de um Círculo de raio {c1.raio}mm é igual a {c1.area():.2f}mm²")

if __name__ == "__main__":
    main()