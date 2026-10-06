import tkinter as tk

# Função que lê o dado e atualiza a tela
def ler_dado():
    # Obtém o texto digitado na caixa de entrada
    texto_digitado = entrada.get()
    # Exibe o valor lido no Label
    resultado_var.set(f"Você digitou: {texto_digitado}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Ler Dado no Tkinter")
janela.geometry("300x200")

# Caixa de texto (Entry) para o usuário digitar
entrada = tk.Entry(janela, width=25)
entrada.pack(pady=10)

# Botão para acionar a leitura
botao = tk.Button(janela, text="Ler Valor", command=ler_dado)
botao.pack(pady=5)

# Variável de controle para atualizar o texto do Label dinamicamente
resultado_var = tk.StringVar()
resultado_var.set("Aguardando dado...")

# Rótulo (Label) que vai mostrar o dado lido na janela
rotulo_resultado = tk.Label(janela, textvariable=resultado_var)
rotulo_resultado.pack(pady=10)

# Inicializa o loop da janela
janela.mainloop()