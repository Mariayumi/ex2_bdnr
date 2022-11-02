from bson import ObjectId
import pymongo
from pymongo.server_api import ServerApi

client = pymongo.MongoClient("mongodb+srv://Mariana:MatPetErAt@cluster0.jgkawuu.mongodb.net/test")
db = client.test

global mydb
mydb = client.mercadolivre


## SEARCH ##
def searchVendedores():
    global mydb
    mycol = mydb.vendedor

    print("\n##### VENDEDORES #####")
    vendedores = mycol.find({})
    vendedoreslista = []
    for vendedor in vendedores:
        vendedoreslista.append(vendedor)
    return print(vendedoreslista)

#searchVendedores()

def searchUsuarios():
    global mydb
    mycol = mydb.usuario

    print("\n##### USUÁRIOS #####")
    usuarios = mycol.find({})
    usuarioslista = []
    for usuario in usuarios:
        usuarioslista.append(usuario)
    return print(usuarioslista)

#searchUsuarios()

def searchProdutos():
    global mydb
    mycol = mydb.produto

    print("\n##### PRODUTOS #####")
    produtos = mycol.find({})
    produtoslista = []
    for produto in produtos:
        produtoslista.append(produto)
    return print(produtoslista)

#searchProdutos()

def searchCompras():
    global mydb
    mycol = mydb.compra

    print("\n##### COMPRAS ####")
    compras = mycol.find({})
    compraslista = []
    for compra in compras:
        compraslista.append(compra)
    return print(compraslista)

#searchCompras()


## FIND ##
def findVendedor(cnpj):
    global mydb
    mycol = mydb.vendedor

    print("\n##### VENDEDOR ENCONTRADO #####")
    myquery = {"cnpj": {"$eq": cnpj}}
    mydoc = mycol.find(myquery)
    for result in mydoc:
        print(result)

#findVendedor("12.345.678/0001-00")

def findUsuario(cpf):
    global mydb
    mycol = mydb.usuario

    print("\n##### USUÁRIO ENCONTRADO #####")
    myquery = {"cpf": {"$eq": cpf}}
    mydoc = mycol.find(myquery)
    for result in mydoc:
        print(result)

#findUsuario("987.654.321.09")

def findProduto(nome):
    global mydb
    mycol = mydb.produto

    print("\n##### PRODUTO ENCONTRADO #####")
    myquery = {"nome": {"$eq": nome}}
    mydoc = mycol.find(myquery)
    for result in mydoc:
        print(result)

#findProduto("API")

def findCompra(usuario):
    global mydb
    mycol = mydb.compra

    print("\n##### COMPRA ENCONTRADA #####")
    myquery = {"usuário": {"$eq": usuario}}
    mydoc = mycol.find(myquery)
    for result in mydoc:
        print(result)

#findCompra("Gerson")


## INSERT ##
def insertUsuario(nome, cpf, email, rua, cidade, estado, bairro):
    global mydb
    mycol = mydb.usuario

    print("\n##### INSERT USUARIO #####")
    mydict = {"nome": nome, "cpf": cpf, "email": email, "endereco": [{"rua": rua, "bairro": bairro, "cidade": cidade, "estado": estado}]}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

#insertUsuario("Diogo Branquinho", "123.456.789.01", "diogo.branquinho@email.com", "Rua Acaraú", "Bela Vista", "Araras", "SP")

def insertVendedor(nome, cnpj, email, rua, cidade, estado, bairro):
    global mydb
    mycol = mydb.vendedor

    print("\n##### INSERT VENDEDOR #####")
    mydict = {"nome": nome, "cnpj": cnpj, "email": email, "endereco": [{"rua": rua, "bairro": bairro, "cidade": cidade, "estado": estado}]}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)

#insertVendedor("Maria Clara", "12.345.678/0001-00", "maria.clara@email.com", "Rua Maestro Alexandre", "Planalto", "Santa Cruz do Capibaribe", "PE")

def insertProduto(nome, preco, descricao, quantidade, vendedor):
    global mydb
    columnVendedores = mydb.vendedor
    columnProdutos = mydb.produto
    findVendedor = columnVendedores.find({"nome": {"$eq": vendedor}}, 
    {
        "_id": 1,
        "nome": 1
    })

    print("\n##### INSERT PRODUTO #####")
    createDict = {}
    for fornecedor in findVendedor:
        createDict.update(fornecedor)
        mydict = {"nome": nome, "preco": preco, "descricao": descricao, "quantidade": quantidade, "vendedor": createDict}
        x = columnProdutos.insert_one(mydict)
        print(x.inserted_id)

#insertProduto("API", "50.000,00", "Nessa metodologia, o objetivo de ensino é alcançar um alto grau de aprendizado por meio de pesquisas profundas e atividades práticas, sendo estas as responsáveis pelo desenvolvimento e o desempenho do aluno.", "1", "Maria Clara")

def insertCompra(precoTotal, data, formaPgt, produto, usuario):
    global mydb
    mycol = mydb.compra
    columnProdutos = mydb.produto
    findProduto = columnProdutos.find({"nome": {"$eq": produto}}, 
    {
        "_id": 1,
        "nome": 1,
        "vendedor": 1
    })

    print("\n##### INSERT COMPRA #####")
    produtoDict = {}
    for fornecedor in findProduto:
        produtoDict.update(fornecedor)
        mydict = {"preço total": precoTotal, "data da compra": data, "forma pagamento": formaPgt, "produto": produtoDict, "usuário": usuario}
        x = mycol.insert_one(mydict)
        print(x.inserted_id)

#insertCompra("R$ 1200", "01/11/2022", "Débito", "API", "Sakaue")


## UPDATE ##
def updateUsuario(id, nome, cpf, email, rua, cidade, estado, bairro):
    global mydb
    mycol = mydb.usuario

    print("\n##### UPDATE USUÁRIO #####")
    objInstance = ObjectId(id)
    myquery = {"_id": objInstance}
    newvalues= {"$set": {"nome": nome, "cpf": cpf, "email": email, "endereco": [{"rua": rua, "bairro": bairro, "cidade": cidade, "estado": estado}]}}
    mycol.update_one(myquery, newvalues)

#updateUsuario("6361122621196fceba920354", "Gerson", "987.654.321.09", "prof.gerson@email.com", "Rua 1", "Colônia Antônio Aleixo", "Manaus", "AM")

def updateVendedor(id, nome, cnpj, email, rua, cidade, estado, bairro):
    global mydb
    mycol = mydb.vendedor

    print("\n##### UPDATE VENDEDOR #####")
    objInstance = ObjectId(id)
    myquery = {"_id": objInstance}
    newvalue = {"$set": {"nome": nome, "cnpj": cnpj, "email": email, "endereco": [{"rua": rua, "bairro": bairro, "cidade": cidade, "estado": estado}]}}
    mycol.update_one(myquery, newvalue)

#updateVendedor("6361154c82a76298c27e2998", "Taís Salomão", "102.398.475.60", "tais_salomao@email.com", "Rua da Imprensa", "Monte Castelo", "Campo Grande", "MS")

def updateProduto(id, nome, preco, quantidade, descricao, vendedor):
    global mydb
    mycol = mydb.produto
    columnVendedores = mydb.vendedor
    findVendedor = columnVendedores.find({"nome": {"$eq": vendedor}}, 
    {
        "_id": 1,
        "nome": 1
    })

    print("\n##### UPDATE PRODUTO #####")
    createDict = {}
    for fornecedor in findVendedor:
        createDict.update(fornecedor)
        objInstance = ObjectId(id)
        myquery = {"_id": objInstance}
        newvalue = {"$set": {"nome": nome, "preco": preco, "descricao": descricao, "quantidade": quantidade, "vendedor": createDict}}
        mycol.update_one(myquery, newvalue)

#updateProduto("63613245fa706a8e279a9976", "Aprendizagem por Projeto Integrado", "55.000,00", "Metodologia de aprendizado", "3", "Matheus")


## DELETE ##
def deleteUsuario(id):
    global mydb
    mycol = mydb.usuario

    print("\n##### DELETE USUÁRIO #####")
    objInstance = ObjectId(id)
    myquery = {"_id": objInstance}
    mycol.delete_one(myquery)

#deleteUsuario("6361122621196fceba920356")

def deleteProduto(id):
    global mydb
    mycol = mydb.produto

    print("\n##### DELETE PRODUTO #####")
    objInstance = ObjectId(id)
    myquery = {"_id": objInstance}
    mycol.delete_one(myquery)

#deleteProduto("636134946254f079e64a6553")

def deleteVendedor(id):
    global mydb
    mycol = mydb.vendedor

    print("\n##### DELETE VENDEDOR #####")
    objInstance = ObjectId(id)
    myquery = {"_id": objInstance}
    mycol.delete_one(myquery)

#deleteVendedor("6361154c82a76298c27e2998")
