from database import Database

op = input("Cadastrar Produtos?? S / N ").upper()

while op != 'N':
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a sua descricao: ")
    preco = input("Digite o seu preço: ")


    dados = (nome, descricao, preco)
    banco = Database()
    banco.cadastrar_produtos(dados)
    op = input("CADASTRAR OUTRO PRODUTO?? S / N ").upper()

print("Programa Finalizado!")
