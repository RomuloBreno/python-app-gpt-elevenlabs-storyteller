import AI.chat_gpt as gpt
import AI.voice_elevenlabs as labs
import base.prompt.prompt as prompt_construct
import structure.doc_interface as manipule_docs
import json
import config

dir_save = config.dir_save()

def get_response_gpt(text_value, context_value):
    try:
        prompt = prompt_construct.define_prompt(text_value)
        if prompt:
            response_gpt = gpt.connection_chatgpt(context_value, prompt)
            return response_gpt, None, True
    except:
        return f"Error create story | Erro de Conexão",  None, False
    
def get_response_eleven(doc_created):
    try:
        print("--- Init Create audio")
        print(doc_created)
        data = json.loads(doc_created)
        response_eleven = labs.connection_elevenlabs(data['voice']['texto_completo'])
        print(response_eleven)
        print(data)
        if not response_eleven[1]:
            return f"Error ElevenLabs connection | {response_eleven[0].content}", False
        file_name = manipule_docs.save_audio(response_eleven[0].content)
        print("--- End Save audio")
        if not file_name[1]:
            return f"Error File Name | {file_name[0]['detail']['message']}", False
        print(file_name)
        print(response_eleven[0].content)
        return file_name[0], True
    except:
        return "Error create storyteller", False

def submit_action(data_json):
    try:
        # Mapping JSON
        json_teste = json.loads(json.dumps(data_json))
        text_value = json_teste['text']
        # title = json_teste['title']
        context_value = json_teste['context']
        
        print("--- Init Valid Submit")

        json_gpt_response = get_response_gpt(text_value, context_value)
        docs = manipule_docs.create_doc(json_gpt_response[0])
        json_buffer_read = docs[0]
        text_buffer_read = docs[1]
        is_valid_doc = docs[2]

        if not is_valid_doc:
            return f"Error GPT : {text_buffer_read}, {json_buffer_read} ", None, 404
        # if json_gpt_response[2]:
            # print(json_buffer_read.getvalue())
            # json_elevenlabs_response = get_response_eleven(json_buffer_read.getvalue())
            # audio_buffer_read = json_elevenlabs_response[0]
            # is_valid_eleven = json_elevenlabs_response[1]

            # if not is_valid_eleven:
            #     return f"Error EvenLabs invalid | {audio_buffer_read}", None, 404

        print("--- End Valid Submit")
        return text_buffer_read, json_buffer_read, 201
    except:
        return "Error valid to JSON", json_gpt_response[0], 404


