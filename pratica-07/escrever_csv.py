"""
Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade.
"""

import csv

def escrever_csv(nome_arquivo, dados):
    with open (nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Nome', 'Idade', 'Cidade'])
        for linha in dados:
            escritor.writerow(linha)
    print(f"Dados salvos em {nome_arquivo}")

dados = [
    ['Ana', 28, 'Rio de Janeiro'],
    ['Bento', 36, 'Sao Paulo'],
    ['Jose', 27, 'Vitoria'],
    ['Juliano', 25, 'Nova York']
]

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo csv: ")
    escrever_csv(nome_arquivo, dados)