from abc import ABC, abstractmethod

class CadastroInterface(ABC):
    @abstractmethod
    def cadastrar(self, id, nome, sobrenome, idade, pais):
        pass

    @abstractmethod
    def getByID(self, id):
        pass

    @abstractmethod
    def getList(self):
        pass

    @abstractmethod
    def modificaByID(self):
        pass

    @abstractmethod
    def deletaByID(self, id):
        pass