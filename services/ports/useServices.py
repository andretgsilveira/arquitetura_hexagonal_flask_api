import itertools

from flask import jsonify
from services.ports.cadastroInterface import CadastroInterface
from services.domain.cliente import Cliente

class clientServices(CadastroInterface):
    clientes = []
    idIncr = itertools.count()

    def cadastrar(self, nome, sobrenome, idade, pais):

        id = next(self.idIncr)

        if nome and sobrenome and idade and pais:
            cliente = Cliente(id, nome, sobrenome, idade, pais)
            clientServices.clientes.append(cliente)

            # return jsonify({'mensagem': 'Dados recebidos com sucesso!'})
            return {'mensagem': 'Dados recebidos com sucesso!'}

        # return jsonify({'mensagem': 'Erro ao receber os dados.'}), 400
        return {'mensagem': 'Erro ao receber os dados.'}

    def getByID(self, id):
        for cliente in self.clientes:
            if cliente.id == id:
                return jsonify(cliente.__dict__)
        return None


    def getList(self):

        json = []
        for cliente in self.clientes:
            json.append(
                {
                    "id": cliente.id,
                    "nome": cliente.nome,
                    "sobrenome": cliente.sobrenome,
                    "idade": cliente.idade,
                    "pais": cliente.pais
                }
            )

        return jsonify(json)

    def modificaByID(self, dados, id):
        for i, objeto in enumerate(self.clientes):
            if objeto.id == id:
                for key, value in dados.items():
                    objeto.__dict__[key] = value
                break
        return self.getByID(id)

    def deletaByID(self, id):
        index_para_deletar = None
        for i, objeto in enumerate(self.clientes):
            if objeto.id == id:
                index_para_deletar = i
                break

        if index_para_deletar is not None:
            self.clientes.pop(index_para_deletar)
            return "Cliente com ID {} deletado com sucesso.".format(id)
        else:
            return "Cliente com ID {} não encontrado.".format(id)

# test = clientServices()
# test.cadastrar("João", "da Silva", 30, "Brasil")
# test.cadastrar("João", "da Silva", 30, "Brasil")
# test.modificaByID({'nome':'klebe'}, 0)
# print(test.getByID(0))