"""
Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição,
subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com
diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.

As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

O programa deve continuar solicitando entradas até que uma operação válida seja
concluída.

Trate os seguintes erros:

Entrada inválida (não numérica) para os números

Divisão por zero

Operação inválida

Use try/except para capturar e tratar os erros apropriadamente.

Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.

Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.
"""

def calculadora():
    while True:
        # Tenta ler o primeiro número
        try:
            num1 = float(input("Digite o primeiro número: "))
        except ValueError:
            print("Erro: Entrada inválida. Digite um número válido.")  # Captura ValueError
            continue  # Volta para o início do loop principal

        # Tenta ler o segundo número
        try:
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Entrada inválida. Digite um número válido.")  # Captura ValueError
            continue  # Volta para o início do loop principal

        # Lê a operação desejada
        operacao = input("Digite a operação (+, -, *, /): ")

        # Verifica se a operação é válida
        if operacao not in ['+', '-', '*', '/']:
            print("Erro: Operação inválida. Escolha entre +, -, * ou /.")
            continue  # Volta para o início do loop principal

        # Tenta realizar a operação
        try:
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2

        except ZeroDivisionError as erro:
            print(f"Erro: {erro}")
            continue  # Volta para o início do loop principal

        # Se chegou aqui, a operação foi bem-sucedida
        print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
        print("Operação concluída com sucesso!")
        break  # Encerra o loop e o programa

# Executa a calculadora
calculadora()
