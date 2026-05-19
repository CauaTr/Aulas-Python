import os
os.system("clear")

# subalgoritmo - procedimento e função
# procedimento - executa uma rotina e não retorna valor ao programa ser chamado
    # - pode conter print e input
# função - executa uma rotina e retorna valor no programa chamador
    # - NUNCA use print e input

# Construção dos subalgoritmos

# Procedimentos - não retorna valor

def saudacao() -> None: # precisa definir o que é
    print("Bom dia, Ana")

def saudacao2(usuario: str) -> None: # parametro/argumento - informação que trafega entre os códicos, não é uma variável, para calcular algo
    print(f"Bom dia, {usuario}")

def saudacao3(usuario: str, hora: int) -> None: # parametro formal, o que ele espera. Assinatura da função
    if hora < 12:
        msg = "Bom dia" # variavel local
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"
    print(f"{msg}, {usuario}")

# Funções - retorna valor
#                  1          2          3
def calcular_delta(va: float, vb: float, vc: float) -> float:
    delta = vb * vb - 4 * va * vc
    return delta # -8

def verificar_maior_2n(n1: float, n2:float) -> float:
    if n1 > n2:
        return n1
    else:
        return n2

# Programa principal
saudacao3("Vania", 15) # isolado em uma linha

a = 1
b = 2
c = 3
resp = calcular_delta(a, b, c) # acompanhada de uma atribuição
print("Delta = ", resp)
print("Delta = ", calcular_delta(-1, 2, 3)) # acompanhada de um print
num1 = 454
num2 = 99
print(f"O maior numeros entre {num1} e {num2} é {verificar_maior_2n(num1, num2)}")