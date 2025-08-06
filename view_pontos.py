# Importando biblioteca tkinter, método adicional ttk e o pacote de caixas de mensagem
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Importando pacote para acessar informações dos colaboradores
from func_bd_colab import *

# Importando as principais funcionalidades voltadas para o sistema de gravar, excluir e alterar os pontos
from func_bd_pontos import *
from func_pontos import *

# Importando as funcionalidades voltadas para a gravação, alteração e confirmação da senha
from view_senha import *

# Importando pacote para adicionar sistema de identifição de faltas com atestados
from view_add_atestado import App_Add_Atestado

# Importando pacote para remover faltas dos funcionários
from view_rem_faltas_func import App_Rem_Falta_Func

class App_Bd_Pontos(Func_bd_pontos, Func_view_pontos, App_Senha):
    def __init__(self, window_main_pontos=None, colaboradores=None):
        self.window_pontos = Toplevel()
        self.window_main_pontos = window_main_pontos
        self.colaboradores = colaboradores
        self.screen_pontos()
        self.screen_frames_pontos()
        self.menu_pontos()
        self.frame_entry_pontos_widgets()
        self.frame_checkButtons_widgets()
        self.frame_table_builder()
        self.build_pontos_table()
        self.select_lista_p()
    
    # Configurações da Janela
    def screen_pontos(self):
        self.window_pontos.title("Gerenciar Pontos")
        self.window_pontos.configure(background = "#043F7C")
        self.window_pontos.geometry('600x520+100+100')
        self.window_pontos.resizable(False, False)
        self.window_pontos.transient(self.window_main_pontos)
        self.window_pontos.focus_force()
        self.window_pontos.grab_set()
    
    # Configuração da barra de menu
    def menu_pontos(self):
        menubar_pontos = Menu(self.window_pontos)
        self.window_pontos.config(menu = menubar_pontos)
        iten_menu_op_avan = Menu(menubar_pontos, tearoff=0)
        iten_menu_rem = Menu(menubar_pontos, tearoff=0)

        menubar_pontos.add_cascade(label="Opções Avançadas", menu=iten_menu_op_avan)
        iten_menu_op_avan.add_cascade(label="Opções de Remoção", menu=iten_menu_rem)

        iten_menu_op_avan.add_command(label="Adicionar atestado", command=self.adicionar_atestado)
        iten_menu_rem.add_command(label="Remover dados antigos", command=self.rem_dados_antigos)
        iten_menu_rem.add_command(label="Remover faltas", command=self.rem_faltas_func)

    # Configurações dos frames da janela
    def screen_frames_pontos(self):
        # Configurando frame_actions
        self.frame_entry_pontos = Frame(self.window_pontos, bg = '#205D9C')
        self.frame_entry_pontos.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.46)

        # Configurando frame_table
        self.frame_table_pontos = Frame(self.window_pontos, bg = '#205D9C')
        self.frame_table_pontos.place(relx = 0.02, rely = 0.5, relwidth = 0.96, relheight = 0.46)

        # Configurando frame onde será posicionado os checkbuttons
        self.frame_checkButtons = Frame(self.frame_entry_pontos, bg = "#043F7C")
        self.frame_checkButtons.place(relx = 0.77, rely = 0.56, relheight = 0.40, relwidth = 0.22)

    # Configuração dos widgets do frame_entry_pontos
    def frame_entry_pontos_widgets(self):
        # Variável de controle da data
        data_var = StringVar()

        def formatar_data(*args):
            # Pega a posição atual do cursor
            pos_cursor = self.data_entry.index(INSERT)

            # Valor atual da Entry
            valor_original = data_var.get()

            # Remove tudo que não é número
            apenas_digitos = ''.join(filter(str.isdigit, valor_original))

            # Limita a 8 caracteres
            if len(apenas_digitos) > 8:
                apenas_digitos = apenas_digitos[:8]

            # Novo valor formatado com barras
            novo_valor = apenas_digitos
            if len(apenas_digitos) > 4:
                novo_valor = f"{apenas_digitos[:2]}/{apenas_digitos[2:4]}/{apenas_digitos[4:]}"
            elif len(apenas_digitos) > 2:
                novo_valor = f"{apenas_digitos[:2]}/{apenas_digitos[2:]}"
            
            # Só atualiza se realmente mudou
            if valor_original != novo_valor:
                # Define novo valor
                data_var.set(novo_valor)

                # Calcula nova posição do cursor
                def ajustar_cursor():
                    nova_pos = pos_cursor

                    # Conta quantas barras existiam antes da posição original
                    barras_antes = valor_original[:pos_cursor].count('/')
                    nova_barras_antes = novo_valor[:pos_cursor].count('/')

                    # Calcula diferença causada pelas barras novas ou removidas
                    diff = nova_barras_antes - barras_antes
                    nova_pos += diff

                    # Garante que o cursor não ultrapasse o tamanho do texto
                    nova_pos = max(0, min(len(novo_valor), nova_pos))

                    self.data_entry.icursor(nova_pos)

                # Aguarda a interface atualizar o texto antes de mover o cursor
                self.data_entry.after_idle(ajustar_cursor)

        # Ativa o monitoramento da variável
        data_var.trace_add("write", formatar_data)

        # Tamanho da fonte do texto das caixas de entrada
        font_size_entry = 8

        # Título do frame
        self.lb_title = Label(self.frame_entry_pontos, text="Gerenciamento de Pontos", bg='#205D9C', fg='white', font=('verdana',16,'bold'))
        self.lb_title.place(relx=0.5, rely=0.13, anchor='center')

        # label e caixa de entrada de texto para o código
        self.lb_codigo = Label(self.frame_entry_pontos, text="Código", bg='#205D9C', fg='white', font=('verdana',10))
        self.lb_codigo.place(relx=0.05, rely=0.24)

        self.codigo_entry = Entry(self.frame_entry_pontos, font=('verdana',font_size_entry))
        self.codigo_entry.place(relx=0.05, rely=0.33, relwidth=0.105)

        # label e caixa de entrada de texto para o nome
        self.lb_nome = Label(self.frame_entry_pontos, text="Nome", bg='#205D9C', fg='white', font=('verdana',10))
        self.lb_nome.place(relx=0.05, rely=0.47)

        self.cb_nome = ttk.Combobox(self.frame_entry_pontos, values=self.colaboradores, font=('verdana',font_size_entry), state='readonly')
        self.cb_nome.place(relx=0.05, rely=0.56, relwidth=0.7)

        # label e caixa de entrada de texto para o horário
        self.lb_horario = Label(self.frame_entry_pontos, text="Horário", bg='#205D9C', fg='white', font=('verdana',10))
        self.lb_horario.place(relx=0.05, rely=0.70)

        self.horario_entry = Entry(self.frame_entry_pontos, font = ('verdana', font_size_entry))
        self.horario_entry.place(relx = 0.05, rely = 0.79, relwidth = 0.15)

        # label e caixa de entrada de texto para a data
        self.lb_data = Label(self.frame_entry_pontos, text = "Data", bg = '#205D9C', fg = 'white', font = ('verdana', 10))
        self.lb_data.place(relx=0.28, rely=0.70)

        self.data_entry = Entry(self.frame_entry_pontos, textvariable=data_var, font=('verdana',font_size_entry))
        self.data_entry.place(relx=0.28, rely=0.79, relwidth=0.15)

        # label e combo box para os momentos
        self.lb_momento = Label(self.frame_entry_pontos, text = "Momento", bg = '#205D9C', fg = 'white', font = ('verdana', 10))
        self.lb_momento.place(relx=0.51, rely=0.70)
        
        self.lista_momentos = ('inicio', 'saida almoço', 'volta almoço', 'fim')
        self.cb_momento = ttk.Combobox(self.frame_entry_pontos, values = self.lista_momentos, font = ('verdana', font_size_entry), state = "readonly")
        self.cb_momento.place(relx=0.51, rely=0.79, relwidth=0.24)

        # Medidas e coordenadas para os botões
        buttons_y = 0.315
        buttons_h = 0.12
        buttons_w = 0.15

        # Botão para adicionar
        self.btn_novo = Button(self.frame_entry_pontos, text="Novo", bd=2, bg='#6095C9', fg='white', font=('verdana',14,'bold'), command=self.add_p_vp)
        self.btn_novo.place(relx=0.2, rely=buttons_y, relwidth=buttons_w, relheight=buttons_h)

        # Botão para alterar
        self.btn_alt = Button(self.frame_entry_pontos, text="Alterar", bd=2, bg='#6095C9', fg='white', font=('verdana',14,'bold'), command=self.alt_p)
        self.btn_alt.place(relx = 0.4, rely = buttons_y, relwidth = buttons_w, relheight = buttons_h)

        # Botão para excluir
        self.btn_del = Button(self.frame_entry_pontos, text="Excluir", bd=2, bg='#6095C9', fg='white', font=('verdana',14,'bold'), command=self.del_p)
        self.btn_del.place(relx=0.6, rely=buttons_y, relwidth = buttons_w, relheight=buttons_h)

        # Botão para pesquisar
        self.btn_search = Button(self.frame_entry_pontos, text="Buscar", bd=2, bg='#6095C9', fg='white', font=('verdana',14,'bold'), command=self.busca_pontos)
        self.btn_search.place(relx=0.8, rely=buttons_y, relwidth=buttons_w, relheight=buttons_h)

    # Frame para organização dos CheckButtons
    def frame_checkButtons_widgets(self):
        # Variáveis para os CheckButtons
        self.var1 = BooleanVar()
        self.var2 = BooleanVar()
        self.var1.set(True)
        self.var2.set(False)

        # Checkbutton para o nome
        nome_check_btn = ttk.Checkbutton(self.frame_checkButtons, text="Nome", takefocus=0, variable=self.var1)
        nome_check_btn.place(relx=0.1, rely=0.1)

        # Checkbutton para data
        data_check_btn = ttk.Checkbutton(self.frame_checkButtons, text="Data", takefocus=0, variable=self.var2)
        data_check_btn.place(relx=0.1, rely = 0.4)  

        # Estilizando os CheckButtons
        style = ttk.Style()
        style.configure('TCheckbutton', background="#043F7C", foreground="white")
    
    def frame_table_builder(self):
        self.lista_pontos = ttk.Treeview(self.frame_table_pontos, height=3, columns=('col1','col2','col3','col4','col5'))
        self.lista_pontos.heading('#0', text='')
        self.lista_pontos.heading('#1', text='Codigo')
        self.lista_pontos.heading('#2', text='Nome')
        self.lista_pontos.heading('#3', text='Horario')
        self.lista_pontos.heading('#4', text='Data')
        self.lista_pontos.heading('#5', text='Momento')

        self.lista_pontos.column('#0', width=1)
        self.lista_pontos.column('#1', width=30)
        self.lista_pontos.column('#2', width=200)
        self.lista_pontos.column('#3', width=40)
        self.lista_pontos.column('#4', width=60)
        self.lista_pontos.column('#5', width=30)

        self.lista_pontos.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.85)
        self.scrool_lista = ttk.Scrollbar(self.frame_table_pontos, orient='vertical')
        self.lista_pontos.configure(yscrollcommand= self.scrool_lista.set)
        self.scrool_lista.place(relx=0.96, rely=0.05, relwidth=0.028, relheight=0.85)
        self.scrool_lista.config(command=self.lista_pontos.yview)
        self.lista_pontos.bind("<Double-1>", self.OnDoubleClick)
    
    # Evento de doubleclick para a tabela
    def OnDoubleClick(self, event):
        self.clear_entry_pontos()
        self.lista_pontos.selection()

        for n in self.lista_pontos.selection():
            col1, col2, col3, col4, col5 = self.lista_pontos.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.cb_nome.set(col2)
            self.data_entry.insert(END, col4)
            self.horario_entry.insert(END, col3)
            self.cb_momento.set(self.lista_momentos[int(col5)])

    # Função que abre a tela para confirmação de senha
    def confirmar_senha(self, w_master=None):
        r_senha = self.get_senha()

        if r_senha == None:
            App_Senha(w_master)
            return False
        else:
            # Chama App_Senha para verificar se a senha digitada é a correta
            App_Senha(w_master)
            with open("senha.json") as file:
                data = json.load(file)
            
            # Verifica se a Senha está correta
            if data['confirn']:
                # Se sim, nega a confirmação
                data['confirn'] = False

                # Abre o arquivo com modo de escrita e cria um novo objeto à partir de um dicionário
                with open("senha.json", 'w') as file:
                    json.dump(data, file, indent = 2)
                return True
            else:
                return False

    # Função que adiciona itens ao banco de dados de pontos usando os dados da view pontos
    def add_p_vp(self):
        if self.confirmar_senha(self.window_pontos):
            self.add_pontos(False)
            self.clear_entry_pontos()
            messagebox.showinfo("Aviso", "Pontos adicionados")
        else:
            messagebox.showinfo("Aviso", "Senha inválida")
    
    # Função que remove itens do se a senha digitada for a correta
    def del_p(self):
        if self.confirmar_senha(self.window_pontos):
            self.del_pontos()
            messagebox.showinfo("Aviso", "Pontos excluídos")
        else:
            messagebox.showinfo("Aviso", "Senha inválida")
    
    # Função que altera um dado específico da tabela
    def alt_p(self):
        if self.confirmar_senha(self.window_pontos):
            self.alt_pontos()
            messagebox.showinfo("Aviso", "Alteração realizada")
        else:
            messagebox.showinfo("Aviso", "Senha inválida")

    # Função que remove dados antigos quando a senha é digitada corretamente
    def rem_dados_antigos(self):
        if self.confirmar_senha(self.window_pontos):
            self.remover_dados_antigos()
            messagebox.showinfo("Aviso", "Dados Removidos")
        else:
            messagebox.showinfo("Aviso", "Senha inválida")

    # Função que gera uma janela para adicionar um atestado à um funcionário
    def adicionar_atestado(self):
        App_Add_Atestado(w_main=self.window_pontos, colaboradores=self.colaboradores)

    # Função que chama uma janela para remover as faltas de um funcionário
    def rem_faltas_func(self):
        App_Rem_Falta_Func(w_main=self.window_pontos, colaboradores=self.colaboradores)