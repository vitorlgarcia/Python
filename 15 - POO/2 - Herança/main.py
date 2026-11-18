# Herança em Python: Trata-se de um mecanismo que permite criar uma nova classe a partir de uma classe existente, herdando seus atributos e métodos. A classe que herda é chamada de subclasse, enquanto a classe da qual se herda é chamada de superclasse.
# A herança é uma dos quatros pilares da programação orientada a objetos (POO), juntamente com encapsulamento, polimorfismo e abstração.
# Vantagens de Herança: 1 - Reutilização de código: permite que subclasses reutilizem métodos e atributos da superclasse, evitando duplicação de código. 2 - Extensibilidade: facilita a criação de novas funcionalidades sem modificar o código existente. 3 - Organização: ajuda a estruturar o código de forma hierárquica, tornando-o mais legível e fácil de manter.
# É possível que todos os módulos estejam no mesmo arquivo, mas é uma boa prática separar cada classe em seu próprio módulo para melhorar a organização e a manutenção do código.

from rich import inspect

from pessoa import Pessoa
from funcionario import Funcionario
from professor import Professor
from aluno import Aluno

# importando as classes Pessoa, Funcionario, Professor e Aluno dos respectivos módulos.

def main():
    a1 = Aluno("João", 20, "Engenharia", "A")
    a1.fazer_matricula()
    inspect(a1, methods=True)
    p1 = Professor("Maria", 35, "Matemática", "Doutorado")
    p1.dar_aula()
    inspect(p1, methods=True)
    f1 = Funcionario("Carlos", 40, "Analista", "TI")
    inspect(f1, methods=True)
    f1.fazer_aniversario()
    inspect(f1, methods=True)

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente (não importado como módulo)
    main() # Chama a função main() para iniciar a execução do programa
