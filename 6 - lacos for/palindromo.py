frase = input("Digite uma frase: ").strip()

lista = frase.upper().split()
frase = (''.join(lista))

# ao inves de usar o laço de for, daria pra usar o seguinte comando pra receber a frase ao contrario:

# frasecontraria = frase[::-1]


frasecontraria = []
# frasecontraria = ''    # se eu usar esse comando ao inves do vetor acima, não precisaria usar o join(frasecontraria), pois já formaria a string com a frase ao contrário e não ficaria um vetor de vários caracateres.
comprimento  = len(frase)
for i in range((comprimento -1), -1, -1):
    frasecontraria += frase[i]
frasecontraria = (''.join(frasecontraria))


print("O inverso de {} é {}".format(frase, frasecontraria))

if frase == frasecontraria:
    print("Temos um palindromo")
else:
    print("Não é um palíndromo!")
