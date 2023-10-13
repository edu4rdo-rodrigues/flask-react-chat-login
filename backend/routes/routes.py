# flask-react-chat-login/backend/routes.py

from flask import Flask, jsonify, request
from models.usuario import Usuario, db
from flask_cors import CORS


from routes.routeCadastro import cadastrar_dados_route
from routes.routeLogin import login_dados_route
from routes.routeLogout import logout_dados_route
#from routes.routeVerificaLogado import verifica_logado

class Routes:
    def __init__(self, app):
        self.app = app
        CORS(app)

        # Chame a função para definir a rota de cadastro de dados
        cadastrar_dados_route(app)
        
        # Chame a função para definir a rota de login de dados
        login_dados_route(app)
        
        # Chame a função para definir a rota de logout de dados
        logout_dados_route(app)

        #verifica_logado(app)