from models.dao import DAO
import json

class Categoria:
    def __init__(self, id, desc):
#   ATRIBUTOS DA CLASSE CATEGORIA:
        self.setId(id)      # <-- ID DA CATEGORIA
        self.setDesc(desc)  # <-- DESCRIÇÃO DA CATEGORIA

    #----- GETTERS -----
    
    def getId(self):
        return self.id
    
    def getDesc(self):
        return self.desc
    
    #----- GETTERS -----

    #----- SETTERS -----

    def setId(self, id):
        if id < 0: raise ValueError("VALOR INVÁLIDO")
        self.id = id
    def setDesc(self, desc):
        self.desc = desc

    #----- SETTERS -----

    #----- TO_STRING -----

    def __str__(self):
        return f"|CATEGORIA_ID: {self.id} | DESCRIÇÃO: {self.desc}|"

    #----- TO_STRING -----

class CategoriaDAO(DAO):
#   CHAMA OS ATRIBUTOS DA CATEGORIA E DEFINE O ARQUIVO A SER USADO PARA LER E ESCREVER
    def __init__(self):
        super().__init__(Categoria, "categorias.json")

#   CHAMA O MÉTODO LISTAR DA CLASSE SUPER NO DAO E ORGANIZA POR ID DE CATEGORIA
    def listar(self):
        objetos = super().listar()
        objetos.sort(key = lambda x : x.getId())
        return objetos