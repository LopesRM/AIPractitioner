import random


palavras = ["cost explorer", "princing calculator", "elastick block storage", "kinesis", "aws", "standart storage system", "athena", "rekognition", "elastic Files System", "kubernet", "docker", "internet of core", "polly","lex", "cloud formation", "cloudfront", "locais de borda", "organizations", "tower control", "artifact",]
palavra_secreta = random.choice(palavras)

tentativas = 6
letras_certas = set()
letras_erradas = set()

while tentativas > 0:
    palavra_mostrada = "".join([letra if letra in letras_certas else "_" for letra in palavra_secreta])
    print(f"\nPalavra: {palavra_mostrada}")
    print(f"Tentativas Restantes: {tentativas}")

    if "_" not in palavra_mostrada:
        print("Venceu")
        break
    tentativa = input("Digite uma letra: ").lower()

    if tentativa in letras_certas or tentativa in letras_erradas:
        print("Você usou essa letra")
        continue

    if tentativa in palavra_secreta:
        letras_certas.add(tentativa)
    else:
        letras_erradas.add(tentativa)
        tentativas -=1
        print("Letra Errada!")

if tentativas == 0:
    print(f"\nVoce perdeu a palavra era: {palavra_secreta}")