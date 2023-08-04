# API Flask - Arquitetura Hexagonal

Este  projeto é uma API criada em Flask que utiliza Docker e Docker Compose para facilitar o desenvolvimento e implantação da aplicação.

## Requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados em sua máquina:

- Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
- Docker Compose: [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

## Configuração

1. Clone este repositório para o seu ambiente de desenvolvimento.
   ```
   git clone https://github.com/andretgsilveira/arquitetura_hexagonal_flask_api.git
   ```

2. Crie um ambiente virtual (opcional) e instale as dependências do Flask.
   ```
   python -m venv venv
   venv\Scripts\activate no Windows
   pip install -r services\requirements.txt
   ```

## Executando a API com Docker Compose

Agora, vamos iniciar o ambiente da API utilizando o Docker Compose:

1. Abra um terminal na pasta do projeto e execute o seguinte comando:
   ```
   docker-compose -f .\docker-compose.yml up --build    
   ```

2. O Docker Compose irá criar os containers e executar a API na porta especificada (por padrão, será a porta 5000).

## Utilização da API

Após a API estar em execução, você pode acessar os endpoints utilizando qualquer cliente HTTP ou ferramenta de teste de API, como o Postman.

Exemplo de endpoint:

```
GET http://localhost:5000/api
```

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte maneira:

```
arquitetura_hexagonal_flask_api/
  ├── services/
  │   ├── adapters/
  │   │   └── app.py
  │   ├── domain/
  │   │   └── cliente.py
  │   └── ports/
  │       ├── cadastroInterface.py
  │       └── useServices.py
  ├── test/
  │   ├── teste_app.py
  │   ├── test_cliente.py
  │   └── test_useService.py
  ├── docker-compose.yml
  ├── Dockerfile
  ├── app.log
  ├── main.py
  ├── .gitignore
  ├── requirements.txt
  └── README.md
```


## Considerações Finais

Este é apenas um exemplo básico de como criar uma API Flask utilizando Docker e Docker Compose. Sinta-se à vontade para modificar e expandir o projeto conforme suas necessidades.
