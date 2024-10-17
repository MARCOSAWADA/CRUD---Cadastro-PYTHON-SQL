from database import Database

op = input("Cadastrar Pessoa?? S / N ").upper()

while op != 'N':
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    senha = input("Digite o sua senha: ")
    avatar = input("Digite o seu avatar: ")
    sexo = input("Digite o seu sexo: ")


    dados = (nome, email, senha, avatar, sexo)
    banco = Database()
    banco.cadastrar_pessoa(dados)
    op = input("CADASTRAR OUTRA PESSOA?? S / N ").upper()

print("Programa Finalizado!")

