"""
Enunciado: Crie uma função que calcule a gorjeta a ser deixada em
um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada.

Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

Parâmetros:

valor_conta (float): O valor total da conta

porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

Retorna:

float: O valor da gorjeta calculada
"""

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso
valor_da_conta = float(input("Digite o valor total da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

valor_gorjeta = calcular_gorjeta(valor_da_conta, porcentagem)
print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
