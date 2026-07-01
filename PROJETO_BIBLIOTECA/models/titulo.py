from entidade import Entidade


class Titulo(Entidade):

    def __init__(self, id, nome, ano, isbn):
        super().__init__(id)
        self.setNome(nome)
        self.setAno(ano)
        self.setIsbn(isbn)

    def getNome(self):
        return self.nome
    
    def getAno(self):
        return self.ano
    
    def getIsbn(self):
        return self.isbn
    
    def setAno(self, ano):
        self.ano = ano

    def setIsbn(self, isbn):
        self.isbn = isbn

    def setNome(self, nome):
        self.nome = nome


    def __str__(self):
        return (
            f"Título\n"
            f"ID: {self.getId()}\n"
            f"Nome: {self.getNome()}\n"
            f"Ano: {self.getAno()}\n"
            f"ISBN: {self.getIsbn()}"
        )

    def to_dict(self):
        return {
            "id": self.getId(),
            "nome": self.getNome(),
            "ano": self.getAno(),
            "isbn": self.getIsbn()
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["id"],
            dados["nome"],
            dados["ano"],
            dados["isbn"]
        )