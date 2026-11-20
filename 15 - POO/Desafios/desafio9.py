# HERANÇA E ABSTRAÇÃO
# Simulação de uma cafeteira.

from abc import ABC, abstractmethod

class BebidaQuente(ABC): #Não existe método construtor nessas classes, pois nenhuma classe recebe atributo. Apenas trabalhou-se com métodos.
    def preparar(self):
        print("--- Iniciando o Preparo ===")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("-- Bebida Pronta ---")

    def ferver_agua(self):
        print("1. Fervendo água à 100 graus Celsius ")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente): # Também não houve chamada do método construtor da classe mãe porque não trabalhamos com atributos nesse exercício. Somente métodos.
    def misturar(self):
        print("2. Passando água pressurizada pelo pó de café moído")

    def servir(self):
        print("3. Servindo em xícara pequena")

class Cha(BebidaQuente):
    def misturar(self):
        print("2. Mergulhando o sachê de ervas na água.")

    def servir(self):
        print("3. Servindo na caneca de porcelana com limão.")


class Leite(BebidaQuente):
    def misturar(self):
        print("2. Passando água pressurizada pelo bico do leite.")

    def servir(self):
        print("3. Servindo na caneca grande, já com café.")


def main():
    b1 = Cafe()
    b2 = Cha()
    b3 = Leite()

    b1.preparar()
    b2.preparar()
    b3.preparar()

if __name__ == "__main__":
    main()