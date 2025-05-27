import datetime

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    data_atual = ano_atual - ano_nascimento
    idade_em_dias = data_atual * 365
    return idade_em_dias

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade_em_dias = calcular_idade_em_dias(ano_nascimento)
print(f"Sua idade em dias é: {idade_em_dias} dias")