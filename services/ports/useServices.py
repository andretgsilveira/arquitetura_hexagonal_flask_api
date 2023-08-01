import uuid
from flask import  jsonify
from services.ports.cadastroInterface import CadastroInterface
from services.domain.cliente import Cliente

class clientServices(CadastroInterface):
    clientes = []

    def cadastrar(self, nome, sobrenome, idade, pais):

        id = str(uuid.uuid4())

        if nome and sobrenome and idade and pais:
            cliente = Cliente(id, nome, sobrenome, idade, pais)
            clientServices.clientes.append(cliente)

            return jsonify({'mensagem': 'Dados recebidos com sucesso!'})

        return jsonify({'mensagem': 'Erro ao receber os dados.'}), 400

    @classmethod
    def getByID(cls, id):
        for cliente in cls.clientes:
            if cliente["id"] == id:
                return cliente
        return None

    @classmethod
    def getList(cls):
        return cls.clientes

    @classmethod
    def modificaByID(cls, id):
        pass

    @classmethod
    def deletaByID(cls, id):
        pass