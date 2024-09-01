# Módulo com as funções de potencia e raiz quadrada

def potencia(n,elevado):
    result = 1
    for i in range(0,elevado):
        result *= n
    return result

def raizquadrada(n, elevado):
    result = n ** (1/elevado)
    return result

