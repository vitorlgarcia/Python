precos = ('lapis', 1.75,
          'Borracha', 2,
          'Caderno', 15.90,
          'Estojo', 25,
          'Transferidor', 4.20,
          'Compasso', 9.99,
          'Mochila', 120.32,
          'Canetas', 22.30,
          'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')  # coloca o titulo no centro (^) e com 40 caracteres
print('-' * 40)
for pos in range(0, len(precos)):
    if pos % 2 == 0:
        print(f'{precos[pos]:.<30}', end='')  # coloca a parte par da tupla (a lista) no lado esquerdo da tabela, com total de 30 caracteres sendo preenchidos por pontos
    else:
        print(f'R${precos[pos]:>7.2f}') # coloca os preços no lado direito da tabela, com 7 caracteres e duas casas depois da virgula (.2f).

print('-' * 40)