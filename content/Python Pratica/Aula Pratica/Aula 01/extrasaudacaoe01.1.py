#Estudo extra:
#Treinos Básicos Python:

#Resposta com base no tempo atual
#Importar a biblioteca
import datetime
import random


# Definindo as listas de saudações
dia = ["Bom dia", "Bom dia, como você está?", "Bom dia, tudo bem?", "Bom dia, espero que esteja tendo um bom dia", "Bom dia, como foi seu dia?"]
tarde = ["Boa tarde", "Boa tarde, como você está?", "Boa tarde, tudo bem?", "Boa tarde, espero que esteja tendo um bom dia", "Boa tarde, como foi seu dia?"]
noite =["Boa noite", "Boa madrugada", "Boa noite, durma bem", "Boa noite, sonhe com os anjos", "Boa noite, até amanhã"]


# Definindo a variável usuario
usuario = input("Com quem estou falando ")


# Definindo a variável hora_atual
hora_atual =datetime.datetime.now().hour


# Definindo a variável saudacao
saudacao_dia = random.choice(dia)
saudacao_tarde = random.choice(tarde)
saudacao_noite = random.choice(noite)


# Definindo a variável saudacao
while True:
    if 0 <= hora_atual < 12:
        print(f"Olá, {usuario} {saudacao_dia}")
    elif 13 <= hora_atual < 18:
        print(f"Oi, {usuario} {saudacao_tarde}")
    elif 19 <= hora_atual < 24:
        print(f"Bem vindo, {usuario} {saudacao_noite}")
    else:
        print("Hora inválida")
        break
    
    # Adicionando uma pausa para evitar loop infinito
    #time.sleep(1)  # Pausa de 1 segundo
    # Adicionando uma condição de parada para o loop
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break
        
