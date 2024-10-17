import mysql.connector

class Database():
    def __init__(self, banco = "cadastro") -> None:
        self.banco = banco
    
    # def connect(self):
    #     self.conn = mysql.connector.connect(host='localhost', database='empresa', user='root', password='')

    def connect(self):
        self.conn = mysql.connector.connect(host='10.38.0.73', database='Rede_Social', user='devweb', password='suporte@22')

        if self.conn.is_connected():
            self.cursor= self.conn.cursor()
            print("CONECTADO COM SUCESSO")
        else:
            print("ALGO DEU ERRADO...")



    # def cadastrar_pessoa(self):
    #     self.connect()
    #     try:
    #         tupla = ("MKS", "123456", "mks@gmail.com", "Desenvolvedor")
    #         self.cursor.execute('INSERT INTO pessoa (nome,cpf,email,profissao) values (%s, %s, %s, %s)', tupla)
    #         self.conn.commit()
    #         print('CADASTRADO COM SUCESSO')
    #     except Exception as err:
    #         print('ERRO AO CADASTRAR')
    #         print(err)



    # 1º PARTE - PARA ADICIONAR PESSOAS sem ter criado o main.py - somente ("self)"
    # def cadastrar_pessoa(self):
    #     self.connect()
    #     try:
    #         tupla = ("MK", "mks@gmail.com", "123456", "imagem.png", "M")
    #         self.cursor.execute('INSERT INTO usuarios (Nome, Email, Senha, Avatar, Sexo) values (%s, %s, %s, %s, %s)', tupla)
    #         self.conn.commit()
    #         print('CADASTRADO COM SUCESSO')
    #     except Exception as err:
    #         print('ERRO AO CADASTRAR')
    #         print(err)

# ________________________________________________________________________________________________________________________________

    # 2º PARTE - PARA ADICIONAR PESSOAS NO MAIN.PY - quando já criado o main.py tem que acrescentar o dados depois do (self,dados)
    # def cadastrar_pessoa(self, dados):
    #     self.connect()
    #     try:
    #         tupla = ("MK", "mks@gmail.com", "123456", "imagem.png", "M")
    #         self.cursor.execute('INSERT INTO usuarios (Nome, Email, Senha, Avatar, Sexo) values (%s, %s, %s, %s, %s)', dados)
    #         self.conn.commit()
    #         print('CADASTRADO COM SUCESSO')
    #     except Exception as err:
    #         print('ERRO AO CADASTRAR')
    #         print(err)

    #     self.close_connection()

# ________________________________________________________________________________________________________________________________

#   3º PARTE - PARA ADICIONAR PESSOAS sem ter criado o main.py - somente ("self)"

    def cadastrar_produtos(self):
        self.connect()
        try:
            dados = ("COCA-COLA 2L", "Refrigerante de cola", "7.50")
            self.cursor.execute('INSERT INTO produtos (nome_produto, descricao, preco) values (%s, %s, %s)', dados)
            self.conn.commit()
            print('CADASTRADO COM SUCESSO')
        except Exception as err:
            print('ERRO AO CADASTRAR')
            print(err)

        self.close_connection()


    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("CONEXÃO ENCERRADA")


if __name__ == "__main__":

    conexao = Database()
    conexao.connect()

    # 1º parte do cadastro
    conexao.close_connection()

    # 2º parte do cadastro
    # conexao.cadastrar_pessoa()

    # 3º parte do cadastro
    conexao.cadastrar_produtos()



