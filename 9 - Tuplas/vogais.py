# Vê as palavras dentro das tuplas e identifica as vogais de cada palavra

palavras = ("aprender", "aceitar", "viajar", "Compreender", "ensinar", "distinguir", "aparecer", "imprimir", "dirigir", "urubu", "promoção")

for p in palavras:
    print(f"\nNa palavra {p.upper()} temos as vogais ", end="")
    for letra in p:
        if letra.lower() in 'aeiouáàéíóúã':
            print(letra, end="")