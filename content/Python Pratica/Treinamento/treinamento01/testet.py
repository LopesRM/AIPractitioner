def soma ():
    numeros = []
    numero = float(input("Digite um numero: "))
    while numero != 0:
        numeros.append(numero)
        numero = float(input("Digite outro numero (ou 0 para sair): "))
    resultado = sum(numeros)
    return resultado
print(soma())