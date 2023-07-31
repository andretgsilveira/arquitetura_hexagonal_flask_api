from abc import ABC, abstractmethod
from typing import List

from servicer.interfaces.cadastro import Cadastro

class CadastroInterface(ABC):
    @abstractmethod
    def getCadastrosList(self) -> List[Cadastro]:
        pass

    @abstractmethod
    def postCasdatro(self, cadastro) -> List[Cadastro]:
        pass