import os
os.system("cls")

#        0   1   2   3   4   5   6   7   8   9
lista = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
#      -10  -9  -8  -7  -6  -5  -4  -3  -2  -1


#Manipulação de listas pelo índice
print(lista)
print(lista[4], lista[-6])

#SLICING - Fatiamento de Lista
#Sintaxe: lista[inicio, fim -1, passo]
print(lista[3:7])
print(lista[-8:-2])

os.system("cls")
#Exibir o primeiro e o último elemento
print(lista[0],lista[-1])
print(lista[0:])
print(lista[:5])
print(lista, lista[:])
print(lista[0:-1:2])
nova_lista = lista[0:-1:3]
print(lista, nova_lista)
print(lista[::-1])

os.system("cls")
#String - Slicing
#        01234567890123456789012345678901234567890123456
frase = "Não acredito que isso funciona com string tabém"
print(frase)
print(frase[10])
print(frase[-30])
print(frase[10:20])
print(frase[-20:-10])
print(frase[::-1])

os.system("cls")
texto = "Python"
texto = texto[:2] + "x" + texto[3:]
print(texto)

os.system("cls")
#Medotodos de strings
nome = "Edson de Oliveira"
print(nome.upper()) #Todas as letras ficam maiusculas
print(nome.lower()) #Todas as letras ficam minusculas
print(nome.title()) #As primeiras letras de cada palavra ficam maiusculas
print(nome.capitalize()) #Primeira letra da String em maiusculo

os.system("cls")
nome = "      Edson de Oliveira       "
print('|' + nome + '|', len(nome),'caracteres')

novo = nome.strip()
print(f'|{novo}| {len(novo)}, caracteres')

novo = nome.lstrip()
print(f'|{novo}| {len(novo)}, caracteres')

novo = nome.rstrip()
print(f'|{novo}| {len(novo)}, caracteres')

os.system("cls")
frase = "Aprendendo a manipular strings"
print(frase)
new1 = frase.replace('e',"E")
print(new1)
new2 = frase.replace('manipular', '*****')
print(new2)
new3 = frase.replace('n','N')
print(new3)

os.system("cls")
texto = "O split() divide a string para um lista pelo argumento passado"
print(texto)
print(texto.split(), len(texto.split()), "partes") #Quebra o texto a partir dos espaços
print(texto.split('p'), len(texto.split('p')), "partes") #Quebra o texto a partir do valor entre parenteses
print(texto.split('uma'), len(texto.split('uma')), "partes")

os.system("cls")
linguagens = ['Python', 'C', 'Java', 'JavaScript']
print(linguagens)
print('|'.join(linguagens))

os.system("cls")
texto = "Programação em Python em Fiap"
print(texto.find('em'))
print(texto.find('gra', 10, 20))
print(texto.find('Edson')) #O 'find' retorna -1 se não encontrar o valor requisitado


os.system("cls")
texto = "Programação em Python na Fiap"
print(texto.count('o')) #Conta a ocorrencia do valor requisitado
print("Edson de Oliveira".count("de"))

os.system("cls")
texto = "Python"
print(texto.startswith("cs"))
print(texto.startswith("Py"))
print(texto.startswith("py"))

texto = "Relatório.pdf"
print(texto.endswith(".pdf"))
print(texto.endswith(".docx"))

os.system("cls")
texto = "1234"
print(texto.isdigit())
texto = "a1234"
print(texto.isdigit())
texto = "-1234"
print(texto.isdigit())

os.system("cls")
texto = "1234"
print(texto.isalpha())
texto = "abc"
print(texto.isalpha())
texto = "python!"
print(texto.isalpha())

os.system("cls")
texto = "1234"
print(texto.isalnum())
texto = "abc"
print(texto.isalnum())
texto = "python!"
print(texto.isalnum())