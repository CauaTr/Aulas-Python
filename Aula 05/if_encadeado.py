import os
os.system("clear")
""""
# Exercícios:
# 1. Dada uma nota verificar se ela é válida ou não.
nota = float(input("Nota: "))
      #  True and True
if  nota >= 0 and nota <= 10: # 0 <= nota <= 10:
    print("Nota válida")
else:
    print("Nota inválida")


# 2. Dadas 3 notas, verificar e exibir qual é a de menor valor
import os
os.system("clear")
nota1 = float(input("Nota 1: ")) # 5
nota2 = float(input("Nota 2: ")) # 8
nota3 = float(input("Nota 3: ")) # 2

menor = nota1 

if nota2 < menor:
    menor = nota2

if nota3 < menor:
    menor = nota3 # menor -> 2

print(menor)
"""
# 3. Dadas 3 notas, calcular a média das duas maiores [verificando se as notas são válidas.]
import os
os.system("clear")

nota1 = float(input("Nota 1: ")) 
if  nota1 >= 0 and nota1 <= 10: 
    nota2 = float(input("Nota 2: "))
    if nota2 >= 0 and nota2 <= 10: 
        nota3 = float(input("Nota 3: ")) 
        if  nota3 >= 0 and nota3 <= 10:
            # Se chegou até aqui, todas as notas são validas e posso calcular a média 
            menor = nota1 

            if nota2 < menor:
                menor = nota2

            if nota3 < menor:
                menor = nota3 
            
            media = (nota1 + nota2 + nota3 - menor) / 2

            print(f"A média das duas maiores notas entre: {nota1:.2f}, {nota2:.2f} e {nota3:.2f} é {media:.2f}")


        else:
            print(f"Nota {nota3} é inválida")
    else:
        print(f"Nota {nota2} é inválida")
else:
    print(f"Nota {nota1} é inválida")