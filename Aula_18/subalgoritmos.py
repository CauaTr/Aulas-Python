#a, b e c são PARÂMETROS
def calcular_delta(a: float, b: float, c: float) -> float:
    return b ** 2 - 4 * a * c

#parâmetros default
def saudacao(nome: str, hora: int = 8) -> str:
    if hora < 12:
        msg = "Bom dia"
    elif hora < 18:
        msg = "Boa tarde"
    else:
        msg = "Boa noite"
    return f"{msg} {nome}! Seja bem-vindo(a)!"

# Parâmetros *args: Torna a quantidade de parâtros volátil
# *args vira uma lista dentro do subalgoritmo
def somar_valores(*args) -> float:
    soma = 0

    for num in args:
        soma = soma + num

    return soma



# Principal
import os
os.system("clear")
soma = somar_valores(56, 34, 33)
print("Soma: ", soma)
soma = somar_valores(56, 34, 33, 44, 3,2, 1)
print("Soma: ", soma)
soma = somar_valores(56, 34)
print("Soma: ", soma)


#1, 2 e 3 são ARGUMENTOS
#delta = calcular_delta(1, 2, 3)
#print(delta)

mensagem = saudacao("Alice")
print(mensagem)

mensagem = saudacao("Paulo", 15)
print(mensagem)