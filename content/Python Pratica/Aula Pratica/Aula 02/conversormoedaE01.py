####################################
######## Conversor de moeda ########
####################################


#Exercicios solicitados sobre python


# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

##################################################################################################

cotacaos = [] #lista para armazenar a cotacao

class cotacao:
    def __init__ (self, dolar, euro):
        self.dolar = dolar
        self.euro = euro


#Definir cotação do dolar e euro
def cotacaocadastro ():
    dolar = float(input("Qual é a cotação do dolar hoje? "))
    euro = float(input("Cotação do euro hoje? "))
    minhacotacao = cotacao(dolar, euro)
    cotacaos.append(minhacotacao)

def showcotacao ():
    if not cotacaos:
        print("Sem registro")
        return

    for id, cotacao in enumerate (cotacaos, start = 1):
        print(f"O id é de {cotacao.id}A cotação do dolar é de {cotacao.dolar} e o euro é de {cotacao.euro}")


flag = False
while flag != True:

    menu = int(input("\t\n 1- Cotação de hoje \t\n 2 - Reais Brasileiros \t\n 3 - sair"))
    if menu == 1:
        cotacaocadastro()
    elif menu == 2:
        if not cotacaos:
            print("Sem cotação")

        real = float(input("Quantos reais você tem? "))

        ultima_cotacao = cotacaos [-1]
        dolareal = real / ultima_cotacao.dolar
        euroreal = real / ultima_cotacao.euro
        print(f"Você tem R${real} em reais em dolar voce tem U${dolareal} e em euros você teria {euroreal}")

    elif menu == 3:
        print ("Saindo do sistema")
        flag = True

    else:
        print("Opção invalida")
