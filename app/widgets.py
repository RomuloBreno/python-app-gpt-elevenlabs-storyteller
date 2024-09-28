import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import AI.voice_elevenlabs as labs
import app.buttons as buttons

def select_dir(global_dir_save):
    # Abre um diálogo para selecionar um diretório
    global_dir_save = filedialog.askdirectory(title="Selecione um diretório para salvar seus arquivos")
    messagebox.showinfo("Diretório Selecionado", f"Você selecionou: {global_dir_save}")

def create_widgets(self, root,global_dir_save):
        # Botão para abrir o seletor de diretório
        label_input_dir = tk.Label(self.root, text="Selecione um diretório para salvar seus arquivos")
        label_input_dir.pack(pady=5)
        botao_selecionar = tk.Button(root, text="Selecione um diretório", command=select_dir)
        botao_selecionar.pack(pady=15)

        # Label e Input (Título)
        label_input_title = tk.Label(self.root, text="Digite o título")
        label_input_title.pack(pady=5)
        self.input_title = tk.Entry(self.root, width=40)
        self.input_title.pack(pady=5)

        # Label e TextArea (Texto principal)
        label_text_area = tk.Label(self.root, text="Digite sobre o que deseja escrever:")
        label_text_area.pack(pady=5)
        self.text_area = tk.Text(self.root, height=5, width=40)
        self.text_area.pack(pady=5)

        # Label e Input (Contexto)
        label_input_1 = tk.Label(self.root, text="Direcione o chat com um contexto:")
        label_input_1.pack(pady=5)
        self.input_1 = tk.Entry(self.root, width=40)
        self.input_1.pack(pady=5)

        # Label e Dropdown (Escolha da voz)
        label_voice_dropdown = tk.Label(self.root, text="Escolha a voz:")
        label_voice_dropdown.pack(pady=5)

        # Lista de vozes (substitua com os dados reais da API)
        voices = labs.get_voices()
        self.voice_dropdown = ttk.Combobox(self.root, values=voices, state="readonly")
        self.voice_dropdown.current(0)  # Define a primeira voz como padrão
        self.voice_dropdown.pack(pady=5)

        # Botão de submissão
        submit_button = tk.Button(self.root, text="Enviar", command=lambda: submit(self, global_dir_save))
        submit_button.pack(pady=10)



def submit(self, global_dir_save):
      buttons.submit_action(self,global_dir_save)