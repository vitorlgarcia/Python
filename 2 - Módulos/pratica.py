import math
import random

mat = math.sqrt(9)
print(mat)

somenumber = random.randint(1, 100)
print(somenumber)

# Exercicio 12 - Porção inteira de um numero com import math
inteiro = float(input("Digite um número fracionário: "))
print("A porção inteira desse numero é {}".format(math.floor(inteiro)))

# Exercicio 13 - Catetos e valor da hipotenusa
catoposto = float(input("Digite o valor do cateto oposto "))
catadjacente = float(input("Digite o valor do cateo adjacente "))
hipotenusa = ((catoposto ** 2) + (catadjacente ** 2)) ** (1/2)
print("O valor da hipotenusa é {:.2f}".format(math.hypot(catoposto,catadjacente)))
print("hipotenusa usando formula é {:.2f}".format(hipotenusa))

# Exercicio 14 - Seno, COsseno e Tangente
angulo = float(input("Digite o angulo qualquer (em graus) "))
angulo = math.radians(angulo) # as funções matematicas do python calculam os angulos somente em radiano. Daí a necessidade de conversão de graus para radianos
print("O valor do seno é {:.2f}, do cosseno é {:.2f} e da tangente é {:.2f}.".format(math.sin(angulo), math.cos(angulo), math.tan(angulo)))

# Exercicio 15 -  sorteio de aluno
aluno1 = input("Digite o primeiro aluno ")
aluno2 = input("Agora o segundo aluno ")
aluno3 = input("Agora o terceiro aluno ")
aluno4 = input("Agora o quarto aluno ")

lista = [aluno1, aluno2, aluno3, aluno4]

print("O aluno escolhido por sorteio foi: {}".format(random.choice(lista)))


# Exercicio 16 - Escolhendo as ordens dos alunos

estudante1 = input("Digite o primeiro estudante ")
estudante2 = input("Digite o segundo estudante ")
estudante3 = input("Digite o terceiro estudante ")
estudante4 = input("Digite o quarto estudante ")

listaestudante = [estudante1, estudante2, estudante3, estudante4]

random.shuffle(listaestudante) # Sorteia o conteudo dentro da lista

print("A ordem de estudantes é: ")
print(listaestudante)
