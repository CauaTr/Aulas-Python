vetor = [45, -89, 32, -12, 33]

#1 - Retorne o rimeiro elemento do vetor.
print(vetor[0])

#2 - Exiba somente os números negativos contidos no vetor.
for c in vetor:
    if c < 0:
        print(c, end=" ")
#3 - Retorne a soma dos elementos do vetor
soma = 0
for c in vetor:
    soma = soma + c
print(f"\n{soma}")

#4 - Retorne a media dos elementos do vetor
print(soma/len(vetor))

#5 - Exiba na tela os números ímpares contidnos no vetor
for c in vetor:
    if (c % 2) != 0:
        print(c, end=" ")

#6 - Que exiba na tela o primeiro e o ultimo elemento do vetor
print(f'Primeiro: {vetor[0]}\nÚltimo: {vetor[-1]}')

#7 - Que exiba os elementos cujos índices sejam pares
for c in range(0, len(vetor), 2):
    print(c, end=" ")

print()
#8 - Que peça um número ao usuário e informe se ele existe ou não
existe = int(input('\nVerificar se tem o valor: '))
if existe in vetor:
    print(f'Existe o elemento {existe} no vetor')
else:
    print(f'Não existe o elemento {existe} no vetor')
    
#9 - Que ordene os elementos do vetor
print(sorted(vetor))

