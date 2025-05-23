#####################################
######## Calculo Combustivel ########
#####################################


# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# * Distância percorrida: 300 km
# * Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.


#####################################################################################################


combustivelkm = []
class combustiveldistancia():
    def __init__ (self, km, combustivel):
        self.km = km
        self.combustivel  = combustivel

def combustivel():
    distancia = float(input("Qual é a distancia? "))
    combustivel = float(input("Quantos km roda com 1 litro? "))
    meuregistro = combustiveldistancia(distancia, combustivel)
    combustivelkm.append(meuregistro)

def showkmcombustivel ():
    if not combustivelkm:
        print("Sem registro")
        return

    for id, combustiveldistancia in enumerate (combustivelkm, start = 1):
        print(f"O id do seu veiculo é de {combustiveldistancia.id} a distancia a ser percorrida é de {combustiveldistancia.distancia} consumo de combustivel por km litro é de {combustiveldistancia.combustive}")


flag = False
while flag != True:
    
    menu = int(input("\t\n 1- Cadastrar a distancia e o km litro \t\n 2 - Calcular o consumo \t\n 3 - Sair"))
    if menu == 1:
        combustivel()
    elif menu == 2:
         if not combustivelkm:
            print("Sem registro de veiculo")
            
            ultima_combustiveldistancia = combustivelkm [-1]
            consumodistancia2 =  ultima_combustiveldistancia.km / ultima_combustiveldistancia.combustivel
            print(f"Seu consumo de gasolina é de {consumodistancia2} por km rodado")

    elif menu == 3:
        print ("Saindo do sistema")
        flag = True

else:
    print("Opção invalida")
