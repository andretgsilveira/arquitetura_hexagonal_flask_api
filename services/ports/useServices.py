import itertools
import json
from services.ports.cadastroInterface import CadastroInterface
from services.domain.cliente import Cliente

# Implementação da classe Cadastro Interface.
# Esta implementa as funções responsaveis por manipular o cadastro de um cliente
# desde sua criação, modificação e exclusão.
class clientServices(CadastroInterface):

    # Variavel que armazena todos os clientes
    clientes = []

    # Gerador de ID incremental
    idIncr = itertools.count()

    # Função responsavel por efetuar o cadastro do cliente.
    def cadastrar(self, nome, sobrenome, idade, pais):

        # Teste para verificar se todos os dados são diferentes de nulo.
        if nome and sobrenome and idade and pais:

            # Criação do proximo ID
            id = next(self.idIncr)

            # Criação do cliente.
            cliente = Cliente(id, nome, sobrenome, idade, pais)

            # Inclusão do cliente a lista clientes.
            clientServices.clientes.append(cliente)

            # retorna uma mensagem positiva caso o cadastro tenha sido efetuado.
            return {'mensagem': 'Dados recebidos com sucesso!'}

        # retorna uma mensagem negativa caso o cadastro não tenha sido efetuado.
        return {'mensagem': 'Erro ao receber os dados.'}

    # Função responsavel por consultar um ID especifico
    def getByID(self, id):
        # Laço para verificar se na lista de clientes existe um cliente com o ID especificado.
        for cliente in self.clientes:
            if cliente.id == id:

                # Se o cliente for localizado, retorna o cliente no formato dicionario
                return cliente.to_json()

        # Caso o cliente não tenha sido localizado retorna uma mensagem negativa.
        return {'mensagem': 'ID não localizado'}

    # Função responsavel por devolver a lista de clientes cadastrados
    def getList(self):

        jsonClientes = []
        # Formação da lista no estrutura JSON
        for cliente in self.clientes:
            jsonClientes.append(
                {
                    "id": cliente.id,
                    "nome": cliente.nome,
                    "sobrenome": cliente.sobrenome,
                    "idade": cliente.idade,
                    "pais": cliente.pais
                }
            )
        # Retorna a lista de clientes
        return json.dumps(jsonClientes)

    # Função responsavel por executar modificações nos clientes.
    # Recebe como parametros um objeto json e um ID para identificar qual usuario será modificado
    def modificaByID(self, dados, id):

        # Localiza a posição do cliente na lista de clientes
        for i, objeto in enumerate(self.clientes):
            if objeto.id == id:

                # Efetua a modificação conforme os dados recebidos
                for key, value in dados.items():
                    objeto.__dict__[key] = value
                break
        # Devolve o cliente modificado
        return self.getByID(id)

    # Função responsavel por excluir o cliente por ID
    def deletaByID(self, id):
        # Variavel para armazenar a posição do cliente que sera excluido
        index_para_deletar = None

        # Laço para localizar o cliente que sera excluido procurando por ID
        for i, objeto in enumerate(self.clientes):
            if objeto.id == id:
                index_para_deletar = i
                break

        # Validação para verificar se o cliente foi localizado
        if index_para_deletar is not None:

            # Remoção do cliente da lista
            self.clientes.pop(index_para_deletar)

            # Devolução de uma mensagem de sucesso
            return {'mensagem': "Cliente com ID {} deletado com sucesso.".format(id)}
        else:

            # Caso o Id não tenha sido localizado devolve uma mensagem negativa
            return {'mensagem': "Cliente com ID {} não encontrado.".format(id)}


    def limparLista(self):
        self.clientes = []