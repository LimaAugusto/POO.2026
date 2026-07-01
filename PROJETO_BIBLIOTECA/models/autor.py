from entidade import Entidade


class Autor(Entidade):
    def __init__(self, id, nome, biografia):
        super().__init__(id)
        self.setNome(nome)
        self.setBiografia(biografia)
        
    def getNome(self):
        return self.nome
    
    def getBiografia(self):
        return self.biografia
    

    def setNome(self, nome):
        if isinstance(nome, str): self.nome = nome
        else: raise ValueError("APENAS STRING.")

    def setBiografia(self, biografia):
        if isinstance(biografia, str): self.biografia = biografia
        else: raise ValueError("APENAS STRING.")


    def __str__(self):
        return (
            f"Autor\n"
            f"ID: {self.getId()}\n"
            f"Nome: {self.getNome()}\n"
            f"Biografia: {self.getBiografia()}"
        )

    def to_dict(self):
        return {
            "id": self.getId(),
            "nome": self.getNome(),
            "biografia": self.getBiografia()
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["id"],
            dados["nome"],
            dados["biografia"]
        )