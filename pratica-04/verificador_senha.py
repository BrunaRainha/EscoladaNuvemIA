"""
Crie um programa que verifique se uma senha é forte. Uma
senha forte deve ter pelo menos 8 caracteres e conter pelo
menos um número. O programa deve continuar pedindo
senhas até que uma válida seja inserida ou o usuário digite
'sair'.
"""

def verificar_senha_forte():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")

        # Encerrar o programa se o usuário quiser
        if senha.lower() == 'sair':
            print("Encerrando o programa.")
            break  # Encerra o loop

        # Verifica se a senha tem pelo menos 8 caracteres
        if len(senha) < 8:
            print("Senha fraca: deve conter pelo menos 8 caracteres.")
            continue  # Solicita nova senha

        # Verifica se a senha contém pelo menos um número
        tem_numero = False
        for caractere in senha:
            if caractere.isdigit():
                tem_numero = True
                break

        if not tem_numero:
            print("Senha fraca: deve conter pelo menos um número.")
            continue  # Solicita nova senha

        # Se passou em todas as verificações
        print("Senha forte! Acesso permitido.")
        break  # Sai do loop

# Executa o programa
verificar_senha_forte()
