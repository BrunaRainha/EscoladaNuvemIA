"""
Crie uma função que calcule a idade de uma pessoa em dias,
baseada no ano de nascimento.
"""

from datetime import date

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Aproximação (não considera anos bissextos)
    return idade_dias

# Exemplo de uso
ano = int(input("Digite o ano de nascimento: "))
idade_dias = calcular_idade_em_dias(ano)
print(f"Idade aproximada em dias: {idade_dias}")
