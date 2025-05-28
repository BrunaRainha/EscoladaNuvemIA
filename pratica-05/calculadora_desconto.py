"""
Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto.
Requisitos:

- Permitir que o usuário informe o preço do produto e o percentual de desconto.
- Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
- Exibir o preço final com duas casas decimais para garantir precisão.
Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
"""

def calcular_preco_final(preco_original, percentual_desconto):
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return preco_final

# Entrada do usuário
preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto: "))

# Cálculo e saída
preco_com_desconto = calcular_preco_final(preco, desconto)
print(f"Preço final com desconto: R$ {preco_com_desconto:.2f}")
