from flask import Flask, request
from services.ports.useServices import clientServices

# Função responsavel por criar o app flask
def create_flask_app(logger):

    # Instancia do objeto Flask
    app = Flask(__name__)

    # Instancia do objeto clientService
    cliente = clientServices()

    # Rota de cadastro
    @app.route('/api', methods=['POST'])
    # Função responsavel pela captura das informações enviadas pela requisição e inclusão em nossa 'base'
    def cadastro():
        # Captura dos dados JSON encaminhadas pela requisição
        dados = request.get_json()

        # Criação da estrutura de log, capturando as informações que vem na requisição
        log_info = {
            "method": request.method,
            "path": request.path,
            "json": request.json
        }

        # Escrita no arquivo de log
        logger.debug(f"Cadastrar usuario - {log_info}")

        # dados capturados na requisição
        nome = dados.get('nome')
        sobrenome = dados.get('sobrenome')
        idade = dados.get('idade')
        pais = dados.get('pais')

        # Inclusão do cliente na 'base', com captura da resposta
        response = cliente.cadastrar(nome, sobrenome, idade, pais)

        # Retorno da resposta obtida
        return response

    # Rota para consultar usuario por ID
    @app.route('/api/<int:id>', methods=['GET'])
    def getByID(id):
        # Estrutura do log a ser registrado
        log_info = {
            "method": request.method,
            "path": request.path
        }
        # Escrita no arquivo de log
        logger.debug(f"Consultar usuario por id. - {log_info}")

        # Retorno da função que busca o cliente por ID
        return cliente.getByID(id)

    # Rota para busca de todos os clientes cadastrados
    @app.route('/api', methods=['GET'])
    def getList():
        # Estrutura do log a ser registrado
        log_info = {
            "method": request.method,
            "path": request.path,
        }
        # Escrita no arquivo de log
        logger.debug(f"Consultar lista de usuarios. - {log_info}")

        # Retorno da função que busca todos os clientes cadastrados
        return cliente.getList()

    # Rota de modificação do usuario por ID
    @app.route('/api/<int:id>', methods=['PATCH'])
    def modificaByID(id):
        # Estrutura do log a ser registrado
        log_info = {
            "method": request.method,
            "path": request.path,
            "json": request.json
        }
        # Escrita no arquivo de log
        logger.debug(f"Modificar usuario por id - {log_info}")

        # Captura doas informações enviadas na requisição no formato JSON
        dados = request.get_json()

        # Retorno da execução da mudança do cliente
        return cliente.modificaByID(dados, id)

    # Rota para exclusão do cliente por ID
    @app.route('/api/<int:id>', methods=['DELETE'])
    def deletaByID(id):
        # Estrutura do log a ser registrado
        log_info = {
            "method": request.method,
            "path": request.path
        }
        # Escrita no arquivo de log
        logger.debug(f"Deletar usuario por id. - {log_info}")

        # Retorno da função responsavel por excluir o cliente
        return cliente.deletaByID(id)

    # Rota para tratamento de erro 404. Tentativas de utilizar rotas não criadas.
    @app.errorhandler(404)
    def not_found_error(error):
        # Escrita no arquivo de log
        logger.debug(f"Rota não encontrada. Path: - {request.path}")

        # Retorno da mensagem de pagina não localizada
        return {'mensagem': "Pagina não encontrada"}

    # Rota para tratamento de erro 405. Utilização de metodo indevido.
    @app.errorhandler(405)
    def not_found_error(error):
        logger.debug(f"Metodo incorreto. Method: - {request.method}")
        return {'mensagem': "Metodo incorreto"}

    return app
