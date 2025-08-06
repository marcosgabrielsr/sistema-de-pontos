from tkinter import *

class Func_view_colab():
    def clear_entry(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.senha_entry.delete(0, END)