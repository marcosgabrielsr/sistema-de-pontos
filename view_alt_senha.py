# Importando biblioteca tkinter e o método adicional ttk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Importando módulo para trabalhar com a senha armazenada no arquivo JSON
from func_json_senha import *

# Classe para Janela de alteração da senha armazenada no arquivo JSON
class App_Alt_Senha(Json_Senha):
    # Método construtor
    def __init__(self, w_main=None):
        # Inicializando as configurações principais da janela
        self.window_alt = Toplevel()
        self.w_main = w_main
        self.screen_alt()
        self.widgets_window_alt()

    # Configuração da Janela
    def screen_alt(self):
        self.window_alt.title("Alteração de Senha")
        self.window_alt.configure(background = "#043F7C")
        self.window_alt.geometry('450x225')
        self.window_alt.resizable(False, False)
        self.window_alt.transient(self.w_main)
        self.window_alt.focus_force()
        self.window_alt.grab_set()
    
    # Configuração dos widgets da Janela
    def widgets_window_alt(self):
        # Variável para armazenar estado da Checkbutton
        self.ver_senha_var = IntVar()

        # Label para senha atual
        self.text1_lbl = Label(self.window_alt, text="Senha atual:", bg='#043F7C', foreground='white', font=('verdana',14,'bold'))
        self.text1_lbl.place(relx=0.05, rely=0.06)

        # Caixa de entrada de texto para confirmar senha atual
        self.senha_atual = Entry(self.window_alt, show="*", font=('verdana', 12))
        self.senha_atual.place(relx=0.5, rely=0.25, width=360, anchor='center')

        # Label para nova senha
        self.text2_lbl = Label(self.window_alt, text="Nova senha:", bg = '#043F7C', foreground='white', font=('verdana',14,'bold'))
        self.text2_lbl.place(relx = 0.05, rely = 0.36)

        # Caixa de entrada de texto para nova senha
        self.senha_dig = Entry(self.window_alt, show="*", font=('verdana', 12))
        self.senha_dig.place(relx = 0.5, rely = 0.55, width = 360, anchor='center')

        # Checkbutton para exibir/ocultar senha
        self.check_ver_senha = Checkbutton(self.window_alt, text='Mostrar senha', bg='#043F7C', fg='white',
                                       activebackground='#043F7C', activeforeground='white',
                                       variable=self.ver_senha_var, command=self.toggle_senha,
                                       font=('verdana',10,'normal'), selectcolor='#043F7C')
        self.check_ver_senha.place(relx=0.5, rely=0.7, anchor='center')

        # Botão de confirmar
        self.btn_alt = Button(self.window_alt, text="Alterar Senha", bd=2, bg='#6095C9', fg='white', font=('verdana',12,'bold'), command = self.alterar)
        self.btn_alt.place(relx = 0.5, rely = 0.89, anchor='center')

    # Função para alternar exibição da senha
    def toggle_senha(self):
        if self.ver_senha_var.get() == 1:
            self.senha_atual.config(show='')
            self.senha_dig.config(show='')
        else:
            self.senha_atual.config(show='*')
            self.senha_dig.config(show='*')
    
    # Função que lê a senha atual e a altera para uma nova senha
    def alterar(self):
        senha = self.get_senha()

        if senha == self.senha_atual.get():
            self.set_senha(self.senha_dig.get())
            messagebox.showinfo("Aviso", "Alteração confirmada")
        else:
            messagebox.showinfo("Aviso", "Senha inválida")
        
        self.window_alt.destroy()