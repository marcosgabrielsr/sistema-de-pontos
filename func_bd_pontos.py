# Impotando as principais funcionalidades e variáveis da tela principal
from func_main import *
from func_pontos import *

# Importando a biblioteca referente ao banco de dados
import sqlite3

# Importando a biblioteca responsável por pegar a data e hora do PC
from datetime import datetime

class Func_bd_pontos():
    # Função que conecta ao banco de dados
    def conecta_pontos_bd(self):
        self.conn = sqlite3.connect("pontos.bd")
        self.cursor = self.conn.cursor()
        print("Conectando ao banco de dados dos pontos")

    # Função que encerra a conexão com o banco de dados
    def desconecta_pontos_bd(self):
        self.conn.close()
        print("Desconectando do banco de dados dos pontos")
    
    # Função que constrói a tabela
    def build_pontos_table(self):
        self.conecta_pontos_bd()

        # Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pontos(
                cod INTEGER PRIMARY KEY,
                nome_pontos CHAR(40) NOT NULL,
                horario CHAR(8) NOT NULL,
                data CHAR(10) NOT NULL,
                tipo INTEGER NOT NULL
            );
        """)

        self.conn.commit(); print("Banco de Dados Criado")
        self.desconecta_pontos_bd()

    # Função que armazena os dados de entrada em variáveis
    def var_pontos(self, isMain):
        current_dt = datetime.now()
        turnos1 = ("Inicio de Turno", "Saida para Almoço", "Retorno do Almoço", "Fim de turno")
        turnos2 = ('inicio', 'saida almoço', 'volta almoço', 'fim')

        if isMain:
            self.nome_pontos = self.cb_colab.get()
            self.tipo = turnos1.index(self.cb_turnos.get())
            self.time = current_dt.strftime('%H%M')
            self.data = current_dt.strftime('%d/%m/%Y')
        else:
            self.nome_pontos = self.cb_nome.get()
            self.tipo = turnos2.index(self.cb_momento.get())
            self.time = self.horario_entry.get()
            self.data = self.data_entry.get()

    # Função que atualiza a tabela com os dados do banco de dados dos pontos
    def select_lista_p(self):
        self.lista_pontos.delete(*self.lista_pontos.get_children())
        self.conecta_pontos_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_pontos, horario, data, tipo FROM pontos ORDER BY nome_pontos ASC;""")

        for i in lista:
            self.lista_pontos.insert("", END, values = i)
        
        self.desconecta_pontos_bd()

    # Função que adiciona dados ao banco de dados (pontos.bd)
    def add_pontos(self, isMain):
        # Tenta conectar ao banco de dados e armazenar os dados
        try:
            # Função que pega os dados dos campos de entrada
            self.var_pontos(isMain)
            self.conecta_pontos_bd()

            self.cursor.execute(""" INSERT INTO pontos (nome_pontos, horario, data, tipo) VALUES ('%s', '%s', '%s', '%d');""" % (self.nome_pontos, self.time, self.data, self.tipo))
            self.conn.commit()

            self.desconecta_pontos_bd()
            
            # Caso esta função seja chamada na main, a tabela de dados não é atualizada
            if not(isMain):
                self.select_lista_p()

        except Exception as e:
            print(f"Erro ao adicionar pontos: {e}")
            # Se ocorrer um erro, chama a função que cria a tabela e tenta novamente
            self.build_pontos_table()
            self.add_pontos()

    # Função que deleta dados da tabela
    def del_pontos(self):
        # Tenta deletar um dos dados da Tabela
        try:
            cod = self.codigo_entry.get()
            self.conecta_pontos_bd()

            self.cursor.execute(""" DELETE FROM pontos WHERE cod = '%s'""" % cod)
            self.conn.commit()

            self.desconecta_pontos_bd()
            self.clear_entry_pontos()
            self.select_lista_p()

        except Exception as e:
            print(f"Erro ao adicionar pontos: {e}")
            # Se ocorrer um erro, chama a função de criar tabelas
            self.build_pontos_table()

    # Função que altera dados da tabela
    def alt_pontos(self):
        #Tenta deletar um dos dados da Tabela
        try:
            cod = self.codigo_entry.get()
            self.var_pontos(False)
            self.conecta_pontos_bd()

            self.cursor.execute(""" UPDATE pontos SET nome_pontos = ?, horario = ?, data = ?, tipo = ? WHERE cod = ? """, (self.nome_pontos, self.time, self.data, self.tipo, cod))
            self.conn.commit()

            self.desconecta_pontos_bd()
            self.clear_entry_pontos()
            self.select_lista_p()

        except Exception as e:
            print(f"Erro ao adicionar pontos: {e}")
            # Se ocorrer um erro, chama a função de criar tabelas
            self.build_pontos_table()

    # Função que busca os pontos referentes aos campos preenchidos dos checkbuttons
    def busca_pontos(self):
        self.conecta_pontos_bd()
        self.lista_pontos.delete(*self.lista_pontos.get_children())

        # Buscando segundo a data e o nome
        if self.var1.get() and self.var2.get():
            self.data_entry.insert(END, '%')        # Adiciona o caracter '%' para permitir buscas parciais

            nome = self.cb_nome.get()
            data = self.data_entry.get()

            self.cursor.execute(
                """
                    SELECT cod, nome_pontos, horario, data, tipo 
                    FROM pontos 
                    WHERE nome_pontos LIKE '%s' AND data LIKE '%s'
                    ORDER BY nome_pontos ASC;
                """ % (nome, data)
            )

        # Buscando apenas pelo nome
        elif self.var1.get():
            nome = self.cb_nome.get()

            self.cursor.execute(
                """
                    SELECT cod, nome_pontos, horario, data, tipo 
                    FROM pontos 
                    WHERE nome_pontos LIKE '%s' 
                    ORDER BY nome_pontos ASC;
                """ % (nome)
            )
        
        # Buscando apenas pela data
        elif self.var2.get():
            self.data_entry.insert(END, '%')

            data = self.data_entry.get()

            self.cursor.execute(
                """
                    SELECT cod, nome_pontos, horario, data, tipo 
                    FROM pontos 
                    WHERE data LIKE '%s'
                    ORDER BY nome_pontos ASC;
                """ % (data)
            )
        else:
            messagebox.showinfo("Aviso", "Nenhum filtro selecionado")

        busca = self.cursor.fetchall()

        for i in busca:
            self.lista_pontos.insert("", END, values=i)
        
        self.clear_entry_pontos()
        self.desconecta_pontos_bd()
    
    # Função que verifica se o ponto já foi cadastrado para aquele dia
    def verifica_ponto(self):
        # Pegamos a data e o horário atual e definimos os turnos
        current_dt = datetime.now()
        turnos1 = ("Inicio de Turno", "Saida para Almoço", "Retorno do Almoço", "Fim de turno")

        # Pegamos o nome, turno e a data atual
        nome_pontos = self.cb_colab.get()
        tipo = turnos1.index(self.cb_turnos.get())
        data = current_dt.strftime('%d/%m/%Y')

        # Conectamos ao banco de dados
        self.conecta_pontos_bd()
        
        # Executamos uma busca para verificar se há um dado onde os campos
        # nome_pontos, tipo e data são iguais aos que serão cadastrados
        self.cursor.execute(
                """
                    SELECT cod, nome_pontos, horario, data, tipo 
                    FROM pontos 
                    WHERE nome_pontos LIKE '%s' AND data LIKE '%s' AND tipo LIKE '%s'
                    ORDER BY nome_pontos ASC;
                """ % (nome_pontos, data, tipo)
            )

        # Armazenamos a informação retornada da busca
        busca = self.cursor.fetchall()
        self.desconecta_pontos_bd()

        # Se a lista da busca estiver vazia, retornamos true
        if not busca:
            return True
        # Se a lista não estiver vazia
        else:
            return False
    
    # Função que verifica se os turnos anteriores foram salvos antes de salvar o atual
    def verifica_turnos_anteriores(self):
        # Pegamos a data e o horário atual e definimos os turnos
        current_dt = datetime.now()
        turnos1 = ("Inicio de Turno", "Saida para Almoço", "Retorno do Almoço", "Fim de turno")

        # Pegamos o nome, tipo de turno e a data atual
        nome_pontos = self.cb_colab.get()
        tipo = turnos1.index(self.cb_turnos.get())
        data = current_dt.strftime('%d/%m/%Y')

        # Criamos um for, que percorre todos os turnos anteriores até o atual que queremos gravar
        for i in range(0, tipo):
            # Conectamos ao banco de dados
            self.conecta_pontos_bd()
            
            # Executamos uma busca para verificar se há um dado onde os campos
            # nome_pontos, tipo e data são iguais aos que serão cadastrados
            self.cursor.execute(
                    """
                        SELECT cod, nome_pontos, horario, data, tipo 
                        FROM pontos 
                        WHERE nome_pontos LIKE '%s' AND data LIKE '%s' AND tipo LIKE '%s'
                        ORDER BY nome_pontos ASC;
                    """ % (nome_pontos, data, i)
                )

            # Armazenamos a informação retornada da busca
            busca = self.cursor.fetchall()
            self.desconecta_pontos_bd()

            # Se a lista busca estiver vazia, retornamos true
            if not busca:
                return False
        # Se ao sair do for, tudo estiver correto return True
        return True
    
    # Função que limpa os dados de uma tabela do banco de dados
    def clear_table(self):
        self.conecta_pontos_bd()

        self.cursor.execute("""DELETE FROM pontos""")
        self.conn.commit()

        self.desconecta_pontos_bd()
    
    # Função que apaga os dados dos meses anteriores
    def remover_dados_antigos(self):
        mes_atual = datetime.now().strftime("%m")
        ano_atual = datetime.now().strftime("%Y")

        self.conecta_pontos_bd()

        # Excluir registros com mês e ano diferentes do atual
        self.cursor.execute("""
            DELETE FROM pontos
            WHERE strftime('%m', substr(data, 7, 4) || '-' || substr(data, 4, 2) || '-' || substr(data, 1, 2)) != ?
            OR strftime('%Y', substr(data, 7, 4) || '-' || substr(data, 4, 2) || '-' || substr(data, 1, 2)) != ?
        """, (mes_atual, ano_atual))

        self.conn.commit()
        self.desconecta_pontos_bd()