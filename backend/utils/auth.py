# flask-react-login/backend/utils/auth.py

from flask import session
from models.usuario import Usuario  # Importe a classe de modelo de usuário, ajuste o caminho conforme necessário
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from werkzeug.security import generate_password_hash, check_password_hash


def is_token_valid():
    try:
        verify_jwt_in_request()  # Verifique se o token está presente e válido
        user_id = get_jwt_identity()  # Obtenha o ID do usuário do token
        return user_id is not None  # Verifique se o ID do usuário está definido no token
    except Exception:
        return False
    
def criar_hash_senha(senha):
    #Cria um hash da senha fornecida.
    return generate_password_hash(senha)

def authenticate_user(email, senha):
    # Consulte o banco de dados para encontrar um usuário com o email fornecido
    usuario = Usuario.query.filter_by(email=email).first()

    # Verifique se o usuário existe e a senha está correta
    if usuario and usuario.verificar_senha(senha):
        return usuario.id  # Retorne o ID do usuário autenticado

    return None  # Retorne None se a autenticação falhar

def login_user(user_id):
    session['user_id'] = user_id

def logout_user():
    session.pop('user_id', None)

def is_logged_in():
    return 'user_id' in session
