import os
os.system('cls')

try: #Rotina a ser executada
    valor1 = float(input('Valor 1: '))
    valor2 = float(input("Valor 2: "))
    resp = valor1/valor2
except ValueError as erro: #Caso ocorra uma falha
    print(erro)
except ZeroDivisionError:
    print('Não existe divisão por zero!')
except:
    print('Por todo esse universo chame o programador ou a NASA')
else: # Executa caso não tenham ocorrido falhas
    print(f'Resultado: {resp:.1f}')
finally: # Executa caso tenha ocorrido um erro ou não
    print('Obrigado por usar o nosso sistema')