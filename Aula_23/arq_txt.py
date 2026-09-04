'''
MODOS DE ABERTURA
-----------------
'w' | write (escrever) - grava e um arquivo (sobregrava se existir)
'r' | read (ler) - abre o arquivo para leitura
'a' | append - abre o arquivo em modo de edição
'x' | gravação - Grava se o arquivo não existir
'+' | Efetua gravação e leitura juntos

função open() - abre um arquivo
Sintaxe:
<objeto> = open(<nome_arquivo>, <modo_abertura>, ...)

write() -> Método que grava informações no arquivo
close() -> Método que fecha o arquivo
read() -> Lê o arquivo a partir do cursor

'''
import os
os.system('cls')

# GRAVAÇÃO EM UM ARQUIVO
arquivo = open("Arq01.txt", 'w', encoding='utf-8')
arquivo.write('Primeira Linha! Que emoção!\n')
arquivo.write('Segunda Linha! Que beleza!\n')
arquivo.close()
print('Arquivo gravado com sucesso!')

#LÊ UM ARQUIVO
os.system('cls')
arquivo = open("Arq01.txt", 'r', encoding='utf-8')
print('-' * 30)
print(arquivo.read().strip())
print('-' * 30)
arquivo.close()

#EDITA UM ARQUIVO
arquivo = open("Arq01.txt", 'a', encoding='utf-8')
arquivo.write('Nova linha!\n')
arquivo.close()
print('Arquivo editado com sucesso!')

#GRAVA EM UM ARQUIVO INÉDITO
os.system('cls')
arquivo = open("Arq02.txt", 'x', encoding='utf-8')
arquivo.write('Nova linha!\n')
arquivo.close()
print('Arquivo editado com sucesso!')