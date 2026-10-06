import requests as req
from tkinter import *

def pegar_cotacoes() -> None:
    requisicao = req.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_disc = requisicao.json()

    cotacao_dolar = requisicao_disc["USDBRL"]["bid"]
    cotacao_euro = requisicao_disc["EURBRL"]["bid"]
    cotacao_btc = requisicao_disc["BTCBRL"]["bid"]

    texto_resposta["text"] = f"Cotação do Dólar: {cotacao_dolar}\nCotação do Euro: {cotacao_euro}\nCotação do Bitcoin: {cotacao_btc}"

janela = Tk()
janela.title("Cotações de Moedas")
texto = Label(janela, text="Clique para ver as cotações")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="Resposta")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()