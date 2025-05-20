#Pessoa
pessoas = []

def pessoacadastro():
    nome = input("Nome: ")
    idade = float(input("Sua Idade: "))
    minhapessoa = pessoa(nome, idade)
    pessoas.append(minhapessoa)

def showpessoa():
    id = 0
    for pessoa in pessoas:
        id = (id+1)
        print(f"{id} Nome é {pessoa.nome} sua idade é de: {pessoa.idade}")


class pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

flag = False
while flag !=True:
    
    menu = int(input("\t\n 1 - Cadastrar Pessoa \t\n 2 - Verificar idade: "))
    if menu == 1:
        pessoacadastro()
    elif menu == 2:
        showpessoa()
        addcheck = int(input("Qual é o ID da pessoa: ")) -1

        if 0<= addcheck < len(pessoas):

            pessoinha = pessoas[addcheck].idade
            if pessoinha >= 18:
                print("Maior de idade")
            else:
                print("Menor de Idade")
        