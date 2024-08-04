print("Sequencia de Fibonacci")
print("-" * 20)

termo = int(input("Quantos termos você quer mostrar? "))

print("~" * 20)

iteracao = 0
fibonacci_n1 = 0
fibonacci_n2 = 1
temporario = 0 # variavel usada apenas para guardar um dos termos de fibonacci, pois ele será apagado quando houver mais uma soma
while iteracao < termo:
    print("{} -> ".format(fibonacci_n1), end="")
    temporario = fibonacci_n2
    fibonacci_n2 = fibonacci_n1 + fibonacci_n2
    fibonacci_n1 = temporario
    iteracao += 1

print("FIM")