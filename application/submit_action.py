import AI.chat_gpt as gpt
import AI.voice_elevenlabs as labs
import base.prompt.prompt as prompt_construct
import structure.doc_interface as manipule_docs
import json
import config

### Dev
# # Acessar as configurações
# config_ = config.load_config()
# dir_save = config_['appSettings']['dir']['save']

dir_save = config.dir_save()

def submit_action(global_dir_save, data_json):
    def access_text(text_value,context_value,title):
        try:
            # Cria o prompt
            prompt = prompt_construct.define_prompt(text_value)
            if prompt[1]:
                # Chamar Funções do chat
                print("--- Init call gpt")
                response_gpt = gpt.connection_chatgpt(context_value, prompt[0])
                # Valid GPT response
                if not response_gpt[1]:
                    return f"Erro na criação do roteiro | {response_gpt[0]}" , False
                # Pegar roteiro para IA
                file_name = manipule_docs.create_doc(response_gpt[0], global_dir_save, title)

                # Ler resposta do chat e separar arquivos
                json_gpt_response = manipule_docs.separar_json_txt(global_dir_save, title, file_name)
                return json_gpt_response[0].name, True
            else:
                return f"Error invalid prompt return {prompt[0]}"
        except:
            if not response_gpt[1]:
                return f"Erro na criação do roteiro | Erro de Conexão" , False
            elif not json_gpt_response[1]:
                return f"Erro na criação do roteiro | {json_gpt_response[0]}" , False
            else:
                return f"Erro na criação do roteiro | {prompt[0]}" , False

    def access_voice(title,json_gpt_response_name):
        # JSON Base para o chat modelar o arquivo JSON para o evenlabs consumir
        try:
            with open(json_gpt_response_name, 'r', encoding='utf-8') as file:
                json_base = file.read()
            data = json.loads(json_base)
            print("--- Init call elevenlabs")

            response_eleven = labs.connection_elevenlabs(data['voice']['texto_completo'])
            if not response_eleven[1]:
                return f"Erro ElevenLabs | {response_eleven[0].content}", False
            
            file_name = manipule_docs.save_audio(response_eleven[0].content, global_dir_save, title)
            if not file_name:
                return f"Erro File Name | {file_name[0]['detail']['message']}", False
            
            return file_name, True
        except:
            return "Erro na criação da narração", False
   
   # Mapping JSON and Valid Returns
    try:
        json_teste = json.loads(json.dumps(data_json))
        text_value = json_teste['text']
        title = json_teste['title']
        context_value = json_teste['context']

        json_gpt_response = access_text(text_value,context_value,title)
        if not json_gpt_response[1]:
            return f"Error GPT : {json_gpt_response[0]}", 404
        
        json_elevenlabs_response = access_voice(title,json_gpt_response[0])
        if not json_elevenlabs_response[1]:
            return f"Error EvenLabs | {json_elevenlabs_response[0]}", 404
        
        return "Ok", 201
    except:
        return "Erro na validação do JSON", 404
        

    