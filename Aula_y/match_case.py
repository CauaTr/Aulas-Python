dia_semana = input('Dia da semana: ')

match dia_semana.lower():
    case 'segunda' | 'terça' | 'quarta' | 'quinta' | 'sexta':
        print('Dia Útil')

    case 'sábado' | 'sabado' | 'domingo':
        print('Fim de Semana')

    case _:
        print('Erro! Texto Inválido!')