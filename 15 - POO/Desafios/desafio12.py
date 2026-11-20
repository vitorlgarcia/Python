# HERANÇA E ABSTRAÇÃO
#

from abc import ABC, abstractmethod
from rich import inspect, print
import random

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca = 50): # NOVIDADE: O parâmetro "forca" passado nesse método é um objeto (instancia de uma classe com todos os seus atributos e métodos). Repare que o IF quer saber se a vida, tanto do objeto de quem atacou e tanto do alvo, são maiores do que 0. Logo, está verificando o atributo "vida" do objeto em questão.

        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))] # Dentro da lista de golpes do respectivo objeto que está atacando, é sorteado um golpe para ser atribuído à variável golpe. Repare, mais uma vez, que essa lista é descrita nas subclasses e, mesmo assim, um método dentro da classe mãe consegue puxar e apresentar. A lista que ele faz o sorteio é do objeto que está atacando.

            print(f"[blue]{self.nome}({self.vida})[/] atacou [red]{alvo.nome}({alvo.vida})[/] com um {golpe} de força {forca}") # Aqui é chamado o atributo nome do objeto em questão, passado com o parâmetro de alvo para esse método.
            alvo.receber_dano(forca) # repare que o método está sendo chamado pelo objeto "alvo" dos ataques. Assim os pontos são subtraídos dele.
        else:
            print(f"O ataque {self.nome} -> {alvo.nome} não pode acontecer")

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida = self.vida - fator
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu [red]dano de {fator}[/]")


    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Golpe de Machado", "Pulo Giratório"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {fator} pontos[/] de vida.")



class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raio de Luz", "Mágia Estática"]

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        print(f"[blue]{self.nome}[/] fez uma poção mágica e [green]recuperou {fator} pontos[/] de vida.")


def main():
    p1 = Guerreiro("Pikachu", 1000)
    p2 = Mago("Mago Negro", 2000)
    p1.atacar(p2, 800)
    p2.atacar(p1,500)
    p1.curar()
    p2.curar()

if __name__ == "__main__":
    main()