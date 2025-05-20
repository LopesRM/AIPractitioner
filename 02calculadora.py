#soma e multiplicação

a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
c = float(input("Multiplicar por: "))

print (f"valor a {a} e o valor b {b} e multiplica {c} é igual {(a+b)*c}")

def multiplicacao (entrada, multiplicador):
    result = entrada * multiplicador
    return result
print (multiplicacao(a+b,c))