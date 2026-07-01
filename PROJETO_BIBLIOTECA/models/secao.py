from entidade import Entidade


class Secao(Entidade):

    def __init__(self, id, nome):
        super().__init__(id)
        self.setNome(nome)

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def __str__(self):
        return (
            f"Seção\n"
            f"ID: {self.getId()}\n"
            f"Nome: {self.getNome()}"
        )

    def to_dict(self):
        return {
            "id": self.getId(),
            "nome": self.getNome()
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["id"],
            dados["nome"]
        )