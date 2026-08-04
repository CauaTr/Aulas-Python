# ---- SUBALGORIMTOS ENCADEADOS
# Função Pai
def calcular_media(n1: float, n2: float) -> float:

    # Função Filho
    def verificar_nota(n: float) -> float:
        # Corpo função Filho
        return n >= 0 and n <= 10
    
    # Corpo função Pai
    if verificar_nota(n1) and verificar_nota(n2):
        return (n1 + n2) / 2
    else:
        return -1
import os
os.system("clear")
# Uso
media = calcular_media(3,-4)
if media == -1:
    print("Nota(s) inválida(s)!")
else:
    print("Media: ", media)