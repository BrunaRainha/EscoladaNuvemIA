"""
Crie um programa que consulte a cotação atual de uma
moeda estrangeira em relação ao Real Brasileiro (BRL). O
usuário deve informar o código da moeda desejada (ex: USD,
EUR, GBP), e o programa deve exibir o valor atual, máximo e
mínimo da cotação, além da data e hora da última
atualização. Utilize a API da AwesomeAPI para obter os
dados de cotação.
"""

import requests

def consultar_cotacao():
    print("=== Consulta de Cotação ===")
    moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        dados = resposta.json()

        if f"{moeda}BRL" not in dados:
            print("Moeda não encontrada. Verifique o código informado.")
            return

        cotacao = dados[f"{moeda}BRL"]

        print("\n--- Cotação Atual ---")
        print(f"Moeda: {cotacao['name']}")
        print(f"Valor atual: R$ {cotacao['bid']}")
        print(f"Valor máximo: R$ {cotacao['high']}")
        print(f"Valor mínimo: R$ {cotacao['low']}")
        print(f"Última atualização: {cotacao['create_date']}")

    except Exception as e:
        print("Erro ao consultar a cotação:", e)

# Executar o programa
consultar_cotacao()
