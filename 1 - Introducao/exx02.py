n1 = int(input("digite um valor"))
n2 = int(input("digite outro valor"))  # Muito importante!!! Por padrão, o comando input grava os dados recebidos na forma de string (str). Necessário o comanti int() para transformar o valor em primitivo do tipo inteiro.
soma = n1 + n2

print("A some entre {} e {} é igual a {}".format(n1, n2, soma))


n3 = input("Digite qualquer coisa")
print("O tipo primitivo desse valor é ", type(n3)) #tipo primitivo nesse caso é sempre str
print("Só tem espaços? ", n3.isspace())
print("Só tem numeros maiúscos? ", n3.isupper())  #metodos is ajudam a saber o tipo de dados digitados atraves do input. Repare que, embora, o tipo primitivo seja string, os métodos is ajudam a saber o que foi digitado (se é numero, letras, letras e numeros juntos, caracteres, maiusculas, etc.)
print("Só tem letras? ", n3.isalpha())
print("Sò tem numeros? ", n3.isnumeric())
print("Contem numeros e letras? ", n3.isalnum())
