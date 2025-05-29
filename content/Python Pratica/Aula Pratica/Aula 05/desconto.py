produto = float(input("Qual valor do produto: "))
desconto = float(input("Qual valor do desconto: "))

precofinal = ((produto * desconto)/100)
precofinal2 = (produto - precofinal)
print(f"Seu produto ficou com o desconto de {precofinal} ficando em {precofinal2}")