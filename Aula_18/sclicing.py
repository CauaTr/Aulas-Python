import os
os.system("clear")

# Slicing - Fatiamento de lista e string
# Vetor: Esturura com tamanho definido que armazena dados do mesmo tipo
#         0.  1.  2.  3  <== indices positivos
vetor = [23, 34, 45, 65]

# Lista: Estrutura com tamanho flexivel que armazena dados de quaisquer tipos
#           0.    1.   2.    3    4  <== indices positivos
lista = ["Edson", 51, True, 5.6, 77, ]
#         -5    -4   -3   -2     -1  <== índices negativos

# Exibir o primeiro e ultimo elemento da lista
print(lista[0], lista[-1])

import os
os.system("clear")

# manipulacao de listas
#        0. 1.  2.  3.  4.  5.  6.  7.  8.  9.  <- positivos
lista = [0, 11, 22, 33, 44, 55, 66, 77, 88, 99]
#      -10. -9. -8. -7. -6. -5. -4. -3. -2. -1. <- negativos

print(lista)
print(lista[5], lista[-3])

# Slicing - fatiamento de lista
# Sintaxe: lista[inicio, fim-1, passo]
nova_lista = lista[2:8] # inicio, fim - 1
print(lista, nova_lista)
print(lista[0:], lista)
print(lista[-8: -2])
print(lista[:])
print(lista[0:9:2])
print(lista[0:9:4])
print(lista[::1]) # a lista assume este padrao
print(lista[::-1]) # a lista assume este padrao

# slicing - Fatiamento de string
os.system("clear")
#        01234567890123456789012345678901234567890123456789
frase = "Não acredito que isso também é possível em string!"
print(frase)
print(frase[4])
print(frase[-10])
print(frase[10:20])
print(frase[:20])
print(frase[21:])
print(frase[::3])
print(frase[-20:-10:2])