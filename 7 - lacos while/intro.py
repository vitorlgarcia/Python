# Verifica se o sexo é masculino ou feminino e não sai do laço enquanto o usuário confirmar

sexo = input("Informe seu sexo: [M/F]").upper().strip()[0]
print(sexo)

#  Eu fiz -> while sexo != 'M' or sexo != 'F': e Meu loop não estava parando nunca. nem colocando M ou F, achei muito estranho e demorei pra entender o motivo. A minha maneira de interpretar pra entender melhor foi a seguinte:  'Enquanto sexo for diferente de 'M' OU diferente de 'F' entre na repetição', so que 'M' sempre será diferente de 'F' e vise versa. Então se digitasse 'M' o programa testava --> 'M' é diferente de 'M' OU de 'F' ? Sim , 'M' é igual a 'M' , porém é diferente de 'F', então entre na repetição! , e se digitasse 'F' ele testava --> 'F' é diferente de 'M' OU de 'F' ? Sim, 'F' é diferente de 'M' , entre na repetição! E digitando qualquer palavra OU um OU outro sempre seriam satisfeitos, loop infinito! 

# Usando a função AND da certo porque enquanto sexo for diferente de "M" E de "F" ele entra no loop. Qualquer palavra então vai fazer ele entrar na repetição, porém se você digitar 'M' ele vai testar -> 'M' É diferente de M e F ? não, é só diferente de F e igual a M, saia da repetição.  Se colocar 'F' ele vai testar -> É diferente de M e F? não, é só diferente de M e igual a F, saia da repetição. Acho que é isso. 


while sexo != 'M' and sexo != 'F':
    sexo = input("Dados inválidos. Por favor, informe seu sexo: ").upper().strip()[0]

print("Sexo registrado com sucesso e é {}".format(sexo))


# Jeito mais facil de validar:

# while sexo not in 'MmFf':
    # sexo = input("Dados inválidos. Por favor, informe seu sexo: ").upper().strip()[0]

# print("Sexo registrado com sucesso e é {}".format(sexo))
