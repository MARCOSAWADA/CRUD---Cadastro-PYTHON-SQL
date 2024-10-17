import mysql.connector

class Database():
    def __init__(self,banco = "empresa") -> None:
        self.banco = banco

    def connect(self):
        # self.conn = mysql.connector.connect(host='localhost',database='empresa',user='root',password='')
        self.conn = mysql.connector.connect(host='10.38.0.73', database='empresa2', user='devweb', password='suporte@22')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            print("CONECTADO COM SUCESSO")
        else:
            print("ALGO DEU ERRADO....")


# ___________________________________________________________________


    def cadastrar_pessoa(self, dados):
        self.connect()
        try:
            self.cursor.execute('INSERT INTO pessoa (nome,cpf,email,profissao) values (%s,%s,%s,%s)', dados)
            self.conn.commit()
            print('Cadastrado com sucesso!!!')
        except Exception as err:
            print('Erro ao cadastrar')
            print(err)
        
        self.close_connection()

# ___________________________________________________________________


    def listar_pessoa(self):
        self.connect()
        try:
            self.cursor.execute(""" SELECT * FROM pessoa """)
            result = self.cursor.fetchall()

            # print(result)

            # for item in result:
            #     print(item)

            return(result)
        
        except Exception as err:
            print(err)

        self.close_connection()

# ___________________________________________________________________

    def deletar_pessoa(self, id_pessoa):
        self.connect()
        try:
            self.cursor.execute(f'''DELETE FROM pessoa id={id_pessoa} ''')
            self.conn.commit()
            return "OK"
        except Exception as err:
            return err
            # print(err)
        
        self.close_connection()




# ___________________________________________________________________

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexao encerrada")


if __name__ == "__main__":
    print("EXECUTANDO NA MAIN")
    banco = Database()
    banco.listar_pessoa()









# if __name__ == "__main__":
#     conexao = Database()
#     conexao.cadastrar_pessoa()
    