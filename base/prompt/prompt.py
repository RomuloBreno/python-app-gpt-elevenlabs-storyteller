import config as config_
import os
def define_prompt(text_value):
        dir_local = config_.dir_local()
        prompt = config_.config_prompt()
        try:
            # Roteiro Base para o chat modelar o TXT
            with open(dir_local+"base/prompt/base_txt.txt", 'r', encoding='utf-8') as file:
                txt_base = file.read()

            # JSON Base para o chat modelar o arquivo JSON para o evenlabs consumir
            with open(dir_local+"base/prompt/base_json.json", 'r', encoding='utf-8') as file:
                json_base = file.read()
            # Monta a mensagem para o modelo
            model_prompt = f"Levando em consideração o modelo apresentado abaixo\n\n{txt_base}"
            roles_prompt = f"\n\nPreciso que crie uma roteiro para narrador para a midia {prompt['midia']} com duração de {prompt['time']} em um TXT identico ao modelo sobre o assunto: "
            convert_prompt = f"\n\nApós isso crie um JSON identico ao modelo {json_base} com base no TXT criado"

            prompt = f"{model_prompt}{roles_prompt}{text_value}\n\n{convert_prompt}"
            return prompt, True
        except:
             return "Erro na validação dos modelos", False




