import json


class Cliente():
    def __init__(self, id, nome, sobrenome, idade, pais):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.pais = pais

    def __repr__(self):
        return json.dumps({"id": self.id, "nome": self.nome, "sobrenome": self.sobrenome, "idade": self.idade, "pais": self.pais})

    def to_json(self):
        return json.dumps(self.__dict__)

