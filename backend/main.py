# flask-react-chat-login/backend/main.py

import os
import argparse
from flask import Flask, jsonify
from flask_cors import CORS
from models.usuario import db
from routes.routes import Routes
from flask_migrate import Migrate
from dbConfig import Config
from dotenv import load_dotenv
from varEnv.exportVariables import PYTHON_APP_API_FRONTEND_URL 




# Carrega as variáveis de ambiente a partir do arquivo .env
load_dotenv()

# Crie um objeto ArgumentParser
parser = argparse.ArgumentParser(description='Run the Flask app with custom port.')

# Adicione um argumento para a porta
parser.add_argument('--port', type=int, default=5000, help='Port to run the Flask app on')

# Parse os argumentos da linha de comando
args = parser.parse_args()

app = Flask(__name__)
CORS(app, resources={r"/socket.io/*": {"origins": PYTHON_APP_API_FRONTEND_URL}})


api_url = os.environ.get("REACT_APP_API_URL")

# Carregue as configurações do objeto Config
app.config.from_object(Config)

# Inicialize o SQLAlchemy diretamente no main.py
db.init_app(app)

migrate = Migrate(app, db)
# Crie uma instância da classe Routes e passe o aplicativo Flask para ela
Routes(app)

with app.app_context():
    db.create_all()

# Manipulador de erro CORS personalizado
@app.errorhandler(500)
def handle_cors_error(e):
    return jsonify({"error": "Erro de CORS"}), 500

if __name__ == '__main__':
    #socketio_app = SocketIOApp()  # Crie uma instância da classe SocketIOApp
    #socketio_app.socketio.run(app, debug=True)
    app.run(debug=True, port=8000)
