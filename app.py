from flask import Flask, jsonify
from flask import Flask, jsonify, request, send_file
import application.submit_action as submit
import config
import structure.doc_interface as structure
import os
import requests
import urllib.parse
base_url= 'http://192.168.0.20:5000'
app = Flask(__name__)
dir_save =  config.dir_save()

@app.route('/')
def home():
    return jsonify({"message": "Bem-vindo ao gerador de Historias por IA"})

@app.route('/health', methods=['GET'])
def submitteste_action():
    return jsonify(message="Tudo certo com a aplicação")

@app.route('/download/<title>', methods=['GET'])
def download(title):
    print("--- Return Download")
    string_decodificada = urllib.parse.unquote(title)
    caminho_zip_to_download = os.path.join(dir_save, f'{string_decodificada}/{string_decodificada}.zip')
    print(caminho_zip_to_download)
    return send_file(caminho_zip_to_download, as_attachment=True, download_name=f'{title}.zip', mimetype="application/zip")

@app.route('/submit', methods=['POST'])
def data_handler():
    data = request.json
    response = submit.submit_action(data)
    if response[2] == 201:
        print('--- Init Download')
        # Construc Download
        title = data['title']
        download = structure.create_download_file(response[0], response[1], title)
        # Define o caminho completo do arquivo ZIP a ser salvo
        caminho_zip = os.path.join(dir_save, f'{title}/{title}.zip')
        structure.save_zip(caminho_zip, download)
        return jsonify({"success": True, "data": "Ser arquivo Foic riado com sucesso, consulte /download/<title>"})
        # return send_file(download, as_attachment=True, download_name=f'{title}.zip', mimetype="application/zip")
    else:
        # return jsonify({"success": True, "data": req.content})
        return jsonify({"success": False, "data": response[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))