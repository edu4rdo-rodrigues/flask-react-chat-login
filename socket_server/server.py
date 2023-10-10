from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")  # Permitir origens de qualquer lugar. Você pode ajustar isso conforme sua necessidade.


@socketio.on('connect')
def handle_connect():
    print('Cliente conectado ao servidor Socket.io python')


@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))


@socketio.on('message')
def handle_message(message):
    print('Received message:', message)


if __name__ == '__main__':
    socketio.run(app, debug=True)
