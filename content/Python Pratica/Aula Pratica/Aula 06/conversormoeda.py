import requests
from datetime import datetime

def cotacao_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        cotacao = dados[f"{moeda}BRL"]
        valor_atual = float(cotacao['bid'])
        return {
            "moeda": moeda,
            "valor": valor_atual,
            "maxima": float(cotacao['high']),
            "minima": float(cotacao['low']),
            "timestamp": int(cotacao["timestamp"])
        }

    except requests.exceptions.RequestException as e:
        return f"Erro ao obter a cotação: {e}"
    except KeyError:
        return "Moeda não encontrada ou dados inválidos."

def calcular_valor_em_reais(cotacao, quantidade):
    if isinstance(cotacao,dict):
        return quantidade * cotacao["valor"]
    return None
def main():
    moeda = input("Digite a sigla da moeda (ex: USD, EUR, BTC): ").upper()
    print("\nObtendo cotação...")
    resultado = cotacao_moeda(moeda)
    print(resultado)

    if isinstance(resultado, dict):
        print(f"""
              Moeda: {resultado['moeda']} para BRL
              Valor atual: R$ {resultado['valor']:.2f}
                Máxima: R$ {resultado['maxima']:.2f}
                Mínima: R$ {resultado['minima']:.2f}
                Data/hora: {"data_hora"}""")
        try:
            quantidade = float(input(f"Quantos {resultado['moeda']} você deseja converter? "))
            valor_em_reais = calcular_valor_em_reais(resultado, quantidade)
            print(f"\n {quantidade} {resultado['moeda']} equivalem a R$ {valor_em_reais:.2f}")
        except ValueError:
            print("Erro: Por favor, digite um número válido para a quantidade.")
    else:
        print(resultado)


if __name__ == "__main__":
    main()



