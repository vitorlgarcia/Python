# Faça um programa que tenha uma função notas() que pode receber varias notas de alunos e vai retornar um dicionário com as seguintes informações: 1) Quantidade de notas, 2) a maior nota, 3) A menor nota, 4) A média da turma, 5) a situação (opcional)

def notas(*grades, sit=False):
    maior = 0
    menor = 0
    total = 0
    aluno = dict()
    for i in range(0, len(grades)):  # laço de for que vai de 0 até o comprimento da tupla grades
        if i == 0:  # inicializa as variaveis "maior" e "menor" com o valor do indice 0 de grades
            maior = grades[i]
            menor = grades[i]
        
        if grades[i] > maior:  # se o conteudo do indice de valor igual a i for maior que "maior"
            maior = grades[i]  # a variável "maior" recebe esse valor do indice da tupla grades
        
        if grades[i] < menor:
            menor = grades[i]
        
        total += grades[i]
    
    aluno['total'] = len(grades)
    aluno['maior'] = maior
    aluno['menor'] = menor
    aluno['media'] = total / len(grades)

    if sit == True:
        if aluno['media'] < 5:
            aluno['situacao'] = "RUIM"
    
        elif aluno['media'] < 7:
            aluno['situacao'] = "REGULAR"
    
        else:
            aluno['situacao'] = "BOA"
    
    return aluno
    


resp = notas(5.5, 6.3, 10, 6.5, 3.5, sit=True)

print(resp)