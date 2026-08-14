import os
os.system("cls")

#Dicionário de Dicionários
alunos = {
    "RM001": {
        "Nome" : "Edson",
        "Idade" : "55"
    },
    "RM002":{
        "Nome" : "Ester",
        "Idade" : 33
    },
}

print(alunos["RM001"])
print(alunos["RM001"]["Nome"])

for rm, dados in alunos.items():
    print(rm)
    print(dados)