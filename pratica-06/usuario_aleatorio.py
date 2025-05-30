"""
Crie um programa que gera um perfil de usuário aleatório usando a
API 'Random User Generator'. O programa deve exibir o nome, email
e país do usuário gerado."
"""

import requests  # Biblioteca para fazer requisições HTTP

def gerar_usuario():
    url = "https://randomuser.me/api/"  # Endpoint da API

    try:
        resposta = requests.get(url)  # Envia uma requisição GET para a API
        if resposta.status_code == 200:
            dados = resposta.json()  # Converte a resposta em JSON
            usuario = dados['results'][0]

            nome = f"{usuario['name']['first']} {usuario['name']['last']}"
            email = usuario['email']
            pais = usuario['location']['country']

            print("=== Perfil Gerado ===")
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"País: {pais}")
        else:
            print("Erro ao obter dados da API. Código de status:", resposta.status_code)
    except Exception as e:
        print("Ocorreu um erro ao tentar acessar a API:", e)

# Executa o programa
gerar_usuario()
