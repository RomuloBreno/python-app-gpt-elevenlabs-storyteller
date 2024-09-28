
import AI.chat_gpt as gpt
import AI.voice_elevenlabs as labs
import base.prompt.prompt as prompt_construct
import structure.doc_interface as manipule_docs
import json
import tkinter as tk
import config

# Acessar as configurações
config_ = config.load_config()
dir_save = config_['appSettings']['dir']['save']

def submit_action(self, global_dir_save):
    def access_text(text_value,context_value,title):
        try:
            # Cria o prompt
            prompt = prompt_construct.define_prompt(text_value)
            
            # Chamar Funções do chat
            response_gpt = gpt.connection_chatgpt(context_value, prompt)
            #response_gpt = "texto balablabla"

            # Pegar roteiro para IA
            file_name = manipule_docs.create_doc(response_gpt, global_dir_save, title)

            # Ler resposta do chat e separar arquivos
            json_gpt_response = manipule_docs.separar_json_txt(global_dir_save, title, file_name)
            return json_gpt_response
        except:
            return "erro na criação do roteiro"

    def access_voice(title,json_gpt_response):
        # JSON Base para o chat modelar o arquivo JSON para o evenlabs consumir
        try:
            print(json_gpt_response)
            with open(json_gpt_response, 'r', encoding='utf-8') as file:
                json_base = file.read()
            data = json.loads(json_base)
            response_eleven = labs.connection_elevenlabs(data['voice']['texto_completo'])
            file_name = manipule_docs.save_audio(response_eleven, global_dir_save, title)
            return file_name
        except:
            return "erro na criação da narração"

    # Captura os valores dos campos
    text_value = self.text_area.get("1.0", tk.END).strip()
    title = self.input_title.get()
    context_value = self.input_1.get()
    voice_value = self.voice_dropdown.get()

    text_value = "ANOS 90"
    title = "ANOS 90"
    context_value = "Historiador"
    json_gpt_response = access_text(text_value,context_value,title)
    access_voice(title,json_gpt_response.name)
