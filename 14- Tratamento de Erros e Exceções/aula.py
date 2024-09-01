# Assim como a maioria das linguagens de programação, o Python trabalha com o tratamento de erros. Uma alternativa bem conhecida são os comandos "Try" e "Exception".

# Até o momento sempre demos comandos imperativos através dos comandos Python (Se numero menor que 10, faça isso!) ou (Enquanto n maior que 5, faça isso!) ou (Print tal valor!).

# As mensagens de erro serão tratadas como tentativas -> Tente esse comando: ...    Exceção: ...

# EXEMPLO:

try:  # o comando tente: Aqui o usuario vai tentar fazer a divisão de dois numeros. Lembrando que os numeros precisam ser inteiros e não é aceito número em extenso (escritos com letras. ex: um, dois, tres...) e também divisão por 0 é um erro na matemática.
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b

except: # A exceção: Aqui é feito o tratamento do erro. Se o usuário digitou um número usando letras ou se a divisão foi por zero, por exemplo. Ao invés do programa travar e aparecer mensagem de erro igual nos exercicios anteriores, o erro será tratado. Nesse caso apenas será printado que houve um erro no código.
    print("Erro no código")

else: # Agora, caso não ocorreu nenhum erro, o resultado da divisão é apresentado na tela.
    print(f"O resultado é {r:.1f}")

finally: # Comando opcional. Caso seja colocado no programa, ele será implementado independente do "except" ou "else" serem rodados. 
    print("Obrigado e volte sempre!")


# ----------------------------------------------------------------------------------------------------


# O tratamento do erro no except vai muito alem de um print do erro. Pode-se usá-lo para especificar quais são os tipos de erros apresentados no python e o comando ainda pode ser implementado mais de uma vez dentro do programa. Tudo para especificar os diversos erros possíveis de acontecer. Ex:

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b

except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que vocẽ digitou. ") # erro nos tipos de dados

except ZeroDivisionError:
    print("Não é possível dividir um número por zero! ")

except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados!") # erro na ausencia de dados

except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}") # Apresenta o erro do jeito que o sistema escreve

else:
    print(f"O resultado é {r:.1f}") # Se nenhum erro for detectado, o comando normal é executado

finally:
    print("Volte sempre! Muito obrigado!") # Comando que vai ser executado no final de qualquer forma

