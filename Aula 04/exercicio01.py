#Pede o valor da compra pro usuário
compra = float(input("Valor da compra: R$"))

#Armazena o valor do desconto e do valor da compra com desconto
desconto = 0
desc_compra = 0

#Verifica qual desconto deve ser aplicado e calcula o valor com desconto
if compra > 1000:
    desconto = 10
    desc_compra = compra - compra * 0.10

elif compra <=1000 and compra >= 500:
    desconto = 5
    desc_compra = compra - compra * 0.05

else:
    desconto = 0
    desc_compra = compra

#Retorna todos os valores pro usuário
print(f'Valor da compra: R${compra:.2f}\nValor do desconto: {desconto}%\nValor final: R${desc_compra:.2f}')