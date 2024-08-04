frase = "Curso em Video Python"

# Python trata o array dentro da variavel frase como um vetor com cada caracter sendo um elemento do indice. Assim como todas as linguagens de programação, o índice começa no 0.

print(frase[:9]) # printa o inicio da frase até o caractere do indice 8 (sempre um abaixo no numero digitado)
print(frase[4:]) # printa o caractere de indice 4 até o ultimo caractere da string
print(frase[2:15:2]) # printa o caractere de indice 2 até o de numero 14 pulando de 2 em 2

print(len(frase)) # imprime o comprimento da frase, ou seja, a quantidade de indices que a variavel possui

print(frase.count('o')) # Imprime a quantidade de vezes que a letra "o" apareceu dentro do objeto frase
print(frase.count("o", 0, 13)) # Imprime a quantidade de vezes que a letra "o" apareceu entre os indices 0 e 12.

print(frase.find('deo')) # Imprime em qual indice dentro da string frase é encontrado a expressao "deo". Se essa expressão não existir na string, é retornado o valor -1

expressao = 'Curso' in frase
print(expressao) # variavel expressao guarda o valor lógico da procura da expressao "Curso" dentro da string. Se essa expressão existe dentro da string, é retornado True. Caso não, retornado False.

print(frase.replace("Python", "Android"))

print(frase.upper()) # coloca todas as letras em maiusculo
print(frase.lower()) # Coloca toddas as letras em minúsculo
print(frase.capitalize) # Coloca as iniciais de cada palavra em maiúsculo
print(frase.title()) #Colo cas iniciais das palavras em maiúsculo também (essa é preferivel)

# frase.strip()     # Remove espaços em branco no inicio e no final de cada string (Se houver). A primeira letra da primeira palavra passa para o índice 0

# frase.lstrip()   # É uma variação do método strip(), onde somente o lado esquerdo (inicio) da string que tenha espaços em branco são apagados.


print(frase.split())  # separa as palavras de uma string usando como referencia algo que é escrito dentro do parenteses do split. Quando não há nada (como nesse caso), são considerados os espaços o divisor de cada palavra. Se, por exemplo, o comando fosse "split(",")", a VIRGULA seria o divisor das palavras.

# o split() cria uma lista onde cada palavra da string que foi separada se torna um índice da lista.

lista = frase.split()
print('-'.join(lista)) # Após uma lista ser formada atraves das palavras separadas pelo split(), o método join() une novamente os índices em uma só string usando o sinal determinado. Nesse caso o sinal desejado foi o tracinho "-"

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.""") # Usando o print com três aspas, o comando print gera uma frase do jeito que foi escrito no comando.


# IMPORTANTE: Observe que a "variável" frase é, na verdade, um objeto. Quando um array de palavras é escrito dentro de uma "variável", ele vira um objeto (POO). Por isso o objeto frase consegue ser usado com os métodos e atributos (Ex: frase.split() é um objeto trabalhando com um método). Outros exemplos: frase.title(), frase.upper(), etc.

