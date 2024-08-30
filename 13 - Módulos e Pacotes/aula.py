# aula sobre módulos e pacotes.

# Um módulo seria uma ou mais funções no qual posso salvar em um arquivo python separado e importá-lo usando o comando "import" igual já é feito com módulos e pacotes pré-criados no python.

# nesse exemplo é criado um módulo em um arquivo python separado, chamado de "uteis.py". Nele será colocado funções criadas. Nesse arquivo "aula.py" será usado o comando import para importar uteis.py e as funções desse arquivo serão chamadas e rodadas no presente arquivo.

import uteis  # módulo criado por mim mesmo
from matematica import potencia, raizquadrada # módulo matematica criada por mim e funções potencia e raizquadrada chamadas de forma específica


num = int(input("Digite um valor: "))
fat= uteis.fatorial(num)
dob = uteis.dobro(num)
trip = uteis.triplo(num) 
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {dob}")
print(f"O triplo de {num} é {trip}")

numer = int(input("Digite um novo número: "))
elevad = int(input("Numero da potencia a ser elevado: "))
power = potencia(numer, elevad)  # REPARE que aqui não precisei chamar a função potencia como "matematica.potencia(), pois eu importei essa função de forma específica dentro do módulo "matematica.py"
print(f"O numero {numer} elevado a {elevad} é igual a {power}")

print(f"A raiz {elevad} de {numer} é igual a {raizquadrada(numer,elevad)}") # mais uma vez não foi necessário chamar a função como "matematica.raizquadrada()" porque ela foi importada de forma específica junto com a função "potencia".

# ----------------------------------------------------------------------------------------------------

# PACOTES EM PYTHON

# Quando a quantidade de módulos a serem importadas se tornar muito grande, é recomendável o uso de pacotes (ou bibliotecas). Em Python é comum ser chamado de pacotes. Uma vez que cada arquivo.py é possivelmente um módulo python, cada pasta que contem arquivos py podem ser pacotes.

# Nos PACOTES (Pastas) estão contidos vários MÒDULOS (arquivos python).
# Para uma Pasta ser validada como PACOTE, é necessário que exista um arquivo chamado "__init__.py" contida na pasta em questão.

# É possível existir hierarquia de pacotes, como por exemplo:

# -> PACOTE (principal) (contem o __init__.py)
#   -> DADOS (pacote com várias funções de manipulação de dados dentro do arquivo __init__.py)
#   -> MATH (pacote que pode existir várias funções de matematica dentro do arquivo o __init__.py)
#   -> STRINGS (pacote que pode existir varias funções de manipulação de strings dentro do __init__.py)
#   -> CORES (pacote que pode existir varias funções de manipulação de cores dentro do __init__.py)

from pacote import dados # importando os módulos do pacote dados que está embutido no pacote de nome "pacote"

number = int(input("Digite um terceiro numero: "))
elevar = int(input("Numero da potencia ou raiz: "))
resultado2 = dados.raizquadrada(number, elevar)
print(f"A raiz {elevar} de {number} é igual a {resultado2}")
print(f"Por sua vez, {number} elevado a {elevar} é igual a {dados.potencia(number, elevar)}")