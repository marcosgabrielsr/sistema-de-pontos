# Importando biblioteca para trabalhar com o sistema operacional
import os

class Folders():
    # Função que cria a pasta planilhas, onde serão armazenadas todas as pastas de todos os meses
    # contendo as planilhas de pontos de todos os funcionários
    def create_planilhas(self):
        #Obtendo diretório do arquivo
        diret = os.path.dirname(os.path.realpath(__file__))

        #Juntando o diretório atual com 
        path_folder = os.path.join(diret, "planilhas")

        #Tenta criar a pasta planilhas caso ela não exista
        try:
            os.makedirs(path_folder)        
        #caso a pasta já exista
        except FileExistsError:
            print("A pasta *planilhas* já existe!")

    # Função que cria as pastas referente ao mes atual
    def create_folder_mes(self, folder_name):
        # Obtendo diretório do arquivo
        diret = os.getcwd()

        # Gerando caminho da nova pasta
        new_path = os.path.join(diret, 'planilhas', folder_name)

        # Verifique se a pasta já existe antes de criar
        if not os.path.exists(new_path):
            # Caso não exista, cria a nova pasta
            os.makedirs(new_path)
            print(f"A pasta '{new_path}' foi criada com sucesso.")
        else:
            # Caso exista, imprime uma mensagem na tela
            print(f"A pasta '{new_path}' já existe.")

    # Verifica se uma determinada planilha existe
    def get_sheet_path(self, folder_name, sheet_name):
        # Obtendo diretório atual do arquivo
        direct = os.getcwd()
        path = os.path.join(direct, 'planilhas', folder_name, sheet_name)
        print(f'path: {path}')

        # Verifica se a planilha existe
        if os.path.exists(path):
            print(f'Planilha encontrada no caminho: {path}')
            return path
        else:
            print('Planilha não encontrada')
            return ''