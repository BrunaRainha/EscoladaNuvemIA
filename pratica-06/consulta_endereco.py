"""
Desenvolva um programa que consulte informações de
endereço a partir de um CEP fornecido pelo usuário,
utilizando a API ViaCEP. O programa deve exibir o
logradouro, bairro, cidade e estado correspondentes ao CEP
consultado.
"""

import requests  # Biblioteca para fazer requisições HTTP

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()

            if "erro" in dados:
                print(" CEP não encontrado. Verifique e tente novamente.")
            else:
                print("\n=== Endereço Encontrado ===")
                print(f"Logradouro: {dados['logradouro']}")
                print(f"Bairro: {dados['bairro']}")
                print(f"Cidade: {dados['localidade']}")
                print(f"Estado: {dados['uf']}")
        else:
            print(" Erro ao acessar a API. Código:", resposta.status_code)
    except Exception as e:
        print(" Erro de conexão:", e)

# Programa principal
cep_input = input("Digite um CEP (somente números): ").strip()

if cep_input.isdigit() and len(cep_input) == 8: # Verifica se a string tem apenas números, e sabe quantos elementos há 
    consultar_cep(cep_input)
else:
    print(" CEP inválido. Deve conter 8 dígitos numéricos.")
