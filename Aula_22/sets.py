import os
os.system('clear')

# Inicializar um conjunto vazio
conjunto = set()
print(conjunto)
print('-'*20)

# Exibindo os elementos de um set
numeros = [4, 5, 6, 7, 6, 4, 5]
print(numeros)
conjunto = set(numeros)
print(conjunto)
print('-'*20)

# add - adiciona elementos em um set()
numeros = [1, 2, 2, 3, 3, 4, 4]
conjunto = set(numeros)
print(numeros, conjunto)
conjunto.add(10)
conjunto.add(0)
print(conjunto)
print('-'*20)

# remove - remove um elemento do set se o elemento existir
conjunto = {1, 2, 3}
print(conjunto)
conjunto.remove(2)
print(conjunto)

# discard - remove um elemento de set se ele existir, se não segue o jogo
conjunto = {1, 2, 3}
print(conjunto)
conjunto.discard(8)
print(conjunto)

# ================= OPERAÇÕES ARITMÉTICAS COM CONJUNTOS ====================
# | - union() -> União de 2 conjuntos
a = {0, 1, 3, 5, 7, 9}
b = {0, 2, 4, 6, 8}
c = a.union(b)
print(a)
print(b)
print(c)