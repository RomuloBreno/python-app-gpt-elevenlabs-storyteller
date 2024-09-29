from flask import Flask, jsonify
from flask import Flask, jsonify, request
import application.submit_action as submit
import config
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, World!"})

# config_ = config.load_config()
#dir_save = config_['appSettings']['dir']['save']
dir_save =  config.dir_save()

app = Flask(__name__)

@app.route('/submitteste', methods=['GET'])
def submitteste_action():
    return jsonify(message="Hello, World!")

@app.route('/submit', methods=['POST'])
def data_handler():
    data = request.json
    response = submit.submit_action(dir_save,data)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))