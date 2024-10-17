from database import Database
banco = Database()

print("Bem vindo ao SysCad")
print("Selecione uma opção, X para sair: ")
print(" 1 -  Cadastrar: ")
print(" 2 -  Listar: ")
print(" 3 -  Deletar: ")
print(" 4 -  Atualizar: ")
op = input("Opção: ")

def mostrar_menu():
    print("Selecione uma opção, X para sair: ")
    print(" 1 -  Cadastrar: ")
    print(" 2 -  Listar: ")
    print(" 3 -  Deletar: ")
    print(" 4 -  Atualizar: ")

while True:
    if op == '1':
        nome = input("Digite seu nome: ")
        cpf = input("Digite seu CPF: ")
        email = input("Digite seu email: ")
        prof = input("Digite sua profissão: ")

        dados = (nome,cpf,email,prof)
        banco = Database()
        banco.cadastrar_pessoa(dados)
        cad = input("Cadastrar outra Pessoa?? S/N").upper()
        if cad == 'N':
            break

    elif op == '2':
        lista = banco.listar_pessoa()
        for item in lista:
            print(item)
        
        mostrar_menu()
        op = input("Opção: ")
        if op == 'N':
            break

    elif op == '3':
        deletar = input("Deseja deletar algum indiviu da vida? ").upper()
        if deletar == "S":
            id_pessoa = int(input("Digite o id do Peao: "))
            result = banco.deletar_pessoa(id_pessoa)
            if result == "OK":
                print("Individuo deletado com sucesso!!!")
                novalista = banco.listar_pessoa()
                for item in novalista:
                    print(item)
        mostrar_menu()
        op = input("Opção: ")
        if op == 'N':
            break

    
    elif op == '4':
        lista = banco.listar_pessoa()
        for item in lista:
            print(item)

        print("--" * 50)
        print("\n Qual usuário você deseja atualizar?")
        id_pessoa = input("Favor digite o ID: ")
        dados_para_alterar = banco.listar_pessoa_by_id(id_pessoa)
        nome = input("Digite o nome: ")
        cpf = input("Digite o cpf: ")
        email = input("Digite o email: ")
        prof = input("Digite a profissão: ")
        result = banco.atualizar_pessoa(dados_para_alterar[0], nome,cpf,email,prof)
        if result == True:
            print("Atualizado com sucesso!!")
        

        mostrar_menu()
        op = input("Opção: ")
        if op == 'N':
            break