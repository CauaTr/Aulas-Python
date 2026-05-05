#MÉTODOS/FUNÇÕES DE LISTAS
# list() - criar uma lista vazia
lista = []
print(lista)

# append(elemento) - adiciona um elemento na lista
lista.append("Edson")
elem = 51
lista.append(elem)
lista.append(33)
lista.append(45)
#elem = input("Elemento: ")
#lista.append(elem)
print(lista)

#insert(posicao, elemento) - adiciona um elemento em uma posição especificada da lista
lista.insert(2, "Novo")
print(lista)

#pop([posicao]) - remove o último elemento ou a [posicao], da erro se você colocar uma posição que não existe
lista.pop()
print(lista)
removido = lista.pop(2)
print(lista, removido)

#remove(elemento) - remove pelo elemento
lista = ["Edson", 51, "Novo", 33, 45]
print(lista)
lista.remove('Novo')
print(lista)

#index() - retorna o indice do elemento
lista = ["Edson", 51, "Novo", 33, 45]
indice = lista.index(51)
print(f"Índice = {indice}")

# count(elemento) - conta quantos elementos especificos existem
lista = ["Edson", 51, "Novo", 33, 45, 51, 51]
qtd = lista.count(51)
print(f'Quantidade = {qtd}')

#len(objeto) - conta quantos elementos/posicoes existem em um objeto
qtd = len("Edson de Oliveira")
print(qtd)
lista = ["Edson", 51, "Novo", 33, 45]
print(len(lista))

#sum(objeto_numerico) - soma os elementos de um 'vetor' numérico
lista = [34, 45, 64, -4, 6.6, 5.50]
somatoria = sum(lista)
print(somatoria)

#ou

somatoria = 0
for elem in lista:
    somatoria = somatoria + elem

print(somatoria)

# + - concatenacao de listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1 + lista2
print(f"Lista 1 = {lista1}")
print(f"Lista 2 = {lista2}")
print(f"Lista 3 = {lista3}")

#copy()
lista1 = [1,2,3]
lista2 = lista1
print(lista1)
print(lista2)
lista1.append(4)
print(lista1)
print(lista2)

#sort() - ordenar uma lista numerica
lista = [19, 4, 25, 33, -5]
print(lista)
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

#reverse() - inverte as posições
lista = [19, 4, 25, 33, -5]
print(lista)
lista.reverse()
print(lista)

#clear() - apaga todos os elementos
lista = [19, 4, 25, 33, -5]
print(lista)
lista.clear()
print(lista)