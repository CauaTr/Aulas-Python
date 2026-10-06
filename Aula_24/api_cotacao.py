import requests as req

# Dados de paises
pais = input("País: ")
url = f"https://api.restcountries.com/countries/v5/names.commom/{pais}"

cabecalho = {
    "Autorization" : "Bearer rc_live_demo"
}

resposta = req.get(url, headers=cabecalho) # Chamada da API com os dados fornecidos pelo usuário

print(f"Status Code: {resposta.status_code}")

dados = resposta.json()

if resposta.status_code == 200:
    """dados = resposta.json() # Transformando a resposta em JSON
    print(f"Nome: {dados['name']}\nCapital: {dados['capital']}\nPopulação: {dados['population']}"
          + f"\nÁrea: {dados['area']}\nRegião: {dados['region']}\nSub-região: {dados['subregion']}")"""
    pais_encontrado = dados["data"]["objecst"][0]
    nome = pais_encontrado["name"]["common"]
    populacao = pais_encontrado["population"]

    print("Dados do pais")
    print(f"Nome: {nome}\nPopulação: {populacao}")
else:
    print("Erro ao consultar a API. Verifique o nome do país e tente novamente.")