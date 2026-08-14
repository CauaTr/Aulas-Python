import os
os.system("cls")

# Lista de dicionários

alunos = [
    {
        'nome' : 'Vania',
        'idade' : 55,
    },
    {
        'nome' : "Edilson",
        'idade' : 33
    }
]

aluno = {
    'nome' : '',
    'idade' : 0
}

aluno['nome'] = input('Nome: ')
aluno['idade'] = int(input('Idade: '))

print(alunos)
alunos.append(aluno)
print(alunos)

