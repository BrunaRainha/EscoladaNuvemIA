"""
Crie uma função que verifique se uma palavra ou frase é um
palíndromo (lê-se igual de trás para frente, ignorando
espaços e pontuação).

Se o resultado é True, responda “Sim”, se o resultado for
False, responda “Não”
"""

def eh_palindromo(texto):

    # Remove espaços, pontuação e converte para minúsculas
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    # Verifica se o texto limpo é igual ao seu reverso
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

# Exemplo de uso
frase = input("Digite uma palavra ou frase: ")
resultado = eh_palindromo(frase)
print(f"É palíndromo? {resultado}")
