from flask import Flask, request, jsonify

def create_flask_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Ola!"

    @app.route('/cadastro', methods=['POST'])
    def cadastrar():
        dados = request.get_json()

        nome = dados.get('nome')
        sobrenome = dados.get('sobrenome')
        idade = dados.get('idade')
        pais = dados.get('pais')

        if nome and sobrenome and idade and pais:
            # Aqui você pode processar os dados recebidos como quiser
            # Por exemplo, salvar em um banco de dados, fazer alguma validação, etc.

            return jsonify({'mensagem': 'Dados recebidos com sucesso!'})

        return jsonify({'mensagem': 'Erro ao receber os dados.'}), 400

    @app.route('/listaCadastros', methods=['GET'])
    def listarCadastros():

        return "rota para lista de cadastros"


    @app.route('/consultaCadastro', methods=['GET'])
    def consultaCadastro():
        lista = {1, 2, 3, 4, 5, 6}

        dados = request.get_json()

        inteiro = dados.get('inteiro')

        if inteiro in lista:
            return "Esta na lista"

        return jsonify({'mensagem': 'não esta na lista'}), 400

    return app
