import json
import os


#Get keys
def keygpt():
    gpt = os.environ.get('gpt')
    return gpt

def keyeleven():
    eleven = os.environ.get('eleven')
    return eleven

def dir_save():
    dir_save = os.environ.get('dir_path')
    return dir_save


# AppSetting
def load_config(file_path='appsettings.Development.json'):
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
    return config

# Prompt
def load_prompt(file_path='base/prompt/prompt.json'):
    with open(file_path, 'r') as config_file:
        config = json.load(config_file)
    return config


# Acessar as configurações
def config_construct():
    config = load_config()
    return config

# Acessar as configurações
def config_prompt():
    config = load_prompt()
    return config