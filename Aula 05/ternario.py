#Ternário: Condição composta (if else) onde só aceita uma instrução no lado verdade e outra no falso.
# Pode servir como calculo

#Sintaxe:
#[variavel = ] instrução True if condição else instrução False

salario = 10000

#maior 500 -> 10% | até 5000 -> 5%
inss = salario *0.1 if salario > 5000 else salario *0.05

print(salario,inss)



idade = int(input("Idade: "))

if idade >= 18:
     print("Maior de idade")
else:
     print("Menor de idade")

print("Maior de idade") if idade >= 18 else print("Menor de idade")