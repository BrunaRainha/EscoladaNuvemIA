"""
4- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

# Funções de conversão
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Solicita entrada do usuário
valor = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").strip().upper()
destino = input("Digite a unidade de destino (C, F ou K): ").strip().upper()

# Verifica e converte
resultado = None

if origem == "C":
    if destino == "F":
        resultado = celsius_para_fahrenheit(valor)
    elif destino == "K":
        resultado = celsius_para_kelvin(valor)
    elif destino == "C":
        resultado = valor
elif origem == "F":
    if destino == "C":
        resultado = fahrenheit_para_celsius(valor)
    elif destino == "K":
        resultado = fahrenheit_para_kelvin(valor)
    elif destino == "F":
        resultado = valor
elif origem == "K":
    if destino == "C":
        resultado = kelvin_para_celsius(valor)
    elif destino == "F":
        resultado = kelvin_para_fahrenheit(valor)
    elif destino == "K":
        resultado = valor

# Exibe o resultado ou erro
if resultado is not None:
    print(f"{valor}°{origem} equivale a {resultado:.2f}°{destino}")
else:
    print("Unidade inválida. Use apenas C, F ou K.")
