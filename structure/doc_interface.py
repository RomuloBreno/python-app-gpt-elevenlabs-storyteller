import os
from pathlib import Path
import re
# Criando a pasta, se não existir

def create_doc(resp, dir, title):
    if title:
        dir_create = os.path.join(dir, title) # Salva o dir escolhido
        file_name = title + ".txt" # Cria o nome do arquivo
        path_save = os.path.join(dir_create, file_name) # Cria p dirretoria completo para salvar o arquivo
        os.makedirs(dir_create, exist_ok=True)
        with open(path_save, 'w') as arquivo:
            arquivo.write(resp)
    print(f"--- Texto salvo: {path_save}")
    return path_save

def save_audio(audio, dir, title):
    try:
        CHUNK_SIZE = 1024
        dir_create = os.path.join(dir, title) # Salva o dir escolhido
        file_name = title + ".mp3" # Cria o nome do arquivo
        path_save = os.path.join(dir_create, file_name) # Cria diretorio completo para salvar o arquivo
        with open(path_save, 'wb') as f:
            for chunk in audio.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
        print("--- Save audio")
    except:
        return False
# Função para separar o JSON do texto
def separar_json_txt(dir, title, arquivo_origem):
    try:
        dir_create = os.path.join(dir, title) # Salva o dir escolhido
        path_save = os.path.join(dir_create, title)

        with open(arquivo_origem, 'r') as f:
            conteudo = f.read()

        # Extrair o conteúdo JSON
        padrao_json = re.search(r'{(.|\n)*}', conteudo)
        
        if padrao_json:
            json_str = padrao_json.group()
            
            # Salvar o JSON em um arquivo separado
            with open(path_save + '.json', 'w', encoding='utf-8') as json_file:
                json_file.write(json_str)

        # Extrair o conteúdo do modelo TXT (tudo antes do JSON)
        txt_str = conteudo.replace(json_str, '').strip()
        
        # Salvar o modelo TXT em um arquivo separado
        with open(path_save + '.txt', 'w', encoding='utf-8') as txt_file:
            txt_file.write(txt_str)
        return json_file, True
    except:
        return "Error split JSON and TXT", False