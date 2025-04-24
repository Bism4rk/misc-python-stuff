# API do Banco Central

import os
import requests
import pprint
import pandas as pd

os.system('cls')

# link = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=28&$orderby=Data%20desc&$format=json"

# link = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=112&$orderby=Data%20desc&$format=json" # API do Banco Central, especificamente sobre a quantidade de dinheiro em circulação no Brasil, criada usando o query builder do Banco Central.

link = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$orderby=Data%20desc&$format=json" # API do Banco Central, especificamente sobre a quantidade de dinheiro em circulação no Brasil, criada usando o query builder do Banco Central.

requisicao = requests.get(link)
informacoes = requisicao.json()
# pprint.pprint(informacoes)

tabela = pd.DataFrame(informacoes['value'])
tabela['Quantidade'] = tabela['Quantidade'].map("{:,}".format) # Formata a coluna 'Quantidade' para exibir com separador de milhar
tabela['Valor'] = tabela['Valor'].map("R$ {:,.2f}".format) # Formata a coluna 'Valor' para exibir com separador de milhar e duas casas decimais
tabela['Denominacao'] = tabela['Denominacao'].map("R$ {}".format) # Formata a coluna 'Denominacao' para colocar o símbolo de R$ na frente

print(tabela)

print('-'*150)

# Pegar todas as informacoes com varias requisições
# A maioria das APIs tem um limite de um certo número requisições por vez, então é necessário fazer várias requisições para pegar todas as informações. O código abaixo faz isso, mas não é necessário para essa API específica.

tabela_final = pd.DataFrame()
pular_indice = 0

while True:
    link = f'https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$skip={pular_indice}&$orderby=Data%20desc&$format=json'
    requisicao = requests.get(link)
    informacoes = requisicao.json()
    tabela = pd.DataFrame(informacoes['value'])
    if len(informacoes['value']) == 0:
        break
    tabela_final = pd.concat([tabela_final, tabela])
    pular_indice += 10000

tabela_final['Quantidade'] = tabela_final['Quantidade'].map("{:,}".format) # Formata a coluna 'Quantidade' para exibir com separador de milhar
tabela_final['Valor'] = tabela_final['Valor'].map("R$ {:,.2f}".format) # Formata a coluna 'Valor' para exibir com separador de milhar e duas casas decimais
print(tabela_final)








