# Aprenda DE VEZ o que é uma API
# API = Application Programming Interface
# API é um conjunto de rotinas e padrões estabelecidos por uma aplicação para utilização de suas funcionalidades por outros aplicativos.
# Ou seja, é uma forma de comunicação entre sistemas.

import requests
import pprint # Print Pretty Print, para imprimir dicionários de forma mais legível.
import json
import os
os.system('cls')

api_key = "3271d1aecc3e4e4a86f175025252204"
link_api = "http://api.weatherapi.com/v1/current.json" 
parametros = {
    "key": api_key,
    "q": "Porto Alegre",
    "lang": "pt"
}

resposta = requests.get(link_api, params=parametros) # Params são os parâmetros que você quer passar para a API, e aceita dicionários.

'''
print(resposta) # Retorna um status code, que é o código de resposta HTTP. 
200 = OK
300 = Redirecionamento
400 = Erro do cliente
    401 = Não autorizado
    403 = Proibido
500 = Erro do servidor
'''

if resposta.status_code == 200: # Se o status code for 200, significa que a requisição foi bem sucedida.
    dados_requisicao = resposta.json() # Converte a resposta em JSON para um dicionário Python.
    # print(dados_requisicao)
    local = dados_requisicao["location"]["name"] # Acessa o nome do local.
    temp = dados_requisicao["current"]["temp_c"] # Acessa a temperatura atual em Celsius.
    descricao = dados_requisicao["current"]["condition"]["text"] # Acessa a condição do tempo atual.
    sensacao =  dados_requisicao["current"]["feelslike_c"] # Acessa a sensação térmica atual em Celsius.
    if descricao == "Sol":
        descricao = "ensolarado"
    print(f"A temperatura atual em {local} é de {temp}°C, com sensação térmica de {sensacao}°C e o tempo está {descricao}.")
    # pprint.pprint(dados_requisicao) #  Imprime o dicionário de forma mais legível.
else:
    print("Erro ao buscar dados da API.")
    print(resposta.status_code) # Imprime o status code da resposta.
    print(resposta.text)
    