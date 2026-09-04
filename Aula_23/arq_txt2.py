'''

'''
arquivo = open("Arq01.txt", 'a+', encoding='utf-8')
arquivo.write('Linha1\n')
arquivo.write('Linha2\n')
arquivo.write('Linha3\n')
print('-' * 30)
arquivo.seek(0)
print(arquivo.read().strip())
print('-' * 30)
arquivo.close()
print('Arquivo gravado com sucesso!')