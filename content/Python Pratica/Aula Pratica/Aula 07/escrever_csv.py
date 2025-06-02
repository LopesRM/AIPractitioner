# import csv

# def escrever_csv(nome_arquivo, dados):
#     try:
#         with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
#             escritor = csv.writer(arquivo_csv)
#             escritor.writerow(['Nome', 'Idade', 'Cidade'])
#             for linha in dados:
#                 escritor.writerow(linha)
#         print(f"Dados salvos em {nome_arquivo}")
#     except Exception as e:
#         print(f"Erro ao salvar o arquivo: {e}")

# dados = [
#     ['Ana', 28, 'Rio de Janeiro'],
#     ['Pedro', 34, 'São Paulo'],
#     ['Maria', 30, 'Salvador']
# ]

# if __name__ == "__main__":
#     nome_arquivo = input("Digite o nome do arquivo CSV: ").strip()
#     escrever_csv(nome_arquivo, dados)
import csv
import os

def escrever_csv(caminho_completo, dados):
    try:
        diretorio = os.path.dirname(caminho_completo)
        if diretorio and not os.path.exists(diretorio):
           os.makedirs(diretorio)

        with open(caminho_completo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome', 'Idade', 'Cidade'])
            for linha in dados:
                escritor.writerow(linha)
            print(f"Dados salvos em {caminho_completo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")
dados = [
    ['Ana', 28, 'Rio de Janeiro'],
    ['Pedro', 34, 'São Paulo'],
    ['Maria', 30, 'Salvador']
]
if __name__ == "__main__":
    caminho_base = r"git/content/Python Pratica/Aula Pratica/Aula 07/"
    nome_arquivo = input("Digite o nome do arquivo CSV (com caminho completo): ").strip()
    caminho_completo = os.path.join(caminho_base, nome_arquivo)
    
    escrever_csv(nome_arquivo, dados)