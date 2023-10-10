# flask-react-chat-login/backend/config.py

from app import app
import os
from dotenv import load_dotenv

class Config:
    # Chave secreta para proteger sessões e outros dados
    SECRET_KEY = 'secret-key-goes-here'

    # Carrega as variáveis de ambiente a partir do arquivo .env
    load_dotenv()

    USER = os.environ['USER_DB']
    PASSWORD = os.environ['PASSWORD_DB']
    DATABASE = os.environ['DB_BACKEND']

    # URL do banco de dados MySQL
    SQLALCHEMY_DATABASE_URI = f'mysql://{USER}:{PASSWORD}@localhost/{DATABASE}'

    # Desativa o rastreamento de modificações do SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
