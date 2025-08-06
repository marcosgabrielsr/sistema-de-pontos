# Importando pacote tkinter
from tkinter import *
from tkinter import messagebox

# Importando classe para gerar as planilhas
from func_planilha import Func_planilhas

class View_Planilha(Func_planilhas):
    def __init__(self, w_fp_main=None):
        self.w_fp = Toplevel()
        self.w_fp_main = w_fp_main
        super().__init__()

        self.screen_fp()
        self.widgets_fp()
    
    def screen_fp(self):
        self.w_fp.title("Gerar Planilha")
        self.w_fp.configure(background = "#043F7C")
        self.w_fp.geometry("400x200")
        self.w_fp.resizable(False, False)
        self.w_fp.transient(self.w_fp_main)
        self.w_fp.focus_force()
        self.w_fp.grab_set()

    def on_validate_2(self, P):
        if len(P) <= 2:
            if P.isdigit() or P == "":
                return True
        return False
    
    def on_validate_4(self, P):
        if len(P) <= 4:
            if P.isdigit() or P == "":
                return True
        return False
    
    def widgets_fp(self):
        # Gerando título da janela
        self.title = Label(self.w_fp, text="Gerar Planilha", bg='#043F7C', fg='white', font=('verdana',16,'bold'))
        self.title.place(relx = 0.28, rely = 0.075)

        # Configurando Label e Caixa de Entrada do mes
        self.lb_mes = Label(self.w_fp, text="Mês:", bg='#043F7C', fg='white', font=('verdana',12,'bold'))
        self.lb_mes.place(relx = 0.12, rely = 0.33)

        validate_cmd_2 = self.w_fp.register(self.on_validate_2)

        self.entry_mes = Entry(self.w_fp, validate="key", validatecommand=(validate_cmd_2, "%P"))
        self.entry_mes.place(relx = 0.25, rely=0.305, relwidth = 0.1, relheight=0.15)

        # Configurando Label e Caixa de Entrada do ano
        self.lb_ano = Label(self.w_fp, text = "Ano:", bg = '#043F7C', fg = 'white', font = ('verdana', 12, 'bold'))
        self.lb_ano.place(relx = 0.51, rely = 0.33)

        validate_cmd_4 = self.w_fp.register(self.on_validate_4)

        self.entry_ano = Entry(self.w_fp, validate="key", validatecommand=(validate_cmd_4, "%P"))
        self.entry_ano.place(relx = 0.64, rely = 0.305, relwidth = 0.25, relheight = 0.15)

        # Configurando botão
        self.button_aplicar = Button(self.w_fp, text="Aplicar", bd=2, bg='#6095C9', fg='white', font=('verdana',12,'bold'), command=self.gerar_planilhas)
        self.button_aplicar.place(relx = 0.36, rely = 0.73)

    def gerar_planilhas(self):
        mes = int(self.entry_mes.get())
        ano = int(self.entry_ano.get())
        super().gerar_planilhas(mes, ano)
        self.w_fp.destroy()
        messagebox.showinfo("Aviso", "Planilhas criadas")