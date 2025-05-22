#Estudo extra:
#Treinos Básicos Python:

#Resposta com base no tempo atual
#Importar a biblioteca
import datetime

usuario = input("Com quem estou falando ")

hora_atual =datetime.datetime.now().hour
if 0 <= hora_atual < 12:
    printrint(f"Olá, {usuario} boa madrugada como você esta?")
elif 13 <= hora_atual < 18:
    print(f"Oi, {usuario} que tarde linda é essa?")
elif 19 <= hora_atual < 23:
    print(f"Bem vindo, {usuario} que noite linda, parece crepusculo para madrugar com python?")