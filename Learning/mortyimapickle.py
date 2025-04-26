# Aprendendo APIs - API do Rick and Morty
# Opções de API nesse caso: character, episode, location

import requests
import json
import os

os.system('cls')

def fetch_data(endpoint, filters={}):
    url = f"https://rickandmortyapi.com/api/{endpoint}"
    response = requests.get(url, params=filters)
    resposta_j = response.json()
    resposta = json.dumps(resposta_j, indent=4)
    return resposta if response.status_code == 200 else None


personagens = fetch_data("character", {'status': 'Dead'})

if personagens:
    print(personagens)
else:
    print("Erro ao buscar dados da API.")
