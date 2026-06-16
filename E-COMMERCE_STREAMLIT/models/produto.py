from models.dao import DAO
import json

class Produto:
    def __init__(self, id, desc, preco, estoque, id_categoria, imagem = None):
#       ATRIBUTOS DA CLASSE PRODUTO:
        self.setId(id)                      # <-- ID DO PRODUTO
        self.setDesc(desc)                  # <-- ID DA DESCRIÇÃO
        self.setPreco(preco)                # <-- PREÇO DO PRODUTO
        self.setEstoque(estoque)            # <-- QUANTIDADE DO PRODUTO NO ESTOQUE
        self.setId_Categoria(id_categoria)  # <-- ID DA CATEGORIA DAQUELE PRODUTO
        self.setImagem(imagem)              # <-- IMAGEM DO PRODUTO (BASE64) OU None SE NÃO HOUVER

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
    
    def getImagem(self):
        return self.imagem

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

    def setImagem(self, imagem):
        # ACEITA None (SEM IMAGEM) OU UMA STRING BASE64 COM A IMAGEM DO PRODUTO
        if imagem is not None and not isinstance(imagem, str):
            raise ValueError("IMAGEM INVÁLIDA!")
        self.imagem = imagem

    #----- SETTERS -----

    #----- TO_STRING -----

    def __str__(self):
        return f"PRODUTO_ID: {self.id} - DESCRIÇÃO: {self.desc} - PREÇO: R${self.preco:.2f} - ESTOQUE: {self.estoque} - ID_CATEGORIA: {self.id_categoria}"

    #----- TO_STRING -----
    
    # ----- TO_JSON -----

    def to_json(self):
        return { "id" : self.id, "desc" : self.desc, "preco" : self.preco, "estoque" : self.estoque, "id_categoria" : self.id_categoria, "imagem" : self.imagem }
    
    # ----- TO_JSON -----

    # ----- FROM_JSON -----

    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["desc"], dic["preco"], dic["estoque"], dic["id_categoria"], dic.get("imagem", None))
        # NOTA: dic.get("imagem", None) GARANTE COMPATIBILIDADE COM REGISTROS ANTIGOS
        # QUE NÃO POSSUEM O CAMPO "imagem" NO JSON
    
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