from dataclasses import dataclass


@dataclass(init=True)
class Cadastro:
    nome: str
    sobrenome: str
    idade: int
    pais: str
