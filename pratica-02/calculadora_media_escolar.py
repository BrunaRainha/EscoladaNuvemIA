"""
Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

- Nota 1: 7.5
- Nota 2: 8.0
- Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""

# Calculadora de média escolar

# Notas do estudante
nota1 = 7.5
nota2 = 8.8
nota3 = 6.5

# Calculo de média
media = (nota1 + nota2 + nota3) / 3

# Exibição do resultado
print("Notas do Estudante:")
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Média final:", round(media, 2))
