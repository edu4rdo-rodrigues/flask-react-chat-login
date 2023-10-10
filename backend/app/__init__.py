# flask-react-chat-login/backend/app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

# Carrega as variáveis de ambiente a partir do arquivo .env
load_dotenv()

PORT = os.environ['REACT_APP_PORT_FRONTEND']

app = Flask(__name__)
app.debug = True

# Configuração do CORS para permitir acesso de qualquer origem
CORS(app, resources={r"/*": {"origins": f"http://localhost:{PORT}"}})
