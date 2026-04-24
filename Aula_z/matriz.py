matriz = [
    [10, 20, 30],
    [40, 50, 60]
]

#Percorre TODA a matriz
for linha in range(0,2,1):
    for coluna in range(0, 3, 1):
        print(matriz[linha][coluna], end=" ")
    print()

print()
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()