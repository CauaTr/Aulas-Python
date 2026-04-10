#Variáveis do programa:
valor1 = int(input('Valor 1: '))
sinal = input('Operação: ')
valor2 = int(input('Valor 2: '))

#Match
match sinal:
    case '+':
        print(f'Resultado: {valor1 + valor2}' )

    case '-':
        print(f'Resultado: {valor1 - valor2}')

    case '*' | 'x' | 'X' | '.':
        print(f'Resultado: {valor1 * valor2}')

    case '**':
        print(f'Resutlado: {valor1 ** valor2}')

    case '/':
        if valor2 == 0:
            print(f'Resultado: Erro!')
        else:
            print(f'Resultado: {valor1 / valor2}')

    case '//':
        if valor2 == 0:
            print(f'Resultado: Erro!')
        else:
            print(f'Resultado: {valor1 // valor2}')

    case '%':
        if valor2 == 0:
            print(f'Resultado: Erro!')
        else:
            print(f'Resultado: {valor1 % valor2}')

    case _:
        print('Erro! Sinal inválido')