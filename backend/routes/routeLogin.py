# flask-react-chat-login/backend/routes/routeLogin.py

from flask import jsonify, request
import jwt  # Você precisará instalar a biblioteca JWT
from models.usuario import Usuario, db
from utils.auth import authenticate_user, login_user, is_token_valid
from werkzeug.security import generate_password_hash, check_password_hash

def login_dados_route(app):

    # Esta é uma chave secreta usada para assinar o token. Deve ser mantida em segredo.
    app.config['SECRET_KEY'] = 'chave_secreta'

    # Dicionário para mapear IDs de usuário para tokens
    user_tokens = {}

    @app.route('/login', methods=['POST'])
    def login():
        if request.method == 'POST':
            data = request.json
            email = data.get('email')
            senha = data.get('senha')

            def criar_hash_senha(senha):
                #Cria um hash da senha fornecida.
                return generate_password_hash(senha)
            
            senha_hash = criar_hash_senha(senha)

            
        


            # Autenticar o usuário e obter o ID
            user_id = authenticate_user(email, senha)

            if user_id:
                # Gere um token JWT
                token = jwt.encode({'user_id': user_id}, app.config['SECRET_KEY'], algorithm='HS256')

                # Armazene o token associado ao ID do usuário
                user_tokens[user_id] = token
                

                login_user(user_id)

                user_info = {"email": email, "senha": senha_hash, "id": user_id, "user_tokens": user_tokens }  # Substitua isso pelos detalhes reais do usuário
                
                
                
                print(f'Login bem-sucedido! Usuário: {user_info}')  # Exibe no console
                return jsonify({"message": "Logado com sucesso", "user_info": user_info})

        return jsonify({"error": "Credenciais inválidas"}), 401
