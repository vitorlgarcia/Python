# Apresenta tabuadas que o usuário pedir e encerra o programa quando é colocado um valor negativo para listar a tabuada

numero = 0
while True:
    numero = int(input("Quer ver a tabuada de qual valor? "))
    if numero >= 0:
        print("-" * 20)
        for i in range(0,11):
            print(f"{numero} x {i} = {numero * i}")
    
    else:
        break

print("Programa de tabuada encerrado. Volte sempre!")
