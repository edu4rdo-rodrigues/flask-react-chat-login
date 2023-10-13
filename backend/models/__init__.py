# flask-react-chat-login/backend/models/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from varEnv.exportVenv import (
    API_FRONTEND_URL, 
    DATABASE_MYSQL_URL,
)


#print('database_mysql_url: ', database_mysql_url)

# Carrega as variáveis de ambiente a partir do arquivo .env
load_dotenv()

app = Flask(__name__)
app.debug = True

#print('api_frontend_url: ', PYTHON_APP_API_FRONTEND_URL)

# Configuração do SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_MYSQL_URL
db = SQLAlchemy(app)

# Configuração do CORS para permitir acesso de qualquer origem
CORS(app, resources={r"/*": {"origins": API_FRONTEND_URL}})