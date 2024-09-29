from elevenlabs import voice_generation  
import json
import requests
import config


my_api_key = config.keyeleven()
prompt = config.config_prompt()
voices_id = prompt['voices']
# Gere áudio a partir de um texto
def connection_elevenlabs(context,model="eleven_multilingual_v2"):
    try:
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voices_id[0]['voice_id']}"
        headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": f"{my_api_key}"
        }

        data = {
        "text": f"{context}",
        "model_id": f"{model}",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
        }
        print("--- Connecting elevenlabs")
        response = requests.post(url, json=data, headers=headers) 
        print(f"--- Content ElevenLbas{response}")
        return response, True
    except Exception as e:
        return f"Ocorreu um erro: {e}", False

# def get_voices():
#     # Defina a URL e a chave da API
#     url = f"https://api.elevenlabs.io/v1/voices/{voices_id[0]['voice_id']}"
#     # Defina os cabeçalhos da requisição
#     headers = {
#         "xi-api-key": my_api_key
#     }
#     # Realizando a requisição GET
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         voices = response.json()
#         voices_str = "["+json.dumps(voices)+"]"
#         data = json.loads(voices_str)
#     # Definir a classe para representar a voz
#         class Voice:
#             def __init__(self, voice_id, name, category, labels):
#                 self.voice_id = voice_id
#                 self.name = name
#                 self.category = category
#                 self.labels = labels

#             def __repr__(self):
#                 return f"{self.name}"
#         voices_list = [
#             Voice(
#                 name=voices['name'],
#                 voice_id=voices['voice_id'],
#                 category=voices['category'],
#                 labels=voices['labels']
#             )
#             for voices in data
#         ]

#         return voices_list
#     else:
#         print(f"Erro: {response.status_code} - {response.text}")



