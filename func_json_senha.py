#Importanto o módulo para trabalhar com JSON
import json
import os

class Json_Senha():
    def get_senha(self):
        #Verifica se o arquivo json buscado já existe...
        if os.path.exists("senha.json"):
            #Lê a senha já armazenada
            with open("senha.json") as file:
                data = json.load(file)

        #Caso ele não exista...
        else:
            #Criando dicionário e armazenando a senha inicialmente como vazia(none)
            data = {'senha': None, 'confirn': False}

            #Abre o arquivo com modo de escrita e cria um novo objeto à partir de um dicionário
            with open("senha.json", 'w') as file:
                json.dump(data, file, indent = 2)
        
        return data['senha']

    def set_senha(self, new_senha):
        #Criando dicionário e armazenando a senha inicialmente como vazia(none)
        data = {'senha': new_senha, 'confirn': False}
        
        #Abre o arquivo com modo de escrita e cria um novo objeto à partir de um dicionário
        with open("senha.json", 'w') as file:
            json.dump(data, file, indent = 2)