from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit
import connection
import os
app = Flask(__name__)
socketio = SocketIO(app)
connection.socket = socketio
app.debug = True
CORS(app)

import ui as ui


@socketio.on('from_client')
def handle_from_client(json):
    print('Received json: ' + str(json))
    #print('Received value: ' + str(json['value']) + ' from client id ' + str(json['id']))
    connection.clientHandler(json['id'], json['value'], json['event_name'])
    # You can also set your variable here if you want
    # my_class_instance.my_var = json['value']

ui_src = ui.UI()

@app.route('/')
def home():
    return send_from_directory("output", "index.html")

image_names = os.listdir('./output/images')
images = [{'name': n, 'url': os.path.join('output/images', n)} for n in image_names]


@app.route('/image/<int:index>')
def image(index):
    return send_file(images[index]['url'])


@app.route('/<path:path>')
def files(path):
    return send_from_directory("output", path)


@app.route('/init', methods=['GET'])
def get_render():    
    if ui_src is None:
        return jsonify({'result': 'init not called'})
    else:
        return ui_src

if __name__ == '__main__':
    app.run(port=5000, debug=True)