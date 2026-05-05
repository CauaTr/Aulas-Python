# SUBALGORITMO: Procedimento e função
# Procedimento: Executa uma rotina e não retorna valor ao programa chamador
# Função: Executa uma rotina e retorna valor ao programa chamador


#Criação da função

# ---------- Criação da função
def varificar_maior_3n(n1: int, n2: int, n3: int) -> int:
    maior = n1
    if n2 > maior:
        maior = n2

    if n3 > maior:
        maior = n3
    
    return maior


# ---------- Programa Principal
num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
num3 = int(input('Numero 3: '))

maior = num1
if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

resp = varificar_maior_3n(num1, num2, num3)

print("Maior: ", resp)