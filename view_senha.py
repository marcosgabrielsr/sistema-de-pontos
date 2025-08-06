# Importando biblioteca tkinter e o método adicional ttk
from tkinter import *
from tkinter import ttk

# Importando módulo para trabalhar com a senha armazenada no arquivo JSON
from func_json_senha import *

# Classe para Janela de cadastro e verificação de senha
class App_Senha(Json_Senha):
    # Método executado quando o sistema é iniciado
    def __init__(self, w_main=None):
        # Inicializando as configurações principais da Janela
        self.window_entry = Toplevel()
        self.w_main = w_main

        self.r_senha = self.get_senha()

        # Definindo algumas strings para a janela
        if self.r_senha == None:
            self.title = "Cadastrar Senha"
            self.text = "Insira a nova senha: "
            self.text_btn = "Cadastrar"
        else:
            self.title = "Confirmar Senha"
            self.text = "Insira a senha para confirmar a ação: "
            self.text_btn = "Confirmar"
        
        self.screen_entry()
        self.widgets_window_entry()
        self.window_entry.wait_window()

    # Configuração da Janela
    def screen_entry(self):
        self.window_entry.title(self.title)
        self.window_entry.configure(background = "#043F7C")
        self.window_entry.geometry('450x225')
        self.window_entry.resizable(False, False)
        self.window_entry.transient(self.w_main)
        self.window_entry.focus_force()
        self.window_entry.grab_set()
    
    # Configuração dos widgets da Janela
    def widgets_window_entry(self):
        # Variável para armazenar estado da Checkbutton
        self.ver_senha_var = IntVar()

        # Configurando a Label para Texto de informação
        self.text_lbl = Label(self.window_entry, text=self.text, bg='#043F7C', foreground='white', font=('verdana',14,'bold'))
        self.text_lbl.place(relx=0.5, rely=0.1, anchor='center')

        # Configurando a caixa de entrada de texto
        self.senha_txt_entry = Entry(self.window_entry, show="*", font=('verdana',12))
        self.senha_txt_entry.place(relx=0.5, rely=0.35, width=360, anchor='center')

        # Checkbutton para exibir/ocultar senha
        self.check_ver_senha = Checkbutton(self.window_entry, text='Mostrar senha', bg='#043F7C', fg='white',
                                       activebackground='#043F7C', activeforeground='white',
                                       variable=self.ver_senha_var, command=self.toggle_senha,
                                       font=('verdana',10,'normal'), selectcolor='#043F7C')
        self.check_ver_senha.place(relx=0.5, rely=0.52, anchor='center')

        # Configurando botão para confirmar a ação de confirmar ou gravar uma senha
        self.btn_senha = Button(self.window_entry, text=self.text_btn, bd=2, bg='#6095C9', fg='white', font=('verdana',12,'bold'), command=self.verificar_senha)
        self.btn_senha.place(relx=0.5, rely=0.80, anchor='center')
    
    # Função para alternar exibição da senha
    def toggle_senha(self):
        if self.ver_senha_var.get() == 1:
            self.senha_txt_entry.config(show='')
        else:
            self.senha_txt_entry.config(show='*')
    
    # Função chamada pelo botão e determina se a senha será comparada ou armazenada
    def verificar_senha(self):
        # Armazena a senha escrita na caixa de texto
        wr_senha = self.senha_txt_entry.get()
        r_senha = self.get_senha()
    
        # Verifica se existe uma senha, ou seja, se a senha salva no JSON não é nula
        if r_senha != None:
            if wr_senha == r_senha:
                print("Senha correta!")
                
                # Lê a senha já armazenada
                with open("senha.json") as file:
                    data = json.load(file)
                
                # Altera o campo confirn para True
                data['confirn'] = True

                # Abre o arquivo com modo de escrita e cria um novo objeto à partir de um dicionário
                with open("senha.json", 'w') as file:
                    json.dump(data, file, indent=2)

            else:
                print("Senha incorreta!")

        # Caso seja nula, adicionamos uma nova senha
        else:
            print("Senha cadastrada!")
            self.set_senha(wr_senha)
        
        # Fecha a janela
        self.window_entry.destroy()