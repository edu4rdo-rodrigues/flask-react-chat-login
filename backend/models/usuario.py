# flask-react-chat-chat-login/backend/models/usuario.py

from models.__init__ import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha_hash = generate_password_hash(senha)  # Hash da senha

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)
