from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_cors import CORS
from varEnv.exportVenv import API_FRONTEND_URL

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'

CORS(app, resources={r"/*": {"origins": f"{API_FRONTEND_URL}"}})

# Criar uma instância do Socket.IO
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    print('Cliente conectado ao servidor Socket.io python')

@socketio.on('disconnect')
def handle_disconnect():
    print('Cliente Desconectado ao servidor Socket.io python')


@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))


@socketio.on('message')
def handle_message(message):
    print('Received message:', message)


if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
