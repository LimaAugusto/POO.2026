from models.dao import DAO
import json

class Produto:
    def __init__(self, id, desc, preco, estoque, id_categoria):
#       ATRIBUTOS DA CLASSE PRODUTO:
        self.setId(id)                      # <-- ID DO PRODUTO
        self.setDesc(desc)                  # <-- ID DA DESCRIÇÃO
        self.setPreco(preco)                # <-- PREÇO DO PRODUTO
        self.setEstoque(estoque)            # <-- QUANTIDADE DO PRODUTO NO ESTOQUE
        self.setId_Categoria(id_categoria)  # <-- ID DA CATEGORIA DAQUELE PRODUTO

    #----- GETTERS -----

    def getId(self):
        return self.id
    
    def getDesc(self):
        return self.desc
    
    def getPreco(self):
        return self.preco
    
    def getEstoque(self):
        return self.estoque
    
    def getId_Categoria(self):
        return self.id_categoria

    #----- GETTERS -----

    #----- SETTERS -----

    def setId(self, id):
        if id < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id = id
    
    def setDesc(self, desc):
        self.desc = desc
    
    def setPreco(self, preco):
        if preco < 0.0: raise ValueError("VALOR INVÁLIDO!")
        self.preco = preco
    
    def setEstoque(self, estoque):
        if estoque < 0: raise ValueError("VALOR INVÁLIDO!")
        self.estoque = estoque
    
    def setId_Categoria(self, id_cat):
        if id_cat < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id_categoria = id_cat

    #----- SETTERS -----

    #----- TO_STRING -----

    def __str__(self):
        return f"PRODUTO_ID: {self.id} - DESCRIÇÃO: {self.desc} - PREÇO: R${self.preco:.2f} - ESTOQUE: {self.estoque} - ID_CATEGORIA: {self.id_categoria}"

    #----- TO_STRING -----
    
    # ----- TO_JSON -----

    def to_json(self):
        return { "id" : self.id, "desc" : self.desc, "preco" : self.preco, "estoque" : self.estoque, "id_categoria" : self.id_categoria }
    
    # ----- TO_JSON -----

    # ----- FROM_JSON -----

    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["desc"], dic["preco"], dic["estoque"], dic["id_categoria"])
    
    # ----- FROM_JSON -----


class ProdutoDAO(DAO):
#   CHAMA OS ATRIBUTOS DO PRODUTO E DEFINE O ARQUIVO A SER USADO PARA LER E ESCREVER
    def __init__(self):
        super().__init__(Produto, "produtos.json")

#   CHAMA O MÉTODO LISTAR DA CLASSE SUPER NO DAO E ORGANIZA POR ID DE PRODUTO
    def listar(self):
        objetos = super().listar()
        objetos.sort(key = lambda x : x.getId())
        return objetos