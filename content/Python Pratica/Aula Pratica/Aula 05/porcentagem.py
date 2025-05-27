compra = float(input("Qual valor total da compra: "))
gorjeta = float(input("% da gorjeta: "))



def Gorjeta_Calculo (compra, gorjeta):
    calculo = compra * (gorjeta/100)
    print(f"O valor da gorjeta é de: {calculo:.2f}")
    return calculo

Gorjeta_Calculo (compra, gorjeta)