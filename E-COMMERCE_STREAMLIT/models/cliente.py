from models.dao import DAO
import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
    #   ATRIBUTOS DA CLASSE CLIENTE:
        self.setId(id)       # <-- ID DO CLIENTE
        self.setNome(nome)   # <-- NOME DO CLIENTE
        self.setEmail(email) # <-- EMAIL DO CLIENTE
        self.setFone(fone)   # <-- TELEFONE DO CLIENTE
        self.setSenha(senha) # <-- SENHA DO CLIENTE
    
    # ----- GETTERS -----

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
    
    # ----- GETTERS -----

    # ----- SETTERS -----

    def setId(self, id):
        if id < 0: raise ValueError("ID INVÁLIDO!")
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setEmail(self, email):
        self.email = email

    def setFone(self, fone):
        self.fone = fone

    def setSenha(self, senha):
        self.senha = senha
        
    # ----- SETTERS -----

    #----- TO_STRING -----

    def __str__(self):
        return f"|CLIENTE_ID: {self.id} | NOME: {self.nome} | EMAIL: {self.email} | FONE: {self.fone} | SENHA: {self.senha}|"

    #----- TO_STRING -----


class ClienteDAO(DAO):
#   CHAMA OS ATRIBUTOS DO CLIENTE E DEFINE O ARQUIVO A SER USADO PARA LER E ESCREVER
    def __init__(self):
        super().__init__(Cliente, "clientes.json")

#   CHAMA O MÉTODO LISTAR DA CLASSE SUPER NO DAO E ORGANIZA POR NOME DE CLIENTE
    def listar(self):
        objetos = super().listar()
        objetos.sort(key = lambda x : x.getNome())
        return objetos
 