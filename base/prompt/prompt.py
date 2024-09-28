import config as os
config_contruct = os.config_construct()
dir = config_contruct['appSettings']['dir']['local']
def define_prompt(text_value):
        config_prompt = os.config_prompt()
        # Roteiro Base para o chat modelar o TXT
        with open(dir+"base/prompt/base_txt.txt", 'r', encoding='utf-8') as file:
            txt_base = file.read()


        # JSON Base para o chat modelar o arquivo JSON para o evenlabs consumir
        with open(dir+"base/prompt/base_json.json", 'r', encoding='utf-8') as file:
            json_base = file.read()
            

        # Monta a mensagem para o modelo
        model_prompt = f"Levando em consideração o modelo apresentado abaixo\n\n{txt_base}"
        roles_prompt = f"\n\nPreciso que crie uma roteiro para narrador para a midia {config_prompt['midia']} com duração de {config_prompt['time']} em um TXT identico ao modelo sobre o assunto: "
        convert_prompt = f"\n\nApós isso crie um JSON identico ao modelo {json_base} com base no TXT criado"

        prompt = f"{model_prompt}{roles_prompt}{text_value}\n\n{convert_prompt}"
        return prompt