import os
os.system("clear")

########### SUBALGORITMOS
# ---- procedimentos
def preencer_lista(l: list) -> None:
    while True:
        elem = input("Elemento: ")
        if elem == ".":
            break
        else:
            l.append(elem)

def exibir_lista(l: list) -> None:
    print()
    for ind, elem in enumerate(l, 1):
        print(f'{ind} -> {elem}')
# ---- funções
def retornar_ultimo(lista: list) -> str:
    print()
    return lista[-1]


########### PRINCIPAL
lista = []
while True:
    print("""
0 - SAIR
1 - Preencher lista
2 - Exibir Lista
3 - Exibir ultimo elemento
        """)
    opcao = input('Escolha: ')
    match opcao:
        case '0':
            break
        case '1':
            preencer_lista(lista)
        case '2':
            if len(lista) > 0:
                exibir_lista(lista)
            else:
                print("\nA lista está vazia")
        case '3':
            if len(lista) > 0:
                ultimo = retornar_ultimo(lista)
                print(f"Último elemento da lista: {ultimo}")
            else:
                print("\nA lista está vazia")
        case _:
            print("Opção Inválida, tente novamente!")
    input("Pressione algo para continuar")