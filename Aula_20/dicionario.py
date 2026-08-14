import os
os.system("cls")


def numero(dic: dict) -> None:
    print(len(dic))

def exibir(dic: dict) -> None:
    for c,v in dic.items():
        print(f'{c.title()}: {v}')


aluno = {
    'nome' : 'Edson de Oliveira',
    'idade' : 44,
    'curso' : 'TDS'
}

numero(aluno)
exibir(aluno)