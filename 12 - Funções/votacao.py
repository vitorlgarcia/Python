# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATORIO nas eleições.

from datetime import datetime

def voto(anos):
    idade = datetime.now().year - anos
    if idade < 16:
        return f"Com {idade} anos: VOTO NEGADO"
    
    elif idade < 18 or idade > 60:
        return f"Com {idade} anos: VOTO OPCIONAL"
    
    else:
        return f"Com {idade} anos: VOTO OBRIGATÒRIO"



ano_nascimento = int(input("Em que ano você nasceu? "))

print(voto(ano_nascimento))