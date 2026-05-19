#funções
def calcular_delta(a: float, b: float, c: float) -> float:
    return b * b - 4 * a * c

def verifica_maior(a: float, b: float) -> float:
    if a > b:
        return a
    else:
        return b

def verifica_menor(a: float, b: float, c: float) -> float:
    menor = a
    if b < menor:
        menor = b
    if c < menor:
        menor = c
    return menor

#procedimentos