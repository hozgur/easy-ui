from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='./output')
CORS(app)
init = None


@app.route('/')
def home():
    return send_from_directory("output", "index.html")

@app.route('/static/<path:path>')
def files(path):
    return send_from_directory("output", path)


@app.route('/init', methods=['GET'])
def get_render():    
    if init is None:
        return jsonify({'result': 'init not called'})
    else:
        return init
    
@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    result = data['a'] * data['b']
    return jsonify({'result': result})


def start(port = 5000):
    app.run(port=port)

if __name__ == '__main__':
    app.run(port=5000)