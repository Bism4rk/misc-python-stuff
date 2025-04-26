# API do IBGE

import requests
import pprint
import os
os.system('cls')

link2 = "https://servicodados.ibge.gov.br/api/v3/agregados/9625/periodos/2014|2022/variaveis/10484?localidades=N1[all]"

link = "https://servicodados.ibge.gov.br/api/v3/agregados/9625/periodos/2014|2022/variaveis/10484?localidades=N1[all]&classificacao=12920[119346]" # API do IBGE, especificamente sobre o número de espécies da fauna e flora brasileira consideradas "em perigo" de extinção, criada usando o query builder do IBGE.

requisicao = requests.get(link)
informacoes = requisicao.json()
# pprint.pprint(informacoes)

item_busca = informacoes[0]['variavel']
resultados = informacoes[0]['resultados'][0]['series'][0]['serie']

requisicao2 = requests.get(link2)
informacoes2 = requisicao2.json()
# pprint.pprint(informacoes2)

item_busca2 = informacoes2[0]['variavel']
resultados2 = informacoes2[0]['resultados'][0]['series'][0]['serie']

for x in resultados2:
    print(item_busca2 + " em " + str(x) + ": " + str(resultados2[x]) + ".")

print("-"*150)

for x in resultados:
    porcentagem = round(int(resultados[x])/int(resultados2[x])*100, 2)
    print("Porcentagem do " + item_busca.lower() + " consideradas em perigo em " + str(x) + ": " + str(porcentagem) + "%.")