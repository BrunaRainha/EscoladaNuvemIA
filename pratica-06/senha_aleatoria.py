"""
Crie um programa que gera uma senha aleatória com o
módulo random, utilizando caracteres especiais,
possibilitando o usuário a informar a quantidade de
caracteres dessa senha aleatória.
"""

# Importando o módulo padrão random
import random
import string 

def gerar_senha(tamanho):
    
    # Gera uma senha aleatória com letras, números e caracteres especiais.
    
    # Caracteres disponíveis: letras maiúsculas, minúsculas, dígitos e pontuação
    caracteres_disponiveis = string.ascii_letters + string.digits + string.punctuation

    # Utiliza random.choice para selecionar caracteres aleatórios
    senha = ''.join(random.choice(caracteres_disponiveis) for _ in range(tamanho))
    
    return senha

# Entrada do usuário
try:
    tamanho = int(input("Digite o número de caracteres da senha: "))
    
    if tamanho <= 0:
        print("O número deve ser maior que zero.")
    else:
        senha = gerar_senha(tamanho)
        print(f"Senha gerada: {senha}")

except ValueError:
    print("Por favor, digite um número inteiro válido.")
