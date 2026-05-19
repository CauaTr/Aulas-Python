#Cria uma lista vazia
lista = []

# Pede elementos para o usuário até que o usuário digite '.'
while True:
    valor = input('Digite algo("." finaliza o programa): ')
    if valor == '.':
        break
    else:
        lista.append(valor)

print(f'lista = {lista}')