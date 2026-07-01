from entidade import Entidade


class Prateleira(Entidade):

    def __init__(self, id, codigo):
        super().__init__(id)
        self.setCodigo(codigo)

    def getCodigo(self):
        return self.codigo

    def setCodigo(self, codigo):
        self.codigo = codigo

    def __str__(self):
        return (
            f"Prateleira\n"
            f"ID: {self.getId()}\n"
            f"Código: {self.getCodigo()}"
        )

    def to_dict(self):
        return {
            "id": self.getId(),
            "codigo": self.getCodigo()
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["id"],
            dados["codigo"]
        )