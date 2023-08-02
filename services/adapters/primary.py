from flask import Flask, request
from services.ports.useServices import clientServices
cliente = clientServices()



def create_flask_app(logger):
    app = Flask(__name__)

    @app.route('/cadastro', methods=['POST'])
    def cadastro():
        dados = request.get_json()
        log_info = {
            "method": request.method,
            "path": request.path,
            "json": request.json
        }
        logger.debug(f"Cadastrar usuário - {log_info}")

        nome = dados.get('nome')
        sobrenome = dados.get('sobrenome')
        idade = dados.get('idade')
        pais = dados.get('pais')

        response = cliente.cadastrar(nome, sobrenome, idade, pais)

        return response

    @app.route('/consultaCadastro/<int:id>', methods=['GET'])
    def getByID(id):
        log_info = {
            "method": request.method,
            "path": request.path
        }
        logger.debug(f"Consultar usuario por id. - {log_info}")
        return cliente.getByID(id)

    @app.route('/listaCadastros', methods=['GET'])
    def getList():
        log_info = {
            "method": request.method,
            "path": request.path,
        }
        logger.debug(f"Consultar lista de usuários. - {log_info}")
        return cliente.getList()

    @app.route('/modificar/<int:id>', methods=['PATCH'])
    def modificaByID(id):
        log_info = {
            "method": request.method,
            "path": request.path,
            "json": request.json
        }
        logger.debug(f"Modificar usuário por id - {log_info}")
        dados = request.get_json()
        return cliente.modificaByID(dados, id)

    @app.route('/delete/<int:id>', methods=['DELETE'])
    def deletaByID(id):
        log_info = {
            "method": request.method,
            "path": request.path
        }
        logger.debug(f"Deletar usuário por id. - {log_info}")
        return cliente.deletaByID(id)

    @app.errorhandler(404)
    def not_found_error(error):
        logger.debug(f"Rota não encontrada. Path: - {request.path}")
        return "Página não encontrada"

    @app.errorhandler(405)
    def not_found_error(error):
        logger.debug(f"Metodo incorreto. Method: - {request.method}" )
        return "Metodo incorreto"

    return app
