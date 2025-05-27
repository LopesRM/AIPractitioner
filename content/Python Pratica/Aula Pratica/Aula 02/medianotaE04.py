#######################
######## Média ########
#######################


# Calculadora de média escolar

# # Notas do aluno
# nota1 = 7.5
# nota2 = 8.0
# nota3 = 6.5

# # Cálculo da média
# media = (nota1 + nota2 + nota3) / 3

# # Exibição do resultado
# print("Notas do aluno:")
# print("Nota 1:", nota1)
# print("Nota 2:", nota2)
# print("Nota 3:", nota3)
# print("Média final:", round(media, 2))


# notaA = float(input("Nota A "))
# notaB = float(input("Nota B "))
# notaC = float(input("Nota C"))

# resultado_final = ((notaA + notaB + notaC)/3)

# print(f"resultado da nota A {notaA}, notaB{notaB}, notaC{notaC} ficou em {resultado_final:.2f}")

######################################################################################################

nota = 0
soma = 0
notas = []


while True:
    entrada = input("Digite uma nota ou (s) para sair: ")
    if entrada == "s":
        break
    try:
        valor = float(entrada)
        if valor <= 0:
            print("Digite nota maior que zero ou (s) para sair")
            continue
        notas.append(valor)
        soma += valor
        nota += 1
    except ValueError:
        print("Entrada invalida, digite numero ou (s) para sair")
        continue

if nota > 0:
    media = soma / nota
    print("\nNotas digitadas: ", notas)
    print("\ntotal da soma: ", soma)
    print("\nQuantidade de notas digitadas: ", nota)
    print("\nMédia dos valores: ", media)
    if media >= 7:
        print(f"A nota do aluno foi de {media:.2f} aluno aprovado")
    else:
        print(f"A nota do aluno foi de {media:.2f} aluno reprovado")
else:
    print("Nenhuma nota valida.")