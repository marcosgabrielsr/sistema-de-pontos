#Funções gerais para view pontos
from tkinter import *

class Func_view_pontos():
    # Função para limpar os campos de entrada da janela de pontos
    def clear_entry_pontos(self):
        self.codigo_entry.delete(0, END)
        self.cb_nome.set('')
        self.data_entry.delete(0, END)
        self.horario_entry.delete(0, END)
        self.cb_momento.set('')