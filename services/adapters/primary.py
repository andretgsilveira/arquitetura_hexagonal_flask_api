from flask import Flask, request
from services.ports.useServices import clientServices

cliente = clientServices()


def create_flask_app():
    app = Flask(__name__)

    @app.route('/cadastro', methods=['POST'])
    def cadastro():
        dados = request.get_json()

        nome = dados.get('nome')
        sobrenome = dados.get('sobrenome')
        idade = dados.get('idade')
        pais = dados.get('pais')

        response = cliente.cadastrar(nome, sobrenome, idade, pais)

        return response

    @app.route('/consultaCadastro/<int:id>', methods=['GET'])
    def getByID(id):
        return cliente.getByID(id)

    @app.route('/listaCadastros', methods=['GET'])
    def getList():
        return cliente.getList()

    @app.route('/modificar/<int:id>', methods=['PATCH'])
    def modificaByID(id):
        dados = request.get_json()
        return cliente.modificaByID(dados, id)

    @app.route('/delete/<int:id>', methods=['DELETE'])
    def deletaByID(id):
        return cliente.deletaByID(id)

    return app
