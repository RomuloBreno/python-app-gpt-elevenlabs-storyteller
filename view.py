
import app.widgets as widgets
import config as config_
import tkinter as tk
import base.prompt.prompt as prompt_construct

# Insira sua chave da API da OpenAI aqui
config_contruct = config_.config_construct()
dir_save = config_contruct['appSettings']['dir']['save']
global_dir_save = dir_save

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("NewStory")
        self.root.geometry("800x650")  # Define o tamanho da janela

        # Criação dos widgets
        widgets.create_widgets(self,root,global_dir_save)


# Cria a janela principal
if __name__ == "__main__":
    root = tk.Tk()  # Instancia o Tkinter
    app = App(root)  # Passa a janela principal para a classe
    root.mainloop()  # Executa a aplicação
