import random

#jogo de adivinhar numero

def jogo_adivinhacao():
    numero_secreto=random.randint(1,100)
    tentativas = 0

    print(" === Jogo de Adivinhação ===")
    print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")

    while True:
        palpite = int(input("Seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Chutou Baixo")

        elif palpite > numero_secreto:
            print("Chutou alto")

        else:
            print(f"Parabens você acertou em {tentativas} Tentativas!")
            break
            

jogo_adivinhacao()


