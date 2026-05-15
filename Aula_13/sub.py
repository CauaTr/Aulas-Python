# CONSTRUÇÃO DOS SUBALGORITMOS
# ------------ PROCEDIMENTOS
def saudacao() -> None:
    print("Bom dia Cauã!")

def saudacao2(nome: str) -> None:
    print(f"Bom dia {nome}!")

def saudacao3(nome: str, hora: int) -> None:
    if hora < 12:
        msg = "Bom dia!"
    elif hora < 18:
        msg = "Boa tarde!"
    else:
        msg = "Boa noite!"
    print(f'{msg} {nome}')
# ------------ FUNÇÕES

# PROGRAMA PRINCIPAL
saudacao()
saudacao2("Caio")
nome = "Marcelo"
saudacao2(nome)
saudacao3("Osmar", 17)
