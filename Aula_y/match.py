#Estrutura de seleção: match class
#Comparações equivalentes
dia = int(input('Numero: '))

match dia:
    case 1:
        print('Domingo')

    case 2:
        print('Segunda')

    case 3:
        print('Terça')

    case 4:
        print('Quarta')

    case 5:
        print('Quinta')

    case 6:
        print('Sexta')

    case 7:
        print('Sábado')

    case _:
        print('Isso não é um número de 1 a 7...')