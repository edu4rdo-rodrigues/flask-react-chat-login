# flask-react-chat-login/backend/routes/routeLogin.py

from flask import jsonify
from models.usuario import Usuario, db
from utils.auth import logout_user, is_logged_in

def logout_dados_route(app):
    @app.route('/logout', methods=['GET'])
    def logout():
        if is_logged_in():
            logout_user()
            return jsonify({"message": "Logout realizado com sucesso"})
        return jsonify({"error": "Nenhum usuário logado"}), 401

