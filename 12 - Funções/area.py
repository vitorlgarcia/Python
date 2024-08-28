# Crie um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, alt):
    calcarea = larg * alt
    print(f"A área de um terreno {larg}x{alt}m é de {calcarea}m2")

print("Controle de Terrenos")
print("-" * 40)
largura = float(input("LARGURA (m): "))
altura = float(input("COMPRIMENTO: (m): "))
area(largura, altura)