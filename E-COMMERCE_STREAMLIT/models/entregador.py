from models.dao import DAO

class Entregador:
    def __init__(self, id, nome, email, fone, senha):
        self.setId(id)
        self.setNome(nome)
        self.setEmail(email)
        self.setFone(fone)
        self.setSenha(senha)

    #----- GETTERS -----

    def getId(self):
        return self.id

    def getNome(self):
        return self.nome

    def getEmail(self):
        return self.email

    def getFone(self):
        return self.fone

    def getSenha(self):
        return self.senha

    #----- GETTERS -----

    #----- SETTERS -----

    def setId(self, id):
        if id < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id = id

    def setNome(self, nome):
        if nome == "": raise ValueError("NOME INVÁLIDO!")
        self.nome = nome

    def setEmail(self, email):
        if email == "": raise ValueError("E-MAIL INVÁLIDO!")
        self.email = email

    def setFone(self, fone):
        self.fone = fone

    def setSenha(self, senha):
        if senha == "": raise ValueError("SENHA INVÁLIDA!")
        self.senha = senha

    #----- SETTERS -----

    #----- TO_STRING -----

    def __str__(self):
        return f"ENTREGADOR_ID: {self.id} - NOME: {self.nome} - EMAIL: {self.email}"

    #----- TO_STRING -----

    # ----- TO_JSON -----

    def to_json(self):
        return { "id": self.id, "nome": self.nome, "email": self.email, "fone": self.fone, "senha": self.senha }

    # ----- TO_JSON -----

    # ----- FROM_JSON -----

    @staticmethod
    def from_json(dic):
        return Entregador(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])

    # ----- FROM_JSON -----


class EntregadorDAO(DAO):
    def __init__(self):
        super().__init__(Entregador, "entregadores.json")

    def listar(self):
        objetos = super().listar()
        objetos.sort(key = lambda x: x.getNome())
        return objetos
