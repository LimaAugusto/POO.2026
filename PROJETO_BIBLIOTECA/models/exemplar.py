from entidade import Entidade


class Exemplar(Entidade):

    def __init__(self, id, disponivel=True):
        super().__init__(id)
        self.setDisponivel(disponivel)

    def getDisponivel(self):
        return self.disponivel

    def setDisponivel(self, disponivel):
        self.disponivel = disponivel

    def __str__(self):
        return (
            f"Exemplar\n"
            f"ID: {self.getId()}\n"
            f"Disponível: {self.getDisponivel()}"
        )

    def to_dict(self):
        return {
            "id": self.getId(),
            "disponivel": self.getDisponivel()
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["id"],
            dados["disponivel"]
        )