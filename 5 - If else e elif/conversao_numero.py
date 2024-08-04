numero = int(input("Digite um número qualquer em decimal: "))

print('''Escolha uma das bases para conversão?
[ 1 ] para Binário
[ 2 ] para Octal
[ 3 ] para Hexadecimal''')

opcao = int(input("Sua opção: "))

if opcao == 1:
    print("\033[0;32m{} convertido para BINÁRIO é igual {}\33[m".format(numero, bin(numero)))

elif opcao == 2:
    print("\033[0;32m{} convertido para OCTAL é igual a {}\33[m".format(numero, oct(numero)))

elif opcao == 3:
    print("\033[0;32m{} convertido para HEXADECIMAL é igual a {}\33[m".format(numero, hex(numero)))

else:
    print("\033[0;31mTente novamente!\033[m")