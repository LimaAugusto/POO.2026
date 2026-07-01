from abc import ABC, abstractcmethod

class Entidade(ABC):
    def __init__(self, id=None):
        self.setId(id) = id

    def getId(self):
        return self.id
    
    def setId(self, id):
        if id >= 0 : self.id = id
        else : raise ValueError("VALOR INVÁLIDO")

    @abstractcmethod
    def to_dict(self):
        pass

    @classmethod
    @abstractcmethod
    def from_dict(cls, dados):
        pass