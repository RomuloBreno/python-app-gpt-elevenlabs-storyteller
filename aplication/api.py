# from flask import Flask, jsonify, request
# import app.submit_action as submit
# import config

# config_ = config.load_config()
# dir_save = config_['appSettings']['dir']['save']
# app = Flask(__name__)

# @app.route('/submitteste', methods=['GET'])
# def submitteste_action():
#     return jsonify(message="Hello, World!")

# @app.route('/submit', methods=['POST'])
# def data_handler():
#     data = request.json
#     response = submit.submit_action(dir_save,data)
#     return response

# if __name__ == '__main__':
#     app.run(debug=True)