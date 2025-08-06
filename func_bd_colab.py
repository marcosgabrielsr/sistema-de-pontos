from func_colab import *
import sqlite3

class Func_colab_bd(Func_view_colab):
    #Função que conecta ao banco de dados
    def conecta_colab_bd(self):
        self.conn = sqlite3.connect("colab.bd")
        self.cursor = self.conn.cursor()
    
    #Função que encerra a conexão com o banco de dados
    def desconecta_colab_bd(self):
        self.conn.close()
        print("Deconectando do banco de dados")
    
    #Função que constrói a tabela
    def build_tables(self):
        self.conecta_colab_bd()

        #Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS colab (
                cod INTEGER PRIMARY KEY,
                nome_colab CHAR(40) NOT NULL,
                senha CHAR(40) NOT NULL
            );
        """)

        self.conn.commit(); print("Banco de Dados Criado")
        self.desconecta_colab_bd()
    
    #Função que cria variáveis para receber os dados dos campos de entrada
    def variables(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.senha = self.senha_entry.get()
    
    #Função que atualiza a tabela com os dados do banco de dados
    def select_lista(self):
        self.lista_colab.delete(*self.lista_colab.get_children())
        self.conecta_colab_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_colab FROM colab ORDER BY nome_colab ASC;""")

        for i in lista:
            self.lista_colab.insert("", END, values = i)
        
        self.desconecta_colab_bd()

    #Função para adicionar novos colaboradores
    def add_colab(self):
        self.variables()
        self.conecta_colab_bd()

        self.cursor.execute(""" INSERT INTO colab (nome_colab, senha) VALUES ('%s', '%s')""" % (self.nome, self.senha))

        self.conn.commit()

        self.desconecta_colab_bd()
        self.select_lista()
        self.clear_entry()
    
    #Função que deleta um determinado colaborador já cadastrado
    def deleta_colab(self):
        self.variables()
        self.conecta_colab_bd()

        self.cursor.execute(""" DELETE FROM colab WHERE cod = '%s'""" % self.codigo)
        self.conn.commit()

        self.desconecta_colab_bd()
        self.clear_entry()
        self.select_lista()

    #Função que altera os dados um determinado colaborador já cadastrado
    def altera_colab(self):
        self.variables()
        self.conecta_colab_bd()

        self.cursor.execute(""" UPDATE colab SET nome_colab = ?, senha = ?  WHERE cod = ?""", (self.nome, self.senha, self.codigo))
        self.conn.commit()

        self.desconecta_colab_bd()
        self.select_lista()
        self.clear_entry()
    
    # Função que retorna os colaboradores
    def get_colabs(self):
        self.conecta_colab_bd()

        # Executa a consulta SQL
        self.cursor.execute("""SELECT nome_colab FROM colab ORDER BY nome_colab ASC;""")

        colaboradores = [registro[0] for registro in self.cursor.fetchall()]

        self.desconecta_colab_bd()

        return colaboradores

    # Função que retorna o código do colaborador passado por parâmetro
    def get_cod(self, nome):
        self.conecta_colab_bd()

        #Executa uma consulta SQL
        self.cursor.execute("""SELECT cod FROM colab WHERE nome_colab LIKE '%s'""" % nome)

        cod = self.cursor.fetchall()

        self.desconecta_colab_bd()

        return cod
    
    # Função que retorna a senha do usuário que quer gravar os pontos
    def get_senha_colab(self):
        self.nome = self.cb_colab.get()
        self.conecta_colab_bd()

        self.cursor.execute("""SELECT senha FROM colab
                            WHERE nome_colab LIKE '%s'""" % self.nome)
        
        senha = self.cursor.fetchall()

        self.desconecta_colab_bd()

        if len(senha) > 0:
            return senha[0][0]
        
        return senha