from database import Database

op = input("Cadastrar Pessoa?? S/N: ").upper()

while op != 'N':
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    email = input("Digite seu email: ")
    prof = input("Digite sua profissão: ")



    # dados = (nome,cpf,email,prof)
    # banco = Database()
    # banco.cadastrar_pessoa(dados)

#     op = input("Cadastrar outra Pessoa?? S/N").upper()

# print("Programa finalizado!")

# ___________________________________________________________________

    # result=banco.cadastrar_pessoa(dados)
    # if result:
    #     print("CaDasTrAdo CoM SuCeSso")

#     op = input("Cadastrar outra Pessoa?? S/N").upper()

# print("Programa finalizado!")

# ___________________________________________________________________

#     dados = (nome,cpf,email,prof)
#     banco = Database()
#     banco.cadastrar_pessoa(dados)

#     lista = banco.lista_pessoa()
#     for item in lista:
#         print(item)

#     op = input("Cadastrar outra Pessoa?? S/N").upper()

# print("Programa finalizado!")

# ___________________________________________________________________


    dados = (nome,cpf,email,prof)
    banco = Database()
    banco.cadastrar_pessoa(dados)

    lista = banco.listar_pessoa()
    for item in lista:
        print(item)

    deletar = input("Deseja deletar algum vilão?: ")
    if deletar == "S":
        id_pessoa = int(input("Digite o id do Vilão: "))
        result = banco.deletar_pessoa(id_pessoa)
        if result == "OK":
            print("Vilão deletado com sucesso!!!")
            novalista = banco.listar_pessoa()
            for item in novalista:
                print(item)


    op = input("Cadastrar outro Vilão?? S/N: ").upper()

print("Programa finalizado!")




# ___________________________________________________________________