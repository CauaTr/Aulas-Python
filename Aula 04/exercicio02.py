#Requisita uma nota pro usuário
nota = float(input('Digite a nota: '))

#Verifica se a nota é válida
if nota < 0 or nota > 10:
    print("Erro! Nota Inválida!")
else:
    print("Nota válida!")