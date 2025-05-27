def mesa():
    todasasmesas = []
    digitenumero = int(input("Qual mesa deseja selecionar"))
    numeromesa = digitenumero
    todasasmesas.append(numeromesa)   
    return todasasmesas

def comandas():
    todasascomandas = []
    digitecomanda = int(input("Qual comanda deseja selecionar"))
    numerocomanda = digitecomanda
    todasascomandas.append(numerocomanda)   
    return todasascomandas
    
while True:
    acabou = False  # Defina a condição de parada conforme necessário
    if acabou:
        numero = 0
        break
    elif comandas:
        numero = 1