from flask import Flask, jsonify
from flask import Flask, jsonify, request, send_file
import application.submit_action as submit
import config
import structure.doc_interface as structure
import os

app = Flask(__name__)

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
    if response[1] == 201:
        download_file(response)
        return jsonify({"success": True, "data": response[0]})
    return jsonify({"success": False, "data": response[0]})

@app.route('/download/<name_file>', methods=['GET'])
def download_file(name_file):
    # Caminho do arquivo temporário
    try:
        print("--- Init download")
        data = {
                "txt":f"{dir_save}{name_file}/{name_file}.txt",
                "json":f"{dir_save}{name_file}/{name_file}.json",
                "audio":f"{dir_save}{name_file}/{name_file}.mp3",
        }
    except Exception as e:
        return f"Erro na contrução do JSON dos arquivos | {e}", 404
    
    file_zip = structure.create_zip(dir_save,data, name_file)
    # Enviar o arquivo para o cliente
    return send_file(file_zip, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))