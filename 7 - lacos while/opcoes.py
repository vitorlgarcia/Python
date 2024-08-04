n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

opcao = 0
while opcao != 5:
    print('''
             [ 1 ] Somar
             [ 2 ] Multiplicar
             [ 3 ] Maior
             [ 4 ] Novos Valores
             [ 5 ] Sair do programa''')
    
    opcao = int(input("Qual é a sua opção? "))

    if opcao == 1:
        print("A soma entre {} e {} é {}".format(n1, n2, (n1 + n2)))
    
    elif opcao == 2:
        print("O produto entre {} e {} é {}".format(n1, n2, (n1 * n2)))

    elif opcao == 3:
        if n1 > n2:
            print("Entre {} e {} o maior valor é {}".format(n1, n2, n1))
        elif n1 < n2:
            print("Entre {} e {} o maior valor é {}".format(n1, n2, n2))
        else:
            print("Os dois números são iguais")
    
    elif opcao == 4:
        print("Selecione novos números para continuar.")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    
    elif opcao > 5 or opcao == 0:
        print("Opção Inválida! Tente novamente...")

print("Programa finalizado...")