from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit
import connection
import os
app = Flask(__name__)
socketio = SocketIO(app)
connection.socket = socketio
app.debug = True
CORS(app)

import ui

ui_src = ui.UI()

@socketio.on('from_client')
def handle_from_client(json):
    print('Received value: ' + str(json['value']) + ' from client id ' + str(json['id']))
    connection.clientHandler(json['id'], json['value'], json['event_name'])
    # You can also set your variable here if you want
    # my_class_instance.my_var = json['value']

@app.route('/')
def home():
    return send_from_directory("output", "index.html")

@app.route('/images')
def image():
    image_names = os.listdir('./images/')
    images = [{'name': n, 'url': os.path.join('images', n)} for n in image_names]
    return str(images)  # just returning the string representation of list for testing


@app.route('/images/<int:index>')
def image():
    return send_from_directory("images", "index.html")


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