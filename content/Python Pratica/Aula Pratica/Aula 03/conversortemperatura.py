temp = float(input("Digite uma temperatura: "))
origem = input("Digite a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
destino = input("Digite a unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()

def converter_temperatura(temp, origem, destino):
    if origem == destino:
        resultado = temp
    elif origem == 'C':
        if destino == 'F':
            resultado = (temp * 9/5) + 32
        elif destino == 'K':
            resultado = temp + 273.15
        else:
            raise ValueError("Unidade de destino inválida")
    elif origem == 'F':
        if destino == 'C':
            resultado = (temp - 32) * 5/9
        elif destino == 'K':
            resultado = (temp - 32) * 5/9 + 273.15
        else:
            raise ValueError("Unidade de destino inválida")
    elif origem == 'K':
        if destino == 'C':
            resultado = temp - 273.15
        elif destino == 'F':
            resultado = (temp - 273.15) * 9/5 + 32
        else:
            raise ValueError("Unidade de destino inválida")
    else:
        raise ValueError("Unidade de origem inválida")
    return resultado
try:
    resultado = converter_temperatura(temp, origem, destino)
    print(f"{temp}°{origem} é igual a {resultado:.2f}°{destino}")
except ValueError as e:
    print(f"Erro: {e}")
    