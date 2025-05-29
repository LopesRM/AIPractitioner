import requests
from datetime import datetime

def cotacao_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        cotacao = dados[f"{moeda}BRL"]
        return f"""
        Moeda:{moeda} para BRL
        valor: R$ {float(cotacao['bid']):.2f}
        maxima: R$ {float(cotacao['high']):.2f}
        minima: R$ {float(cotacao['low']):.2f}
        data/hora: {datetime.fromtimestamp(int(cotacao["timestamp"]))}
        """
    except requests.exceptions.RequestException as e:
        return f"Erro ao obter a cotação: {e}"
    except KeyError:
        return "Moeda não encontrada ou dados inválidos."
    
def main():
    moeda = input("Digite a sigla da moeda (ex: USD, EUR, BTC): ").upper()
    print("\nObtendo cotação...")
    resultado = cotacao_moeda(moeda)
    print(resultado)

if __name__ == "__main__":
    main()

