import openai
import json
from functools import partial
import config

api_key = config.keygpt()


# Configura a chave da API
openai.api_key = api_key

def connection_chatgpt(context, prompt, modelo="gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(
            model=modelo,
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": prompt},
            ]
        )
        # Extrair a resposta gerada
        print("--- Connecting gpt")
        resposta = response['choices'][0]['message']['content']
        return resposta, True

    except Exception as e:
        return f"Ocorreu um erro: {e}", False
    
