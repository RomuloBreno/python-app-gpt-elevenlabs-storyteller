import json
import os
# Carrega as variáveis de ambiente do arquivo .env
from dotenv import load_dotenv
load_dotenv()

#Get keys
def keygpt():
    gpt = os.getenv('GPT')
    return gpt

def keyeleven():
    eleven = os.getenv('ELEVEN')
    return eleven

def dir_save():
    dir_save = os.getenv('DIR_SAVE')
    return dir_save

def dir_local():
    # Obtém o caminho do diretório onde o script atual está localizado
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return current_dir

# Prompt
def load_prompt(file_path='base/prompt/prompt.json'):
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
    return config

# Acessar as configurações do prompt
def config_prompt():
    config = load_prompt()
    return config