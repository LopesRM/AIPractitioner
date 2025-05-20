#IMC Calculadora
#Array de nome, altura, peso e sexo
pessoa = []

#Registro
def registro ():
    nome = input("Seu Nome: ")
    altura = float(input("Sua altura: "))
    peso =  float(input("Seu peso: "))
    sexo = input("\t\n 1 - Masculino \t\n 2 - Feminino")
    
    if sexo == "1":
        sexo = "Masculino"
    elif sexo == "2":
        sexo = "Feminino"
    else:
        print("Opção invalida")
        return
    registropessoa = cpessoa(nome, altura, peso, sexo)
    pessoa.append (registropessoa)

    print(f"Nome: {nome}, a sua altura é de {altura} e seu peso é de {peso}, seu sexo {sexo}")

#Objeto pessoa
class cpessoa:
    def __init__ (self,nome, altura,peso, sexo):
        self.nome = nome
        self.altura = altura
        self.peso = peso    
        self.sexo = sexo

def cpessoaid ():
    id = 0
    for cpessoa in pessoa:
        id = (id+1)
        print (f"{id} {pessoa.nome} {pessoa.altura} {pessoa.peso}")

def calcular_imc (self):
    return self.peso / (self.altura **2)

#Menu
flag = False
while flag != True:
    print("\nMenu: ")
    print("1 - Registrar nova pessoa ")
    print("2 - mostrar registros ")
    print("3 - Calcular IMC ")

    menu = input("Escolha uma opção")
    if menu == "1":
        registro()
    elif menu == "2":
        for p in pessoa:
            print(F"Óla {p.nome}, sua altura é de {p.altura} seu peso é de {p.peso}, e seu sexo é {p.sexo}")
    elif menu == "3":
        idpessoa = int(input("Qual ID de Registro: ")) - 1
        cpessoaid = cpessoaid
        imc = pessoa[cpessoaid].calcular_imc()