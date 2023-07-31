import requests

url = 'http://localhost:5000/cadastro'

dados = {
    "nome": "João",
    "sobrenome": "da Silva",
    "idade": 30,
    "pais": "Brasil"
}

response = requests.post(url, json=dados)

if response.status_code == 200:
    print('Dados enviados com sucesso!')
else:
    print('Erro ao enviar os dados:', response.json())