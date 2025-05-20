#Calculadora de Preço
produtos = []
carrinho = []

#Cadastrar Produto
def cadastroproduto ():
    nome = input("Nome do Produto: ")
    preco = int(input("Preço: "))
    meuproduto = produto(preco,nome)
    produtos.append(meuproduto)



#Catalogo
def showproduto ():
    id = 0
    for produto in produtos:
        id = (id+1)
        print (f"{id} {produto.nome} {produto.preco}")

def showcart ():
    if not carrinho:
        print("Seu carrinho esta vazio.")
        return
    
    print("\nSeu carrinho tem os seguintes intes: ")
    for i, item in enumerate(carrinho, start = 1):
        print (f"Você tem no seu carrinho os seguintes itens: {i} {item.nome} preço {item.preco:.2f}")
        
    
#Registro objeto
class produto: 
    def __init__ (self,preco,nome):
        self.nome = nome
        self.preco = preco
#Menu
flag = False
while flag != True:
        
    menu = int(input("\n 1 - Cadastra Produto \t\n 2 - Sair \t\n 3 - Catalago \t\n 4 - Add Carrinho: \t\n 5 - Mostrar Carrinho: \t\n 6 - Finalizar Compra"))
    if menu == 1:
        cadastroproduto()
        print (produtos [0].nome)
    elif menu == 2:
        flag = True
    elif menu == 3:
        showproduto()
    elif menu == 4:
        addcart = int(input("Qual ID do produto: "))
        produtinho = produto (produtos [addcart -1].preco,produtos [addcart -1].nome)
        quantidadecart = int(input("Quantos produtos: "))
        produtinho.preco *= quantidadecart
        carrinho.append(produtinho)
        print (produtinho.preco)
    elif menu == 5:
        showcart()
    