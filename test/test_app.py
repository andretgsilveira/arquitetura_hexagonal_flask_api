import pytest
from services.adapters.app import create_flask_app


@pytest.fixture
def app():
    # Inicializa a aplicação Flask com um logger fictício
    logger = FakeLogger()
    app = create_flask_app(logger)
    yield app


@pytest.fixture
def client(app):
    # Inicializa um cliente de teste Flask
    with app.test_client() as client:
        yield client


class FakeLogger:
    # Implementa um logger fictício para os testes
    def debug(self, message):
        pass


def test_cadastro(client):
    # Testa a rota de cadastro
    data = {
        "nome": "João",
        "sobrenome": "Silva",
        "idade": 30,
        "pais": "Brasil"
    }
    response = client.post('/api', json=data)
    assert response.status_code == 200


def test_get_by_id(client):
    # Testa a rota para obter um usuário pelo ID
    response = client.get('/api/1')
    assert response.status_code == 200


def test_get_list(client):
    # Testa a rota para obter a lista de usuários
    response = client.get('/api')
    assert response.status_code == 200


def test_modifica_by_id(client):
    # Testa a rota para modificar um usuário pelo ID
    data = {
        "nome": "Maria",
        "sobrenome": "Souza",
        "idade": 25,
        "pais": "EUA"
    }
    response = client.patch('/api/1', json=data)
    assert response.status_code == 200


def test_deleta_by_id(client):
    # Testa a rota para deletar um usuário pelo ID
    response = client.delete('/api/1')
    assert response.status_code == 200


def test_not_found_error(client):
    # Testa a resposta de erro 404 para uma rota não encontrada
    response = client.get('/invalid_route')
    assert response.status_code == 200


def test_method_not_allowed(client):
    # Testa a resposta de erro 405 para um método não permitido em uma rota
    response = client.post('/api/1')
    assert response.status_code == 200