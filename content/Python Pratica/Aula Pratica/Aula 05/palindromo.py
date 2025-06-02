###################################################################
############################ Palindromo ###########################
###################################################################

def is_palindrome(s):
    s = s.lower()  # Converte para minúsculas
    s = ''.join(c for c in s if c.isalnum())  # Remove espaços e pontuação
    return s == s[::-1]  # Verifica se a string é igual à sua reversa

def main():
    frase = input("Digite uma frase: ")
    if is_palindrome(frase):
        print("A frase é um palíndromo.")
    else:
        print("A frase não é um palíndromo.")

if __name__ == "__main__":
    main()