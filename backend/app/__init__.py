# flask-react-chat-login/backend/app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from varEnv.exportVenv import (
    API_FRONTEND_URL, 
)


# Carrega as variáveis de ambiente a partir do arquivo .env
load_dotenv()


app = Flask(__name__)
app.debug = True

# Configuração do CORS para permitir acesso de qualquer origem
CORS(app, resources={r"/*": {"origins": API_FRONTEND_URL}})
