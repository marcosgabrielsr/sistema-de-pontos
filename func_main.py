#============================================================================================================================
    #Aqui estão as principais funções da janela main
#============================================================================================================================
from tkinter import *
from tkinter import messagebox

class Func():
    #Função que limba as combo box
    def clear_cb(self):
        self.cb_colab.set('')
        self.cb_turnos.set('')
        self.main_entry_senha.delete(0, END)