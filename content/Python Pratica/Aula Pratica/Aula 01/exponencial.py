# Este programa calcula o volume de uma caixa retangular

# # Solicita as dimensões da caixa ao usuário
# comprimento = 12
# largura = 14
# altura = 20

# # Calcula o volume da caixa
# volume = comprimento * largura * altura

# # Exibe o resultado
# print(f"O volume da caixa é {volume} cm³")

try:
    numero_a = float(input("Numero Base "))
    numero_b = float(input("Qual expoente "))
except ValueError:
    print("Por favor digitar apenas numeros")

resultado = numero_a**numero_b
print (f"O Resultado da expoenciação de {numero_a} com expoente {numero_b} é de {resultado}: ")