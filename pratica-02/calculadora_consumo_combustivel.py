"""
Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

- Distância percorrida: 300 km
- Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

# Calculadora de consumo de combustivel

# Dados da viagem
distancia_percorrida = 300 # em km
combustivel_gasto = 25 # em litros

# Calculo do consumo médio
consumo_medio = distancia_percorrida / combustivel_gasto

# Exibição do resultado
print("Dados da viagem:")
print(f"Distância percorrida: {distancia_percorrida} KM")
print(f"Combustivel gasto: {combustivel_gasto} L")
print("Consumo médio:", round(consumo_medio, 2), "KM/L")