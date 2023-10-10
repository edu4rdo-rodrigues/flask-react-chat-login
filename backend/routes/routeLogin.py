# flask-react-chat-login/backend/routes/routeLogin.py

from flask import jsonify, request
from models.usuario import Usuario, db
from utils.auth import authenticate_user, login_user

def login_dados_route(app):
    @app.route('/login', methods=['POST'])
    def login():
        if request.method == 'POST':
            data = request.json
            email = data.get('email')
            senha = data.get('senha')

            # Autenticar o usuário e obter o ID
            user_id = authenticate_user(email, senha)

            if user_id:
                login_user(user_id)
                user_info = {"email": email, "id": user_id, "nome": "a"}  # Substitua isso pelos detalhes reais do usuário
                print(f'Login bem-sucedido! Usuário: {user_info}')  # Exibe no console
                return jsonify({"message": "Logado com sucesso", "user_info": user_info})

        return jsonify({"error": "Credenciais inválidas"}), 401
