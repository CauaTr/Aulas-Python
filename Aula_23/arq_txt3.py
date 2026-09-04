import os
os.system('cls')

def gravar_arquivo_exclusivo(na: str, msg: str) -> bool:
    try:
        arquivo = open(na, 'x', encoding='utf-8')
        arquivo.write(msg + '\n')
    except:
        return False
    else:
        return True

# Principal
nome_arquivo = 'arq10.txt'
mensagem = input("Mensagem: ")
if gravar_arquivo_exclusivo(nome_arquivo, mensagem):
    print('Gravado com Sucesso!')
else:
    print('Não gravou porque o arquivo já existe!')

'''
1. Crie uma função que passa por parâmetro o nome do arquivo e o conteudo e crie-o
2. Crie uma função que passe por parâmetro e nome do arquivo e exiba-o se ele existir
3. Faça uma função que abra um arquivo, conte quantas palavras há nele e retorne a quantidade
'''

def criar_arquivo(nome: str, conteudo: str) -> None:
    try:
        arquivo = open(nome, 'x', encoding='utf-8')
        arquivo.write(conteudo + '\n')
    except FileExistsError:
        print('Já existe um arquivo com esse nome!')
    else:
        print('Arquivo criado com sucesso!')
        arquivo.close()

def exibir_arquivo(nome: str) -> None:
    try:
        arquivo = open(nome,'r', encoding='utf-8')
        arquivo.read()
    except FileNotFoundError:
        print('O arquivo não foi encontrado')
    else:
        arquivo.close()

print(len(letras.split()))