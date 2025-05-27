"""
Crie um programa que permita a um professor registrar as
notas de uma turma. O programa deve continuar solicitando
notas até que o professor digite 'fim'. Notas válidas são de 0 a
10. O programa deve ignorar notas inválidas e continuar
solicitando. No final, deve exibir a média da turma.
"""

def registrar_notas():
    notas = []  # Lista para armazenar as notas válidas

    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")

        # Encerrar o programa se o usuário digitar 'fim'
        if entrada.lower() == 'fim':
            break  # Encerra o loop

        try:
            nota = float(entrada)  # Tenta converter a entrada em número

            if 0 <= nota <= 10:
                notas.append(nota)  # Adiciona nota válida à lista
            else:
                print("Nota fora do intervalo! Digite uma nota entre 0 e 10.")
                continue  # Volta para o início do loop

        except ValueError:
            print("Entrada inválida! Digite um número válido ou 'fim'.")
            continue  # Volta para o início do loop

    # Após saída do loop, verifica se há notas registradas
    if notas:
        media = sum(notas) / len(notas)
        maior = max(notas)
        menor = min(notas)

        print("\n Resultados Finais:")
        print(f"Quantidade de notas válidas: {len(notas)}")
        print(f"Média da turma: {media:.2f}")
        print(f"Maior nota: {maior}")
        print(f"Menor nota: {menor}")
    else:
        print("\nNenhuma nota válida foi registrada.")

# Executa o programa
registrar_notas()
