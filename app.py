from flask import Flask, jsonify
from flask import Flask, jsonify, request
import application.submit_action as submit
import config
import os

app = Flask(__name__)


# config_ = config.load_config()
#dir_save = config_['appSettings']['dir']['save']
dir_save =  config.dir_save()

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Bem-vindo ao gerador de documentos por IA"})

@app.route('/health', methods=['GET'])
def submitteste_action():
    return jsonify(message="Tudo certo com a aplicação")

@app.route('/submit', methods=['POST'])
def data_handler():
    data = request.json
    response = submit.submit_action(dir_save,data)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))