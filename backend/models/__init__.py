# flask-react-chat-login/backend/models/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

# Carrega as variáveis de ambiente a partir do arquivo .env
load_dotenv()

app = Flask(__name__)
app.debug = True

USER = os.environ['USER_DB']
PASSWORD = os.environ['PASSWORD_DB']
DATABASE = os.environ['DB_BACKEND']
PORT = os.environ['REACT_APP_PORT_FRONTEND']

# Configuração do SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{USER}:{PASSWORD}@localhost/{DATABASE}'
db = SQLAlchemy(app)

# Configuração do CORS para permitir acesso de qualquer origem
CORS(app, resources={r"/*": {"origins": f"http://localhost:{PORT}"}})