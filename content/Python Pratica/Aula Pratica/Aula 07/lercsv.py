# import csv

# def ler_csv(nome_arquivo):
#     try:
#         with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
#             leitor = csv.reader(arquivo_csv)
#             for linha in leitor:
#                 print(linha)
#     except FileNotFoundError:
#         print("Arquivo não encontrado.")

# if __name__ == "__main__":
#     nome_arquivo = input("Digite o nome do arquivo CSV: ").strip()
#     ler_csv(nome_arquivo)

import csv
import os
from tkinter import filedialog, Tk

def selecionar_pasta():
    root = Tk()
    root.withdraw()
    pasta = filedialog.askdirectory(title="Selecione a pasta para salvar o arquivo CSV")
    return pasta

def listar_arquivos_CSV(pasta):
    arquivos = [arq for arq in os.listdir(pasta) if arq.lower().endswith('.csv')]
    if not arquivos:
        print("Nenhum arquivo CSV encontrado na pasta.")
        return None
    return arquivos

def selecionar_arquivo(arquivos):
    print("\nArquivos CSV encontrados:")
    for i, arquivo in enumerate(arquivos, 1):
        print(f"{i}. {arquivo}")
    while True:
        try:
            escolha = int(input("Selecione o número do arquivo que deseja ler: ")) - 1
            if 0 <= escolha < len(arquivos):
                return arquivos[escolha]
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def ler_csv(caminho_completo):
    try:
        with open(caminho_completo, 'r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            cabecalho = next(leitor)
            print("\n" +"|".join(cabecalho))
            print("-" * 30)
            for linha in leitor:
                print("|".join(linha))
        print(f"\Total de registros: {sum(1 for _ in open(caminho_completo)) - 1}")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
def main():
    print("=== Leitor de Arquivos CSV ===")
    pasta =selecionar_pasta()
    if not pasta:
        return
    arquivos = listar_arquivos_CSV(pasta)
    if not arquivos:
        return
    
    arquivo_selecionado = selecionar_arquivo(arquivos)
    caminho_completo = os.path.join(pasta, arquivo_selecionado)

    print(f"\nLendo arquivo: {arquivo_selecionado}")
    ler_csv(caminho_completo)
if __name__ == "__main__":
    main()  