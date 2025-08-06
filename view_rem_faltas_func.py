2# Importando biblioteca tkinter e o método adicional ttk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Importando pacote para trabalhar com as planilhas
from func_planilha import Func_planilhas

# Classe para Janela de alteração da senha armazenada no arquivo JSON
class App_Rem_Falta_Func(Func_planilhas):
    # Método construtor
    def __init__(self, w_main=None, colaboradores=None):
        # Inicializando as configurações principais da janela
        self.window_alt = Toplevel()
        self.w_main = w_main
        super().__init__()

        self.colaboradores = colaboradores
        self.screen_alt()
        self.widgets_window_alt()

    # Configuração da Janela
    def screen_alt(self):
        self.window_alt.title("Remover Faltas Funcionário")
        self.window_alt.configure(background = "#043F7C")
        self.window_alt.geometry('450x225')
        self.window_alt.resizable(False, False)
        self.window_alt.transient(self.w_main)
        self.window_alt.focus_force()
        self.window_alt.grab_set()
    
    # Configuração dos widgets da Janela
    def widgets_window_alt(self):
        # Variável de controle da data
        data_var = StringVar()

        def formatar_data(*args):
            # Pega a posição atual do cursor
            pos_cursor = self.data_entry.index(INSERT)

            # Valor atual da Entry
            valor_original = data_var.get()

            # Aceita um único caractere '*'
            if valor_original == "*":
                return 

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

        # Label para senha atual
        self.text1_lbl = Label(self.window_alt, text="Colaborador:", bg='#043F7C', foreground='white', font=('verdana',14,'bold'))
        self.text1_lbl.place(relx=0.05, rely=0.06)

        # Caixa de entrada de texto para confirmar senha atual
        self.cb_colab_atestado = ttk.Combobox(self.window_alt, values=self.colaboradores, font=('verdana',12), state='readonly')
        self.cb_colab_atestado.place(relx=0.5, rely=0.25, width=360, anchor='center')

        # Label para nova senha
        self.text2_lbl = Label(self.window_alt, text="Data:", bg = '#043F7C', foreground='white', font=('verdana',14,'bold'))
        self.text2_lbl.place(relx=0.05, rely=0.36)

        # Caixa de entrada de texto para nova senha
        self.data_entry = Entry(self.window_alt, textvariable=data_var, font=('verdana', 12))
        self.data_entry.place(relx=0.5, rely=0.55, width=360, anchor='center')

        # Botão de confirmar
        self.btn_alt = Button(self.window_alt, text="Remover faltas", bd=2, bg='#6095C9', fg='white', font=('verdana',12,'bold'), command=self.definir_falta_atestado)
        self.btn_alt.place(relx=0.5, rely=0.89, anchor='center')
    
    # Método para remover as faltas dos funcionários
    def remover_falta(self):
        cod = self.get_cod(self.cb_colab_atestado.get())[0][0]
        data = self.data_entry.get()
        dia, mes, ano = int(data[:2]), int(data[3:5]), data[6:]
        path = self.get_sheet_path(f'{mes:02d}-{ano}', f'{cod}-{mes:02d}-{ano}.xlsx')

        if path != '':
            if self.inserir_atestado(dia, path) == 1:
                messagebox.showinfo('Aviso', 'Atestado adicionado')
            else:
                messagebox.showinfo('Aviso', 'Não houve falta neste dia')
        else:
            messagebox.showinfo('Aviso', 'Planilha não encontrada')