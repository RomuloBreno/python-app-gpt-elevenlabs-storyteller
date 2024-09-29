from flask import Flask, jsonify
from flask import Flask, jsonify, request, send_file
import application.submit_action as submit
import config
import structure.doc_interface as structure
import os

app = Flask(__name__)

# config_ = config.load_config()
#dir_save = config_['appSettings']['dir']['save']
dir_save =  config.dir_save()
FOLDER = dir_save

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
    download_file(response)
    return response

@app.route('/download/<names_files>', methods=['GET'])
def download_file(names_files):
    # Caminho do arquivo temporário
    try:
        data = {
            {
                "txt":f"{FOLDER}{names_files}.txt",
                "json":f"{FOLDER}{names_files}.json",
                "audio":f"{FOLDER}{names_files}.audio",
                "title":f"{FOLDER}{names_files}"
            }
        }
    except Exception as e:
        return f"Erro na contrução do JSON dos arquivos | {e}", 404
    
    file_zip = structure.create_zip(data)
    # Enviar o arquivo para o cliente
    return send_file(file_zip, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))