import os
os.system("cls")

#Pede a idade do usuário
idade = int(input('Digite a sua idade: '))

#Retorna uma resposta com base na idade
if idade<18:
    print('Sinto muito, você é novo de mais para acessar esse serviço!')
else:
    print('Idade confirmada, seja bem vindo!')