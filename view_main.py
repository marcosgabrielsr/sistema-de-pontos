#=================================================================================================================================
    #Código da janela principal
#=================================================================================================================================

#Importando funções da janela principal
from func_main import *

#Importando funções e métodos da janela de colaboradores
from view_colab import *
from func_bd_colab import *

#Importando funções e métodos da janela de pontos
from view_pontos import *
from func_bd_pontos import *

#Importando as funcionalidades voltadas para a gravação, alteração e confirmação da senha
from view_senha import *
from view_alt_senha import *

#Importando módulo para trabalhar com pastas
from func_pasta import *

#Importando módulo para gerar as planilhas
from view_planilha import *

from tkinter import PhotoImage

import base64

#Criando objeto para janela
window = Tk()

#Criando classe para a janela principal
class Application(Func, App_Bd_Colab, App_Bd_Pontos, App_Senha, App_Alt_Senha, Folders):
    #Método executado quando o sistema é iniciado
    def __init__(self):
        self.window = window

        #Inicializando os banco de dados
        self.build_pontos_table()
        self.build_tables()

        #Armazenando os colaboradores
        self.colaboradores = self.get_colabs()

        #Setando a base64 do ícone de usuário
        self.iu = "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"

        self.t = ("Inicio de Turno", "Saida para Almoço", "Retorno do Almoço", "Fim de turno")
        self.screen()
        self.screen_frames()
        self.widgets_frame_cb_box()
        self.widgets_frame_btn()
        self.menu()

        self.create_planilhas()

        window.mainloop()
    
    #Configurações da Janela
    def screen(self):
        self.window.title("Sistema de Pontos")
        self.window.configure(background = "#043F7C")
        self.window.geometry('650x500+650+300')
    
    #Configuração da barra de menu
    def menu(self):
        menubar = Menu(self.window)
        self.window.config(menu = menubar)
        iten_menu = Menu(menubar, tearoff = 0)
        iten_menu2 = Menu(menubar, tearoff = 0)

        menubar.add_cascade(label = "Opções", menu = iten_menu)
        menubar.add_cascade(label = "Sobre", menu = iten_menu2)

        iten_menu.add_command(label = "Gerenciar Colaboradores", command = self.window_colab_manager)
        iten_menu.add_command(label = "Gerenciar Dados", command = self.window_pontos_manager)
        iten_menu.add_command(label = "Gerar Planilha", command = self.create_p)
        iten_menu.add_command(label = "Alterar Senha", command = self.alt_senha)

    #Configurações dos frames da janela
    def screen_frames(self):
        self.frame_cb_box = Frame(self.window, bg = '#205D9C')
        self.frame_cb_box.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.76)

        self.frame_btn = Frame(self.window, bg = '#205D9C')
        self.frame_btn.place(relx = 0.02, rely = 0.80, relwidth = 0.96, relheight = 0.18)

    #widgets do frame_cb_box (conterá labels e combo box)
    def widgets_frame_cb_box(self):
        #label de titulo
        self.title_system = Label(self.frame_cb_box, text = "Sistema de Pontos", bg = '#205D9C', foreground = 'white', font = ('verdana', 20, 'bold'))
        self.title_system.place(relx = 0.5, rely = 0.05, anchor='center')

        # Configurando imagem do ícone de usuário
        self.user_icon = PhotoImage(data = base64.b64decode(self.iu))

        self.lbl_user_icon = Label(image=self.user_icon, bg='#205D9C')
        self.lbl_user_icon.place(relx=0.5, rely=0.30, anchor='center')

        # Label colaborador
        self.colab = Label(self.frame_cb_box, text = "Colaborador:", bg = '#205D9C', fg = 'white', font = ('verdana', 14, 'bold'))
        self.colab.place(relx = 0.05, rely = 0.50)

        # Label turno
        self.turnos = Label(self.frame_cb_box, text = "Momento:", bg = '#205D9C', fg = 'white', font = ('verdana', 14, 'bold'))
        self.turnos.place(relx = 0.05, rely = 0.67)

        # Label senha
        self.lb_senha_main = Label(self.frame_cb_box, text="Senha:", bg='#205D9C', fg='white', font=('verdana', 14, 'bold'))
        self.lb_senha_main.place(relx = 0.05, rely = 0.87)

        # Combo box dos colaboradores
        self.cb_colab = ttk.Combobox(self.frame_cb_box, values=self.colaboradores, font=('verdana', 14), state="readonly")
        self.cb_colab.place(relx = 0.35, rely = 0.50, relwidth = 0.60)

        # Combo box dos turnos
        self.cb_turnos = ttk.Combobox(self.frame_cb_box, values = self.t, font = ('verdana', 14), state = "readonly")
        self.cb_turnos.place(relx = 0.35, rely = 0.67, relwidth = 0.60)

        # Algoritmo para limitação de caracteres
        validate_cmd = self.frame_cb_box.register(self.on_validate)

        self.main_entry_senha = Entry(self.frame_cb_box, show="*", validate="key", validatecommand=(validate_cmd, "%P"), font=('verdana', 14))
        self.main_entry_senha.place(relx=0.35, rely=0.87, relwidth=0.6)
    
    # Widgets do frame que conterá os botões gravar e limpar
    def widgets_frame_btn(self):
        # Botão que chamará a função para gravar os dados no banco de dados
        self.btn_gravar = Button(self.frame_btn, text="Gravar", bd=2, bg='#6095C9', fg='white', font=('verdana',14,'bold'), command=self.add_p)
        self.btn_gravar.place(relx=0.15, rely=0.32, relwidth=0.2, relheight=0.4)

        # Botão que limpa os campos de texto
        self.btn_limpar = Button(self.frame_btn, text="Limpar", bd=2, bg='#6095C9', fg='white', font=('verdana',14,'bold'), command=self.clear_cb)
        self.btn_limpar.place(relx=0.65, rely=0.32, relwidth=0.2, relheight=0.4)

    # Função que chama a janela que apresenta os colaboradores
    def window_colab_manager(self):
        App_Bd_Colab(window_main=window)

    # Função que chama a janela que apresenta os pontos salvos no banco de dados
    def window_pontos_manager(self):
        App_Bd_Pontos(window_main_pontos=window, colaboradores=self.colaboradores)
    
    # Função que grava os pontos com os dados da main
    def add_p(self):
        # Verifica se o turno que tentamos gravar já está ou não gravado na data atual
        if self.verifica_ponto():
            # Verifica se os turnos anteriores foram gravados corretamente
            if self.verifica_turnos_anteriores():
                # Armazena a senha no arquivo json na variável senha
                senha = self.get_senha_colab()

                if len(senha) > 0:
                    if senha == self.main_entry_senha.get():
                        print("Senha colaborador correta!")
                        self.add_pontos(True)
                        messagebox.showinfo("Aviso", "Ponto adicionado!")
                        self.clear_cb()
                    else:
                        messagebox.showinfo("Erro na Gravação de Pontos", "Senha inválida") 
                else:
                    messagebox.showinfo("Erro na Gravação de Pontos", "Colaborador não encontrado")
            else:
                messagebox.showinfo("Erro na Gravação de Pontos", "Verifique o turno")
        else:
            messagebox.showinfo("Erro na Gravação de Pontos", "Ponto já gravado")

    # Função que chama a janela de alteração de janela
    def alt_senha(self):
        if self.get_senha() == None:    # Caso uma senha não tenha sido criada...
            App_Senha(self.window)
        else:                           # Caso uma senha já exista...
            App_Alt_Senha(self.window)
    
    # Função que chama a janela de geração de planilhas caso a senha esteja correta
    def create_p(self):
        if self.confirmar_senha(self.window):
            print("\nAbrindo janela para geração de planilhas\n")
            View_Planilha(w_fp_main=self.window)
        else:
            messagebox.showinfo("Aviso", "Senha inválida")

Application()