import os
import re
from flask import send_file
import zipfile
import os

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

def create_zip(files):
    try:
        print("--- Init create zip")
        file_txt = files['txt']
        file_json = files['json']
        file_audio =  files['audio']

        # Criar um arquivo zip em memória
    except Exception as e:
        return f"Erro na criação do buffer zip | {e}"
   
    import io
    # Cria um buffer em memória
    zip_buffer = io.BytesIO()
    try:    
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.write(file_txt, files['txt'])
            zip_file.write(file_json, files['json'])
            zip_file.write(file_audio, files['audio'])
        
        # Voltar ao início do buffer para leitura
        zip_buffer.seek(0)
        return zip_buffer
    except Exception as e:
        return f"Erro na escrita do zip | {e}"
