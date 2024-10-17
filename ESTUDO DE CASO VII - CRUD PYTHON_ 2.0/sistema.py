from database import Database

print("Bem vindo ao SysCad")
print("Selecione uma opção, X para sair: ")
print(" 1 -  Cadastrar: ")
print(" 2 -  Listar: ")
print(" 3 -  Deletar: ")
print(" 4 -  Atualizar: ")
op = int(input("Opção: "))

def mostrar_menu():
    print("Selecione uma opção, X para sair: ")
    print(" 1 -  Cadastrar: ")
    print(" 2 -  Listar: ")
    print(" 3 -  Deletar: ")
    print(" 4 -  Atualizar: ")


while op != "X":
    banco = Database()
    if op == 1:
        cad = input("Cadastrar Pessoa?? S/N").upper()
        while cad != 'N':
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu CPF: ")
            email = input("Digite seu email: ")
            prof = input("Digite sua profissão: ")

            dados = (nome,cpf,email,prof)
            banco = Database()
            banco.cadastrar_pessoa(dados)
            cad = input("Cadastrar outra Pessoa?? S/N").upper()
    
    elif op == 2:
        lista = banco.listar_pessoa()
        for item in lista:
            print(item)
        
        mostrar_menu()
        op = int(input("Opção: "))
    
    elif op == 3:
        deletar = input("Deseja deletar algum indiviu da vida? ")
        if deletar == "S":
            id_pessoa = int(input("Digite o id do Peao: "))
            result = banco.deletar_pessoa(id_pessoa)
            if result == "OK":
                print("Individuo deletado com sucesso!!!")
                novalista = banco.listar_pessoa()
                for item in novalista:
                    print(item)
        mostrar_menu()
        op = int(input("Opção: "))


    elif op == 4:
        atualizar = input("Deseja atualizar algum indiviu da vida? (S/N) ").upper()
        if atualizar == "S":
            id_pessoa = int(input("Digite o id do Peao: "))
            nome = input("Digite o novo nome: ")
            cpf = input("Digite o novo CPF: ")
            email = input("Digite o novo email: ")
            prof = input("Digite a nova profissão: ")

            dados = (nome, cpf, email, prof)

            result = banco.atualizar_pessoa(id_pessoa, dados)
            if result == "OK":
                print("Individuo atualizado com sucesso!!!")
                novalista = banco.listar_pessoa()
                for item in novalista:
                    print(item)
        mostrar_menu()
        op = int(input("Opção: "))

print("Programa finalizado!")
