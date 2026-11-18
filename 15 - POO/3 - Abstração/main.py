# Abstração: Processo de identificar apenas os atributos e métodos essenciais de um objeto, ocultando detalhes desnecessários.
# Vantagens: 1 - Maior Legigibilidade: facilita a compreensão do código, pois foca apenas nos aspectos relevantes do objeto. 2 - Padronização: permite criar interfaces consistentes para diferentes classes, facilitando a interação entre elas. 3 - Redução de Complexidade: ao ocultar detalhes desnecessários, torna o código mais simples e fácil de manter. 4 - Segurança: protege os dados sensíveis, expondo apenas o que é necessário para o funcionamento do objeto.
# Abstração de dados: Acontece quando ignoramos informações desnecessárias para o escopo do projeto.
# Abstração de processos: Acontece quando não precisamos saber como um método faz seu trabalho, apenas sabemos que ele existe pela interface.

# Classe abstrata: Nunca será instanciada, já que ela será usada apenas como base para as subclasses.
# Ao definir um conjunto de métodos abstratos, dizemos que estamos criando a interface pública da classe.
# Uma classe bastrata pode ter métodos abstratos que deverão ser obrigatoriamente implementados nas subclasses.
# Mas uma classe abstrata pode ter métodos concretos se eles funcionarem da mesma maneira para todas as subclasses (DRY - Don't Repeat Yourself).

from rich import inspect

from classes import Pessoa, Aluno, Professor, Funcionario
# importando as classes Pessoa, Funcionario, Professor e Aluno dos respectivos módulos.

def main():
    a1 = Aluno("João", 20, "Engenharia", "A")
    a1.fazer_matricula()
    a1.estudar()
    inspect(a1, methods=True)
    p1 = Professor("Maria", 35, "Matemática", "Doutorado")
    p1.dar_aula()
    p1.estudar()
    inspect(p1, methods=True)
    f1 = Funcionario("Carlos", 40, "Analista", "TI")
    inspect(f1, methods=True)
    f1.fazer_aniversario()
    f1.estudar()
    inspect(f1, methods=True)

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente (não importado como módulo)
    main() # Chama a função main() para iniciar a execução do programa