# API - Aplication Programming Interface

import os
import requests as req
# Verificar um endereço pela API do Correiro
cep = input("Digite o CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = req.get(url) # Chamada da API com os dados fornecidos pelo usuário

dados = resposta.json() # Transformando a resposta em JSON

print("Endereço")
print(f"CEP: {dados['cep']}\nLogradouro: {dados['logradouro']}"
       + f"\nBairro: {dados['bairro']}\nCidade: {dados['localidade']}\nEstado: {dados['uf']}")