# flask-react-chat-login/backend/routes/routeVerificaLogado.py

'''
from flask import Flask, request, jsonify
from utils.auth import is_token_valid
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Modifique a função para aceitar 'app' como argumento
def verifica_logado(app):
    @app.route('/verifica-logado', methods=['GET'])
    def esta_logado():
        token = request.headers.get('Authorization').split('Bearer ')[1]
        
        if is_token_valid():
            return jsonify({'message': 'Usuário está logado'})
        else:
            return jsonify({'message': 'Usuário não está logado'}), 401'''