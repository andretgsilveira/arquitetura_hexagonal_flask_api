from services.ports.useServices import clientServices
import json

class TestClientServices:

    def setup_method(self):
        # Criação do objeto clientServices
        self.client_service = clientServices()


    def test_cadastrar_cliente(self):
        # Testando o cadastro de um cliente válido
        result = self.client_service.cadastrar("João", "Silva", 30, "Brasil")

        # Verficação da condição de igualdade entre a representação da classe cliente e a resposta esperada
        assert result == {'mensagem': 'Dados recebidos com sucesso!'}

        # Testando o cadastro com dados faltando
        result = self.client_service.cadastrar("", "Silva", 30, "Brasil")

        # Verficação da condição de igualdade entre a representação da classe cliente e a resposta esperada
        assert result == {'mensagem': 'Erro ao receber os dados.'}


    def test_get_by_id(self):

        # Cadastro de um cliente para testar a busca pelo ID
        self.client_service.cadastrar("Ana", "Santos", 25, "Brasil")

        # criação da variavel cliente como objeto
        cliente = json.loads(self.client_service.getByID(2))

        # Verficação da condição de igualdade entre a representação da classe cliente e a resposta esperada
        assert cliente is not None
        assert cliente['nome'] == 'Ana'
        assert cliente['sobrenome'] == 'Santos'
        assert cliente['idade'] == 25
        assert cliente['pais'] == 'Brasil'

        # ======================================== #

        # Testando busca por um ID inexistente
        cliente = self.client_service.getByID(999)

        # Expectativa de resposta
        expected_repr = {'mensagem': 'ID não localizado'}

        # Verficação da condição de igualdade entre a representação da classe cliente e a resposta esperada
        assert cliente == expected_repr



    def test_get_list(self):
        # Cadastro de dois clientes para testar a listagem
        self.client_service.cadastrar("Maria", "Souza", 28, "Brasil")
        self.client_service.cadastrar("Carlos", "Ferreira", 35, "EUA")

        # Criação do objeto com a lista
        clientes_list = json.loads(self.client_service.getList())

        # Verifica se a lista não esta vazia
        assert clientes_list is not None

        # Verifica se a lista tem o mesmo tamanho esperado
        assert len(clientes_list) == 5

        # Verificando os dados de um dos clientes na lista
        cliente = clientes_list[3]
        assert cliente['nome'] == 'Maria'
        assert cliente['sobrenome'] == 'Souza'
        assert cliente['idade'] == 28
        assert cliente['pais'] == 'Brasil'



    def test_modifica_by_id(self):
        # Primeiro, cadastrar um cliente para testar a modificação
        self.client_service.cadastrar("Rafael", "Melo", 22, "Brasil")

        # Modificando os dados do cliente
        dados_modificados = {"nome": "Raphael", "idade": 23}

        # Criação do objeto modificado
        cliente_modificado = json.loads(self.client_service.modificaByID(dados_modificados, 4))

        # Verficação da condição de igualdade entre a representação da classe cliente e a resposta esperada
        assert cliente_modificado is not None
        assert cliente_modificado['nome'] == 'Raphael'
        assert cliente_modificado['idade'] == 23

        # Testando modificação em um ID inexistente
        dados_modificados = {"nome": "Pedro"}

        # Tentativa de criar um cliente modificado com ID incorreto
        cliente_modificado = self.client_service.modificaByID(dados_modificados, 999)

        # Expectativa de resposta
        expected_repr = {'mensagem': 'ID não localizado'}

        # Verficação da condição de igualdade entre a representação da classe cliente e a resposta esperada
        assert cliente_modificado == expected_repr


    def test_deleta_by_id(self):
        # Deletando o primeiro cliente cadastrado
        result = self.client_service.deletaByID(0)
        assert result == {'mensagem': 'Cliente com ID 0 deletado com sucesso.'}

        # Tentando deletar um ID inexistente
        result = self.client_service.deletaByID(999)
        assert result == {'mensagem': 'Cliente com ID 999 não encontrado.'}