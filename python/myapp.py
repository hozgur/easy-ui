from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app)

import ui

ui_src = ui.UI()

@app.route('/')
def home():
    return send_from_directory("output", "index.html")

@app.route('/<path:path>')
def files(path):
    return send_from_directory("output", path)


@app.route('/init', methods=['GET'])
def get_render():    
    if ui_src is None:
        return jsonify({'result': 'init not called'})
    else:
        return ui_src
    
@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    result = data['a'] * data['b']
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(port=5000, debug=True)