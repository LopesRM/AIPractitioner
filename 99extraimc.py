#IMC Calculadora
#Array de nome, altura, peso e sexo
pessoa = []

#Registro
def registro ():
    nome = input("Seu Nome: ")
    try:
        altura = float(input("Sua altura: (00.00)"))
        peso =  float(input("Seu peso: (00.00)"))
    except ValueError:
        print("Erro")
        return
    
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
    def __init__ (self, nome, altura, peso, sexo):
        self.nome = nome
        self.altura = altura
        self.peso = peso    
        self.sexo = sexo
    def calcular_imc (self):
        print(f"Calcular o imc para{self.nome}: Altura = {self.altura:.2f}. peso = {self.peso:.2f}")
        return self.peso / (self.altura ** 2)

def cpessoaid ():
    if not pessoa:
        print("Sem registro")
        return
    for i, p in enumerate(pessoa, start = 0): 
        print(f"{i} Pessoa é {p.nome} altura é {p.altura}, o peso é {p.peso}")
    


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
        cpessoaid()

    elif menu == "3":
        if not pessoa:
            print("Não temos registro")
        else:
            cpessoaid()

            try:
                idpessoa = int(input("Qual Id de Registro deseja calcular"))
                if 0<= idpessoa < len(pessoa):
                    imc = pessoa[idpessoa].calcular_imc()
                    print(f"IMC seu {pessoa[idpessoa].nome}: {imc:.2f}")
                    if imc < 18.5:
                        print("Abaixo do peso")
                    elif 18.5 <= imc <= 24.9:
                        print("Peso Normal")
                    elif 25.0 <= imc <= 29.9:
                        print("Sobrepeso")
                    elif 30.0 <= imc <= 34.9:
                        print("obesidade 1")
                else:
                    print("ID Invalido")
            except ValueError:
                print("Entrada  Invalida")




                