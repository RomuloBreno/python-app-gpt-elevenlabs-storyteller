import json
import os
# Carrega as variáveis de ambiente do arquivo .env
from dotenv import load_dotenv
load_dotenv()

#Get keys
def keygpt():
    gpt = os.environ.get('gpt')
    return gpt

def keyeleven():
    eleven = os.environ.get('eleven')
    return eleven

def dir_save():
    dir_save = os.environ.get('dir_save')
    return dir_save

def dir_local():
    dir_local = os.environ.get('dir_local')
    return dir_local

# Prompt
def load_prompt(file_path='base/prompt/prompt.json'):
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
    return config

# Acessar as configurações do prompt
def config_prompt():
    config = load_prompt()
    return config