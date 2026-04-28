#A ordem de leitura é 
#1 - not
#2 - and
#3 - or
tempo = 3
debito = True
aposentado = False

resp = tempo >= 5 and not debito or aposentado

if resp == True:
    print("Terá isenção! :]")
else:
    print("Não terá isenção! :[")