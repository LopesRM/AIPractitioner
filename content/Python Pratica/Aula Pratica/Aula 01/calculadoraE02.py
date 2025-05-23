# Este programa soma dois números inseridos pelo usuário

# # Solicita ao usuário que insira dois números
# numero1 = 12
# numero2 = 14

# # Calcula a soma dos números
# soma = numero1 + numero2

# # Exibe o resultado
# print(f"A soma de {numero1} e {numero2} é: {soma}")



#soma e multiplicação
try:
    numero_a = float(input("Numero A "))
    numero_b = float(input("Numero B "))
except ValueError:
    print("Por favor digitar apenas numeros")

resultado = numero_a + numero_b
print (f"O Resultado da soma de {numero_a} mais o {numero_b} é de {resultado}: ")