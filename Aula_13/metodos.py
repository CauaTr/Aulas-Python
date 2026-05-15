"""
#Sum() = Soma os elementos de uma lista se todos forem numéricos
lista = [45, 21, 24, 66, 32]
suma = sum(lista)
print(suma)

# + = Concatena listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2
print(lista1)
print(lista2)
print(lista3)

# extend - adiciona uma lista no final da outra
lista1 = [1,2,3]
lista2 = [4,5,6]
print(lista1)
print(lista2)
lista1.extend(lista2)
print(lista1)
print(lista2)

#copy() = copia um objeto sem ligar as listas
lista1 = [1,3,4]
lista2 = lista1.copy()
print(lista1)
print(lista2)
lista1.append(7)
lista2.append(8)
print(lista1)
print(lista2)

# sort() = Ordena uma lista
lista1 = [1, 34, 89, 3, 5]
lista1.sort()
print(lista1)
lista1.sort(reverse=True)
print(lista1)
lista2 = ["10", "020", "3"]
lista2.sort()
print(lista2)

#reverse() = inverte a ordem dos elementos
lista = [1, 34, "edson", 89, 3, 5]
print(lista)
lista.reverse()
print(lista)
"""
#exercicio
lista = []

while True:
    num = input('Digite um valor ("." termina): ')
    if num == '.':
        break
    else:
        lista.append(int(num))

lista_crescente = lista.copy()
lista_decrescente = lista.copy()
lista_invertida = lista.copy()

lista_crescente.sort()
lista_decrescente.sort(reverse=True)
lista_invertida.reverse()

print(f"Lista original....: {lista}\nLista crescente...: {lista_crescente}\nLista decrescente.: {lista_decrescente}\nLista invertida...: {lista_invertida}")