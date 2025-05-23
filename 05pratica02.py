#########################
######## Aula 07 ########
#########################

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

# cotacaos = [] #lista para armazenar a cotacao

# class cotacao:
#     def __init__ (self, dolar, euro):
#         self.dolar = dolar
#         self.euro = euro


# Definir cotação do dolar e euro
# def cotacaocadastro ():
#     dolar = float(input("Qual é a cotação do dolar hoje? "))
#     euro = float(input("Cotação do euro hoje? "))
#     minhacotacao = cotacao(dolar, euro)
#     cotacaos.append(minhacotacao)

# def showcotacao ():
#     if not cotacaos:
#         print("Sem registro")
#         return

#     for id, cotacao in enumerate (cotacaos, start = 1):
#         print(f"O id é de {cotacao.id}A cotação do dolar é de {cotacao.dolar} e o euro é de {cotacao.euro}")


# flag = False
# while flag != True:

#     menu = int(input("\t\n 1- Cotação de hoje \t\n 2 - Reais Brasileiros \t\n 3 - sair"))
#     if menu == 1:
#         cotacaocadastro()
#     elif menu == 2:
#         if not cotacaos:
#             print("Sem cotação")

#         real = float(input("Quantos reais você tem? "))

#         ultima_cotacao = cotacaos [-1]
#         dolareal = real / ultima_cotacao.dolar
#         euroreal = real / ultima_cotacao.euro
#         print(f"Você tem R${real} em reais em dolar voce tem U${dolareal} e em euros você teria {euroreal}")

#     elif menu == 3:
#         print ("Saindo do sistema")
#         flag = True

#     else:
#         print("Opção invalida")


##########################
######## Desconto ########
##########################

# 2- Calculadora de Desconto
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.


#####################################################################################################


# produto = float(input("Qual valor do produto: "))
# desconto = float(input("Qual valor do desconto: "))

# precofinal = ((produto * desconto)/100)
# precofinal2 = (produto - precofinal)
# print(f"Seu produto ficou com o desconto de {precofinal} ficando em {precofinal2}")


#######################
######## Média ########
#######################


# notaA = float(input("Nota A "))
# notaB = float(input("Nota B "))
# notaC = float(input("Nota C"))

# resultado_final = ((notaA + notaB + notaC)/3)
# #rint"resultado da nota A {notaA}, notaB{notaB}, notaC{notaC} ficou em {resultado_final})
# print(f"resultado da nota A {notaA}, notaB{notaB}, notaC{notaC} ficou em {resultado_final:.2f}")

#####################################
######## Calculo Combustivel ########
#####################################


# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

# * Distância percorrida: 300 km
# * Combustível gasto: 25 litros
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.


#####################################################################################################


# combustivelkm = []
# class combustiveldistancia():
#     def __init__ (self, km, combustivel):
#         self.km = km
#         self.combustivel  = combustivel

# def combustivel():
#     distancia = float(input("Qual é a distancia? "))
#     combustivel = float(input("Quantos km roda com 1 litro? "))
#     meuregistro = combustiveldistancia(distancia, combustivel)
#     combustivelkm.append(meuregistro)

# def showkmcombustivel ():
#     if not combustivelkm:
#         print("Sem registro")
#         return

#     for id, combustiveldistancia in enumerate (combustivelkm, start = 1):
#         print(f"O id do seu veiculo é de {combustiveldistancia.id} a distancia a ser percorrida é de {combustiveldistancia.distancia} consumo de combustivel por km litro é de {combustiveldistancia.combustive}")


# flag = False
# while flag != True:
    
#     menu = int(input("\t\n 1- Cadastrar a distancia e o km litro \t\n 2 - Calcular o consumo \t\n 3 - Sair"))
#     if menu == 1:
#         combustivel()
#     elif menu == 2:
#          if not combustivelkm:
#             print("Sem registro de veiculo")
            
#             ultima_combustiveldistancia = combustivelkm [-1]
#             consumodistancia2 =  ultima_combustiveldistancia.km / ultima_combustiveldistancia.combustivel
#             print(f"Seu consumo de gasolina é de {consumodistancia2} por km rodado")

#     elif menu == 3:
#         print ("Saindo do sistema")
#         flag = True

# else:
#     print("Opção invalida")



#####################################
############# Saudação ##############
#####################################

# # # 1- Programa de Saudação
# # # * Crie um programa que imprima a mensagem "Olá, mundo!" na tela.


# #Saudação
# bom_dia = print ("Avadaquedabra")
# resposta = input ("Saudação: ")

# print ("Que tem de bom?")


#############################################################################################################################



#####################################
############ Calculadora ############
#####################################


# # # * Desenvolva um programa que soma dois números. Use as variáveis numero1 = 12 e numero2 = 14. O programa deve calcular a soma e exibir o resultado.


###################################################################################################################################


#soma e multiplicação

# a = int(input("Valor 1: "))
# b = int(input("Valor 2: "))
# c = float(input("Multiplicar por: "))

# print (f"valor a {a} e o valor b {b} e multiplica {c} é igual {(a+b)*c}")

# def multiplicacao (entrada, multiplicador):
#     result = entrada * multiplicador
#     return result
# print (multiplicacao(a+b,c))


#####################################
############### Volume ##############
#####################################


# # # 3- Calculadora de Volume
# # # * Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:

# # # * Comprimento: 12 cm
# # # * Largura: 14 cm
# # # * Altura: 20 cm
# # # O programa deve calcular o volume e exibir o resultado em cm³.


######################################################################################################################


#Calculadora de volume em cilindro

# pi = 3.14
# r = float(input("Qual é o Raio?: "))
# h = float(input("Altura?: "))

# resultado = str(pi*r**2*h)

# print (resultado)


#######################################################
############ 4- Calculadora de Preço Total ############
#######################################################


# # # * Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

# # # * Nome do produto: "Cadeira Infantil"
# # # * Preço unitário: R$ 12.40
# # # * Quantidade: 3
# # # O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final


#######################################################################################################################


# #Calculadora de Preço
# produtos = []
# carrinho = []

# #Cadastrar Produto
# def cadastroproduto ():
#     nome = input("Nome do Produto: ")
#     preco = int(input("Preço: "))
#     meuproduto = produto(preco,nome)
#     produtos.append(meuproduto)



# #Catalogo
# def showproduto ():
#     id = 0
#     for produto in produtos:
#         id = (id+1)
#         print (f"{id} {produto.nome} {produto.preco}")

# def showcart ():
#     if not carrinho:
#         print("Seu carrinho esta vazio.")
#         return
    
#     print("\nSeu carrinho tem os seguintes intes: ")
#     for i, item in enumerate(carrinho, start = 1):
#         print (f"Você tem no seu carrinho os seguintes itens: {i} {item.nome} preço {item.preco:.2f}")
        
    
# #Registro objeto
# class produto: 
#     def __init__ (self,preco,nome):
#         self.nome = nome
#         self.preco = preco
# #Menu
# flag = False
# while flag != True:
        
#     menu = int(input("\n 1 - Cadastra Produto \t\n 2 - Sair \t\n 3 - Catalago \t\n 4 - Add Carrinho: \t\n 5 - Mostrar Carrinho: \t\n 6 - Finalizar Compra"))
#     if menu == 1:
#         cadastroproduto()
#         print (produtos [0].nome)
#     elif menu == 2:
#         flag = True
#     elif menu == 3:
#         showproduto()
#     elif menu == 4:
#         addcart = int(input("Qual ID do produto: "))
#         produtinho = produto (produtos [addcart -1].preco,produtos [addcart -1].nome)
#         quantidadecart = int(input("Quantos produtos: "))
#         produtinho.preco *= quantidadecart
#         carrinho.append(produtinho)
#         print (produtinho.preco)
#     elif menu == 5:
#         showcart()



##########################
###### IDADE MINIMA ######
##########################

# # Crie um programa que solicite a idade do usuário e classifique-o 
# # em uma das seguintes categorias: 

# # *Criança (0-12 anos), 
# # *Adolescente (13-17 anos), 
# # *Adulto (18-59 anos) ou 
# # *Idoso (60 anos ou mais).


################################################################################################################


# #Pessoa
# pessoas = []

# def pessoacadastro():
#     nome = input("Nome: ")
#     idade = float(input("Sua Idade: "))
#     minhapessoa = pessoa(nome, idade)
#     pessoas.append(minhapessoa)

# def showpessoa():
#     id = 0
#     for pessoa in pessoas:
#         id = (id+1)
#         print(f"{id} Nome é {pessoa.nome} sua idade é de: {pessoa.idade}")


# class pessoa:
#     def __init__ (self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# flag = False
# while flag !=True:
    
#     menu = int(input("\t\n 1 - Cadastrar Pessoa \t\n 2 - Verificar idade: "))
#     if menu == 1:
#         pessoacadastro()
#     elif menu == 2:
#         showpessoa()
#         addcheck = int(input("Qual é o ID da pessoa: ")) -1

#         if 0<= addcheck < len(pessoas):

#             pessoinha = pessoas[addcheck].idade
#             if pessoinha >= 18:
#                 print("Maior de idade")
#             else:
#                 print("Menor de Idade")
        


#####################################
############ Calculo IMC ############
#####################################


# # Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
# # O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
# # calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

# # < 18.5: classificacao = "Abaixo do peso"
# # < 25: classificacao = "Peso normal"
# # < 30: classificacao = "Sobrepeso"
# # Para os demais cenários: classificacao = "Obeso"


###############################################################################################################


#IMC Calculadora
#Array de nome, altura, peso e sexo
# pessoa = []

# #Registro
# def registro ():
#     nome = input("Seu Nome: ")
#     try:
#         altura = float(input("Sua altura: (00.00)"))
#         peso =  float(input("Seu peso: (00.00)"))
#     except ValueError:
#         print("Erro")
#         return
    
#     sexo = input("\t\n 1 - Masculino \t\n 2 - Feminino")
    
#     if sexo == "1":
#         sexo = "Masculino"
#     elif sexo == "2":
#         sexo = "Feminino"
#     else:
#         print("Opção invalida")
#         return
#     registropessoa = cpessoa(nome, altura, peso, sexo)
#     pessoa.append (registropessoa)

#     print(f"Nome: {nome}, a sua altura é de {altura} e seu peso é de {peso}, seu sexo {sexo}")

# #Objeto pessoa
# class cpessoa:
#     def __init__ (self, nome, altura, peso, sexo):
#         self.nome = nome
#         self.altura = altura
#         self.peso = peso    
#         self.sexo = sexo
#     def calcular_imc (self):
#         print(f"Calcular o imc para{self.nome}: Altura = {self.altura:.2f}. peso = {self.peso:.2f}")
#         return self.peso / (self.altura ** 2)

# def cpessoaid ():
#     if not pessoa:
#         print("Sem registro")
#         return
#     for i, p in enumerate(pessoa, start = 0): 
#         print(f"{i} Pessoa é {p.nome} altura é {p.altura}, o peso é {p.peso}")
    


#Menu
# flag = False
# while flag != True:
#     print("\nMenu: ")
#     print("1 - Registrar nova pessoa ")
#     print("2 - mostrar registros ")
#     print("3 - Calcular IMC ")

#     menu = input("Escolha uma opção")
#     if menu == "1":
#         registro()
#     elif menu == "2":
#         cpessoaid()

#     elif menu == "3":
#         if not pessoa:
#             print("Não temos registro")
#         else:
#             cpessoaid()

#             try:
#                 idpessoa = int(input("Qual Id de Registro deseja calcular"))
#                 if 0<= idpessoa < len(pessoa):
#                     imc = pessoa[idpessoa].calcular_imc()
#                     print(f"IMC seu {pessoa[idpessoa].nome}: {imc:.2f}")
#                     if imc < 18.5:
#                         print("Abaixo do peso")
#                     elif 18.5 <= imc <= 24.9:
#                         print("Peso Normal")
#                     elif 25.0 <= imc <= 29.9:
#                         print("Sobrepeso")
#                     elif 30.0 <= imc <= 34.9:
#                         print("obesidade 1")
#                 else:
#                     print("ID Invalido")
#             except ValueError:
#                 print("Entrada  Invalida")


# # 3- Conversor de Temperatura
# # Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
# # O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

# # 4- Verificador de Ano Bissexto

# # Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
# # Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.