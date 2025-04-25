import requests
import json
import os
from dotenv import load_dotenv
# Carrega as variáveis de ambiente do arquivo .env

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\misc-python-stuff\\Learning APIs\\senha.env", override=True) # Se a variável já existir (que é o caso aqui por causa do setx), ela não será sobrescrita. Se você quiser sobrescrever, use override=True.

chave = os.getenv("APIKEY")
print(chave)

# O código abaixo é só um exemplo ilustrativo de como usar a API do OpenAI. A API do OpenAI é uma API paga e você deve ter uma chave de API válida para usá-la.
'''
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
# link = "https://api.openai.com/v1/chat/completions"
# id_modelo = "gpt-4.1"

# body_mensagem = {
#     "model": id_modelo,
#     "messages": [{"role": "user", "content": "escreva um e-mail para o meu chefe dizendo a previsão do preço do dólar nos próximos 2 meses"}]
# }

# body_mensagem = json.dumps(body_mensagem) # Converte o dicionário em uma string JSON
# requisicao = requests.post(link, headers=headers, data=body_mensagem) # Envia a requisição para a API
# resposta = requisicao.json() # Converte a resposta em JSON
# mensagem = resposta['choices'][0]['message']['content'] # Pega a mensagem da resposta
# print(mensagem) # Imprime a mensagem
'''

'''
Colocar a API key em uma variável não é uma boa prática de segurança, pois ela pode ser exposta acidentalmente.
Ex: API_KEY = "WSERTGHYU6JHYGTRED3RFGTY"
Colocar em um arquivo separado não é uma boa prática também, pois o arquivo deve ser ligado ao repositório quando for enviado para o github.
Uma boa prática é usar variáveis de ambiente para armazenar a chave da API, pois ela só fica disponível no ambiente de execução e não é exposta no código.

Como criar uma variável de ambiente:
1. No Windows, abre o terminal e digite: setx API_KEY "sua_chave_aqui" - A mensgem "ÊXITO: o valor especificado foi salvo." será exibida.
    - Quando você reiniciar o editor, a variável de ambiente estará disponível.
    - Para verificar se a variável foi criada, crie uma varíavel com os.getenv("nome_da_variavel") e imprima o valor dela.

2. Criar um arquivo .env com o seguinte conteúdo:
API_KEY="sua_chave_aqui"
    - Para usar o arquivo .env, você deve instalar a biblioteca python-dotenv: pip install python-dotenv
    - Depois, você deve importar a biblioteca e carregar as variáveis de ambiente do arquivo .env:
        from dotenv import load_dotenv
        load_dotenv()
    - Agora você pode usar a variável de ambiente normalmente com os.getenv("nome_da_variavel")
    - Arquivos .env não são enviados para o github, pois estão no .gitignore por padrão.
    - Para verificar se a variável foi criada, crie uma varíavel com os.getenv("nome_da_variavel") e imprima o valor dela.

3. Usar um sistema externo de gerenciamento de segredos, como o AWS Secrets Manager ou o Azure Key Vault. Esses serviços permitem armazenar e gerenciar segredos de forma segura e acessá-los em seu código.
    - Para usar esses serviços, você deve criar uma conta e seguir a documentação para criar e acessar os segredos.
'''