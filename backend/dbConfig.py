# flask-react-chat-login/backend/config.py

from app import app
import os
from dotenv import load_dotenv

class Config:
    # Chave secreta para proteger sessões e outros dados
    SECRET_KEY = 'secret-key-goes-here'

    # Carrega as variáveis de ambiente a partir do arquivo .env
    load_dotenv()

    DATABASE_MYSQL_URL = os.environ['DATABASE_MYSQL_URL']

    # URL do banco de dados MySQL
    SQLALCHEMY_DATABASE_URI = DATABASE_MYSQL_URL

    # Desativa o rastreamento de modificações do SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
