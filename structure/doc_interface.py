import io
import re
from flask import send_file
import zipfile
import json
from pydub import AudioSegment
from flask import send_file

def create_json(resp):
    print("--- Init Create JSON")
    # Extrair o conteúdo JSON

    padrao_json = re.search(r'\{.*?\}', resp, re.DOTALL) 
      
    if padrao_json:
        # Extrair a parte do JSON
        json_str = padrao_json.group(0)
    print(json_str)
    return json_str

def create_txt(resp, json_str):
    print("--- Init create TXT")
    if resp:
        # Extrair o conteúdo do modelo TXT (tudo antes do JSON)
        txt_str = resp.replace(json_str, '').strip()
        # Salvar o modelo TXT em um arquivo separado
    else:
        return None
    return txt_str
    
def save_audio(audio):
    try:
        audio_buffer = io.BytesIO(audio)
        audio_file = AudioSegment.from_file(audio_buffer, format="mp3")
        return audio_file, True
    except:
        return None, False

def create_zip(txt, json,title):
    zip_buffer = io.BytesIO()
    json_buffer = io.StringIO()
    txt_buffer = io.StringIO()
    json_buffer.write(txt)
    txt_buffer.write(json)

    try:    
        print("--- Init create zip to download")
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
            zip_file.writestr(f'{title}.txt', txt_buffer.getvalue())
            zip_file.writestr(f'{title}.json', json_buffer.getvalue())
        
        # Voltar ao início do buffer para leitura
        zip_buffer.seek(0)
        return zip_buffer
    except Exception as e:
        return f"Erro na escrita do zip | {e}"

def create_download_file(txt, json, title):
    file_zip = create_zip(txt, json,title)
    # Enviar o arquivo para o cliente
    return file_zip

def create_doc(response_gpt):
    print("--- Init Create Docs")
    create_json_file = create_json(response_gpt)
    create_txt_file = create_txt(response_gpt, create_json_file)
    if not create_json_file and create_txt_file:
        return f"Error create document | {create_json_file} | {create_txt_file}", None,  False
    print("--- Docs Created")
    return create_txt_file, create_json_file , True