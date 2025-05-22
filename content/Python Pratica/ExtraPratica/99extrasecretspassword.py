import random
import string
senhas = []

def randompassword (tamanho, incluir_numeros=True, incluir_simbolos=True):
    caracateres = string.ascii_letters

    if incluir_numeros:
        caracateres = string.digits

    if incluir_simbolos:
        caracateres = string.punctuation

    senha = "".join(random.choice(caracateres) for _ in range(tamanho))

    return senha

tamanho_senha = int(input("Digite o tamanho do password: "))
senha_gerada = randompassword(tamanho_senha)
print(f"Senha gerada: {senha_gerada}")
