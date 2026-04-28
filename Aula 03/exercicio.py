#Exercício.
#Dado um número, exibir o seu módulo matemático, ou seja, se for digitado um numero positivo, exibir um positivo e se for digitado um número negativo, transforma-lo em positivo e exibir

#Pedir um número pro usuário:
num = float(input('Digite um número: '))

#Verificar se o número é positivo ou negativo
if num>=0:
    print(f'O número digitado foi {num}') #Se o número for positivo, exibir apenas o número
else:
    num = num*(-1)
    print(f'O módulo do número negativo digitado é {num}')#Se o número for negativo, transforma em positivo e exibe o número5