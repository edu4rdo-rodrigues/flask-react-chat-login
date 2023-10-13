# flask-react-chat-login/backend/routes/routeVerificaUser.py

from flask import Flask, request, jsonify
from models.usuario import Usuario




def verifica_user(app):

    @app.route('/user/<int:user_id>', methods=['GET'])
    def get_user_by_id(user_id):
        user = Usuario.query.get(user_id)
        if user:
            return jsonify({'id': user.id, 'name': user.nome})
        else:
            return jsonify({'message': 'Usuário não encontrado'}), 404
