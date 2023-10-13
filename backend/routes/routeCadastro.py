# flask-react-chat-login/backend/routes/routeCadastro.py

from flask import request, jsonify
from models.usuario import Usuario, db


# Rota para "/cadastrar/dados" com o método POST
def cadastrar_dados_route(app):
    @app.route('/cadastrar/dados', methods=['POST'])
    def cadastrar_dados():
        data = request.json
        print('data:  ', data)

      
        # Crie um novo objeto Usuario com os dados recebidos e adicione-o ao banco de dados
        novo_usuario = Usuario(nome=data['nome'], email=data['email'], senha=data['senha'])

       


    
        db.session.add(novo_usuario)
        db.session.commit()
        

        response = jsonify({"message": "Cadastro de dados realizado com sucesso"})
        return response, 200
