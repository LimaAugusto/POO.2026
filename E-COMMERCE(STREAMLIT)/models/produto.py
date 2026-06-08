from models.dao import DAO
import json

class Produto:
    def __init__(self, id, desc, preco, estoque, id_categoria):
        self.setId(id)
        self.setDesc(desc)
        self.setPreco(preco)
        self.setEstoque(estoque)
        self.setId_Categoria(id_categoria)

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
        return f"|PRODUTO_ID: {self.id} | DESCRIÇÃO: {self.desc} | PREÇO: R${self.preco:.2f} | ESTOQUE: {self.estoque} | ID_CATEGORIA: {self.id_categoria}|"

    #----- TO_STRING -----

class ProdutoDAO(DAO):
    def __init__(self):
        super().__init__(Produto, "produtos.json")

    def listar(self):
        objetos = super().listar()
        objetos.sort(key = lambda x : x.getId())
        return objetos