#================================================================================================================================
    #Código da janela que será utilizada para salvar, excluir e visualizar os colaboradores
#=================================================================================================================================
#Importando biblioteca tkinter e o método adicional ttk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Importando as principais funcionalidades voltadas para o sistema de gravar, excluir e alterar os colaboradores
from func_bd_colab import *
from func_colab import *

#Importando as funcionalidades voltadas para a gravação, alteração e confirmação da senha
from view_senha import *

class App_Bd_Colab(Func_colab_bd, App_Senha):
    def __init__(self, window_main=None):
        self.window = Toplevel()
        self.window_main = window_main
        self.screen()
        self.screen_frames()
        self.widgets_frame_entry()
        self.table()
        self.build_tables()
        self.select_lista()
    
    #Condigurações da janela
    def screen(self):
        self.window.title("Gerenciamento de Colaboradores")
        self.window.configure(background = "#043F7C")
        self.window.geometry('500x600+100+100')
        self.window.resizable(False, False)
        self.window.transient(self.window_main)
        self.window.focus_force()
        self.window.grab_set()

    #Configurações dos frames da janela
    def screen_frames(self):
        #Configurando frame_entry
        self.frame_entry = Frame(self.window, bg = '#205D9C')
        self.frame_entry.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.46)

        #Configurando frame_table
        self.frame_table = Frame(self.window, bg = '#205D9C')
        self.frame_table.place(relx = 0.02, rely = 0.5, relwidth = 0.96, relheight = 0.46)

    # Função para controle do número de caracteres
    def on_validate(self, P):
        return len(P) <= 20
    
    # widgets do frame_entry (conterá caixas de texto e botões)
    def widgets_frame_entry(self):
        # Configurando label código e a caixa de texto que recebe ou apresenta o código
        self.lb_title_1 = Label(self.frame_entry, text = "Gerenciamento de", bg = '#205D9C', fg = 'white', font = ('verdana', 16, 'bold'))
        self.lb_title_1.place(relx = 0.25, rely = 0.05)

        self.lb_title_2 = Label(self.frame_entry, text = "Colaboradores", bg = '#205D9C', fg = 'white', font = ('verdana', 16, 'bold'))
        self.lb_title_2.place(relx = 0.3, rely = 0.2)

        # Configurando label código e a caixa de texto que recebe ou apresenta o código
        self.lb_codigo = Label(self.frame_entry, text = "Código", bg = '#205D9C', fg = 'white', font = ('verdana', 12, 'bold'))
        self.lb_codigo.place(relx = 0.05, rely = 0.38)

        self.codigo_entry = Entry(self.frame_entry)
        self.codigo_entry.place(relx = 0.05, rely = 0.47, relwidth = 0.15)

        # Criação da label nome e a caixa de texto que recebe ou apresenta o nome
        self.lb_nome = Label(self.frame_entry, text = "Nome", bg = '#205D9C', fg = 'white', font = ('verdana', 12, 'bold'))
        self.lb_nome.place(relx = 0.05, rely = 0.59)

        self.nome_entry = Entry(self.frame_entry)
        self.nome_entry.place(relx = 0.05, rely = 0.68, relwidth = 0.9)

        # Criação da label nome e a caixa de texto que recebe ou apresenta a senha
        self.lb_senha = Label(self.frame_entry, text = "Senha", bg = '#205D9C', fg = 'white', font = ('verdana', 12, 'bold'))
        self.lb_senha.place(relx = 0.05, rely = 0.81)

        # Algoritmo para limitação de caracteres
        validate_cmd = self.frame_entry.register(self.on_validate)

        self.senha_entry = Entry(self.frame_entry, show = "*", validate = "key", validatecommand = (validate_cmd, "%P"))
        self.senha_entry.place(relx = 0.05, rely = 0.90, relwidth = 0.9)

        # Criação dos botões para adição, alteração e remoção dos colaboradores
        pos_y = 0.4                                         #Armazena a posição y dos botões que são posicionados lienarmente
        width_buttons = 0.22                                #Armazena a largura dos botões
        height_buttons = 0.16                               #Armazena a expessura dos botões 

        # Botão para adicionar novos colaboradores
        self.btn_novo = Button(self.frame_entry, text="Novo", bd=2, bg='#6095C9', fg='white', font=('verdana',12,'bold'), command=self.add_c)
        self.btn_novo.place(relx = 0.28, rely = pos_y, relwidth = width_buttons, relheight = height_buttons)

        # Botão que altera colaboradores já cadastrados
        self.btn_alterar = Button(self.frame_entry, text="Alterar", bd=2, bg = '#6095C9', fg='white', font=('verdana',12,'bold'), command=self.alt_c)
        self.btn_alterar.place(relx = 0.505, rely = pos_y, relwidth = width_buttons, relheight = height_buttons)

        # Botão que exclui colaboradores já cadastrados
        self.btn_excluir = Button(self.frame_entry, text="Excluir", bd=2, bg='#6095C9', fg='white', font=('verdana',12,'bold'), command=self.del_c)
        self.btn_excluir.place(relx = 0.73, rely = pos_y, relwidth = width_buttons, relheight = height_buttons)
    
    # Função que configura e desenha a tabela no frame_table
    def table(self):
        self.lista_colab = ttk.Treeview(self.frame_table, height = 3, columns = ('col1', 'col2'))
        self.lista_colab.heading('#0', text = '')
        self.lista_colab.heading('#1', text = 'Codigo')
        self.lista_colab.heading('#2', text = 'Nome')

        self.lista_colab.column('#0', width = 1)
        self.lista_colab.column('#1', width = 50)
        self.lista_colab.column('#2', width = 200)

        self.lista_colab.place(relx = 0.01, rely = 0.1, relwidth = 0.95, relheight = 0.85)

        self.scrool_lista = ttk.Scrollbar(self.frame_table, orient = 'vertical')

        self.lista_colab.configure(yscrollcommand= self.scrool_lista.set)

        self.scrool_lista.place(relx = 0.96, rely = 0.1, relwidth = 0.04, relheight = 0.85)
        self.lista_colab.bind("<Double-1>", self.OnDoubleClick)
    
    # Evento de doubleclick para a tabela
    def OnDoubleClick(self, event):
        self.clear_entry()
        self.lista_colab.selection()

        for n in self.lista_colab.selection():
            col1, col2 = self.lista_colab.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
    
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
        
    # Função que adiciona um novo colaborador se a senha estiver correta
    def add_c(self):
        if self.confirmar_senha(self.window):
            if self.nome_entry.get() != "" and self.senha_entry.get() != "":
                self.add_colab()
                messagebox.showinfo("Aviso", "Colaborador adicionado!")

            else:
                messagebox.showinfo("Erro no Cadastro", "Preencha todos os campos!")
        else:
            messagebox.showinfo("Aviso", "Senha inválida")
    
    #Função que altera um colaborador já cadastrado se a senha estiver correta
    def alt_c(self):
        if self.confirmar_senha(self.window):
            self.altera_colab()
            messagebox.showinfo("Aviso", "Alteração Confirmada!")
        else:
            messagebox.showinfo("Aviso", "Senha inválida")
    
    #Função que deleta um colaborador se a senha estiver correta
    def del_c(self):
        if self.confirmar_senha(self.window):
            self.deleta_colab()
            messagebox.showinfo("Aviso", "Colaborador excluído!")
        else:
            messagebox.showinfo("Aviso", "Senha inválida")