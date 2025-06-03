"""
Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do temo de exercução contantes.
"""

import pandas as pd

def processar_logs_treinamento(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        desvio_padrao_tempo = df['tempo_execucao'].std()
        media = df['tempo_execucao'].mean()
        print(f"\nO Desvio Padrão (DP) é: {desvio_padrao_tempo:.2f}")
        print(f"A média do tempo de execução é: {media:.2f}")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo de log: {e}")


nome_arquivo = input("Digite o nome do arquivo de log: ")
processar_logs_treinamento(nome_arquivo)