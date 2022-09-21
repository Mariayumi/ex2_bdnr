import pymongo
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://Mariana:matam1234@cluster0.jgkawuu.mongodb.net/mercadolivre")
db = client.test

global mydb
mydb = client.mercadolivre

###INSERT###
def insertVendedor(nome,email,cnpj):
    #Insert Vendedor
    global mydb
    mycol = mydb.vendedor
    print("\n####INSERT VENDEDOR####")
    mydict = { "nome": nome,"email":email,"cnpj":cnpj}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def insertUsuario(nome,email,senha,endereco):
    #Insert Usuario
    global mydb
    mycol = mydb.usuario
    print("\n####INSERT USUARIO####")
    mydict = { "nome": nome,"email":email,"senha":senha,"endereco":endereco,"favoritos": []}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

def insertProduto(nome,preco,descricao, quant_dispo):
    #Insert Produto
    global mydb
    mycol = mydb.produto
    print("\n####INSERT PRODUTO####")
    mydict = {"nome": nome, "preco":preco,"descricao":descricao, "quantidade disponível": quant_dispo}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

### SORTS ###
def sortUsuarios():
    global mydb
    colunaUsu = mydb.usuario
    mydoc = colunaUsu.find({}, {
        "nome": 1,
        "_id": 1,
    }).sort("nome")
    for result in mydoc:
        print(result)

def sortVendedores():
    global mydb
    colunaVend = mydb.vendedor
    mydoc = colunaVend.find({}, {
        "nome": 1,
        "_id": 1,
    }).sort("nome")
    for result in mydoc:
        print(result)

def sortProdutos():
    global mydb
    colunaProd = mydb.produto
    mydoc = colunaProd.find({}, {
        "nome": 1,
        "_id": 1,
    }).sort("nome")
    for result in mydoc:
        print(result)

### DELETE ###
def deleteUsuario(alvo):
    global mydb
    colunaUsu = mydb.usuario
    objInstance = ObjectId(alvo)
    myquery = {"_id": objInstance}
    colunaUsu.delete_one(myquery)

def deleteProduto(alvo):
    global mydb
    colunaProd = mydb.produto
    objInstance = ObjectId(alvo)
    myquery = {"_id": objInstance}
    colunaProd.delete_one(myquery)

def deleteVendedor(alvo):
    global mydb
    colunaVend = mydb.vendedor
    objInstance = ObjectId(alvo)
    myquery = {"_id": objInstance}
    colunaVend.delete_one(myquery)

### QUERY ###
def queryUsuario(alvo):
    global mydb
    mycol = mydb.usuario
    myquery = {"nome": {"$eq": alvo}}
    mydoc = mycol.find(myquery)
    for result in mydoc:
        print(result)

def queryVendedor(alvo):
    global mydb
    colunaVend = mydb.vendedor
    myquery = {"nome": {"$eq": alvo}}
    mydoc = colunaVend.find(myquery)
    for result in mydoc:
        print(result)

def queryProduto(alvo):
    global mydb
    colunaProd = mydb.produto
    myquery = {"nome": {"$eq": alvo}}
    mydoc = colunaProd.find(myquery)
    for result in mydoc:
        print(result)

def show_menu():
    print("""
    1- Lista de usuários \n
    2- Lista de vendedores \n
    3- Lista de produtos \n
    4- Adicionar novo usuário \n
    5- Adicionar novo vendedor \n
    6- Adicionar novo produto \n
    7- Atualizar usuário \n
    8- Atualizar vendedor \n
    9- Atualizar produto \n
    10- Deletar usuário \n
    11- Deletar vendedor \n
    12- Deletar produto \n
    13- Procurar usuário \n
    14- Procurar vendedor \n
    15- Procurar produto \n
    16- Sair \n
    """)

    loop = True
    while loop:
        select = input("Escolha a ação desejada: ")
        if select == "1":
            sortUsuarios()
        elif select == "2":
            sortVendedores()
        elif select == "3":
            sortProdutos()
        elif select == "4":
            nome = input("Nome do usuário: ")
            email = input("E-mail do usuário: ")
            senha = input("Senha do usuário: ")
            estado = input("Estado: ")
            cidade = input("Cidade: ")
            rua = input("Rua: ")
            bairro = input("Bairro: ")
            numero = input("Número: ")
            insertUsuario(nome,email,senha,{"estado": estado, "cidade": cidade, "rua": rua, "bairro": bairro, "numero": numero})
        elif select == "5":
            nome = input("Nome do vendedor: ")
            email = input("E-mail do vendedor: ")
            cnpj = input("Cnpj do vendedor: ")
            insertVendedor(nome, email, cnpj)
        elif select == "6":
            nome = input("Nome do produto: ")
            preco = input("Preço do produto: ")
            descricao = input("Descrição do produto: ")
            quant_dispo = input("Quantidade disponível do produto: ")
            insertProduto(nome, preco, descricao, quant_dispo)
        elif select == "10":
            sortUsuarios()
            alvo = input("Id do usuário a ser excluído: ")
            deleteUsuario(alvo)
        elif select == "11":
            sortVendedores()
            alvo = input("Id do vendedor a ser excluído: ")
            deleteVendedor(alvo)
        elif select == "12":
            sortProdutos()
            alvo = input("Id do produto a ser excluído: ")
            deleteProduto(alvo)
        elif select == "13":
            alvo = input("Nome do usuário: ")
            queryUsuario(alvo)
        elif select == "14":
            alvo = input("Nome do vendedor: ")
            queryVendedor(alvo)
        elif select == "15":
            alvo = input("Nome do produto: ")
            queryProduto(alvo)
        elif select == "16":
            loop = False

show_menu()