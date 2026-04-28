#EXERCÍCIOS
#1 Dados os numeros do intervalo, exiba o intevalo aberto
#(Sem inicio e sem fim)
inicio = int(input('Início: '))
fim = int(input('Fim: '))

for c in range(inicio+1, fim, 1):
    print(c, end=" ")

#2 Dados 2 numeros do intervalo e o incremento, exiba os números de acordo
#Com os parâmetros:
#ENTRADA: 4, 20, 3  SAÍDA: 4 7 10 13 16 19

inicio = int(input('Início: '))
fim = int(input('Fim: '))
incremento = int(input('Incremento: '))

for c in range(inicio, fim +1, incremento):
    print(c, end=' ')

#3 Dados 2 numeros do intervalo, exiba somente os números ímpares do intervalo
inicio = int(input('Inicio: '))
fim = int(input('Final: '))

for c in range(inicio, fim + 1, 1):
    if (c % 2) != 0:
        print(c)