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


produto = float(input("Qual valor do produto: "))
desconto = float(input("Qual valor do desconto: "))

precofinal = ((produto * desconto)/100)
precofinal2 = (produto - precofinal)
print(f"Seu produto ficou com o desconto de {precofinal} ficando em {precofinal2}")