# flask-react-chat-login/backend/routes/routeCadastro.py

from flask import request, jsonify
from models.usuario import Usuario, db


# Rota para "/cadastrar/dados" com o método POST
def cadastrar_dados_route(app):
    @app.route('/cadastrar/dados', methods=['POST'])
    def cadastrar_dados():
        if request.method == 'POST':
            data = request.json
            nome = data.get('nome')
            email = data.get('email')
            senha = data.get('senha')


            # Crie um novo objeto Usuario com os dados recebidos e adicione-o ao banco de dados
            novo_usuario = Usuario(nome, email, senha)
        
            db.session.add(novo_usuario)
            db.session.commit()

            user_info = {
                "nome": nome, 
                "email": email, 
                "senha": senha, 
            }  # Substitua isso pelos detalhes reais do usuário

            print(
                "\n" "Cadastro bem-sucedido! Usuário: "
                "\n" f"Nome: {user_info['nome']}"
                "\n" f"Email: {user_info['email']}"
                "\n" f"Senha: {user_info['senha']}"
                "\n")  # Exibe no console
            

            response = jsonify({"\n message": "Cadastro de dados realizado com sucesso"})
            return response, 200
    
        return jsonify({"\n error": "Credenciais inválidas"}), 401