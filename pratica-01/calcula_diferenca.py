# Esse código lê valores inteiros inputados pelo usuário

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

# Calculo da diferença
DIFERENCA = (A * B) - (C * D)

# Exibir resultado
print("A fórmula para a diferença é: DIFERENCA = (A * B) - (C * D)")
print(f"Substituindo os valores fornecidos: ({A} * {B}) - ({C} * {D})")
print(f"O resultado da diferença é: {DIFERENCA}")