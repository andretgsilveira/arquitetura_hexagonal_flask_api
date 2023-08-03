import json
from services.domain.cliente import Cliente

# Teste da função de representação da classe Cliente
def test_ClienteRepr():
    # Instancia do cliente ficticio
    cliente = Cliente(1, 'João', 'Silva', 30, 'Brasil')

    # Expectativa de resposta
    expected_repr = json.dumps({"id": 1, "nome": "João", "sobrenome": "Silva", "idade": 30, "pais": "Brasil"})

    # Verficação da condição de igualdade entre a representação da classe cliente e a resposta esperada
    assert repr(cliente) == expected_repr

# Teste da função de conversão para json
def test_ClienteToJson():
    # Instancia do cliente ficticio
    cliente = Cliente(2, 'Maria', 'Santos', 25, 'EUA')

    # Expectativa de resposta
    expected_json = json.dumps({"id": 2, "nome": "Maria", "sobrenome": "Santos", "idade": 25, "pais": "EUA"})

    # Verficação da condição de igualdade entre a representação da classe cliente e a resposta esperada
    assert cliente.to_json() == expected_json