####################################################################
##########################  Gerar CEP  #############################
####################################################################

import requests

cep = input("Digite o CEP (somente números): ")
responsta = requests.get(f"https://viacep.com.br/ws/{cep}/json")
dados = responsta.json()
print("Logradouro",dados["logradouro"])
print("Bairro",dados["bairro"])
print("Cidade",dados["localidade"])
print("Estado",dados["uf"])
