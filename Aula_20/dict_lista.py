import os
os.system("cls")

#Dicionário com lista
aluno = {
    "Nome" : "Ana",
    "Notas": [10, 6.5, 8.4]
}

print(aluno)
for c in aluno['Notas']:
    print(f'Nota: {c}')