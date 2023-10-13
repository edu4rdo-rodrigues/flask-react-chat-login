# flask-react-chat-login/backend/routes/routeLogin.py

from flask import jsonify, request
import jwt  # Você precisará instalar a biblioteca JWT
from utils.auth import authenticate_user, login_user, criar_hash_senha
from cores.Cor import Cor

def login_dados_route(app):
    
    # Esta é uma chave secreta usada para assinar o token. Deve ser mantida em segredo.
    app.config['SECRET_KEY'] = 'chave_secreta'

    # Dicionário para mapear IDs de usuário para tokens
    user_tokens = {}
    
    @app.route('/login', methods=['POST'])
    def login():
        
        if request.method == 'POST':
            data = request.json
            nome = data.get('nome')
            email = data.get('email')
            senha = data.get('senha')

            senha_hash = criar_hash_senha(senha)

            # Autenticar o usuário e obter o ID
            user_id = authenticate_user(email, senha)

            if user_id:
                # Gere um token JWT
                token = jwt.encode({'user_id': user_id}, app.config['SECRET_KEY'], algorithm='HS256')

                # Armazene o token associado ao ID do usuário
                user_tokens[user_id] = token
                
                login_user(user_id)

                user_info = {
                    "nome": nome,
                    "email": email, 
                    "senha": senha_hash, 
                    "id": user_id, 
                    "user_tokens": user_tokens 
                }  # Substitua isso pelos detalhes reais do usuário


                print(
                    Cor.VERDE + "Login bem-sucedido! Usuário: " + Cor.RESET,
                    "\n", Cor.VERDE + Cor.VERDE + f"ID: {user_info['id']}" + Cor.RESET,
                    "\n", Cor.VERDE + f"Email: {user_info['email']}" + Cor.RESET,
                    "\n", Cor.VERDE + f"Senha: {user_info['senha']}" + Cor.RESET,
                    "\n", Cor.VERDE + f"user_tokens: {user_info['user_tokens']}" + Cor.RESET,
                )  # Exibe no console
                
                response = jsonify({"message": "Logado com sucesso", "user_info": user_info,})
                return response, 200
        
            else:
                data = request.json
                print(
                    Cor.VERMELHO + "Error Credenciais inválidas" + Cor.RESET,
                    "\n", Cor.VERMELHO + f"Email: {data['email']}" + Cor.RESET,
                    "\n", Cor.VERMELHO + f"Senha: {data['senha']}" + Cor.RESET
            
                )  # Exibe no console  

        response = jsonify({ "Backend error" : "Credenciais inválidas" })
        return response, 500,
