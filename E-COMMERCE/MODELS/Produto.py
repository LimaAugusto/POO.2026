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

class ProdutoDAO:
    def _init__(self):
        self.produtos = []
    
    def Salvar(self):
        with open(r"POO2026\pythonn\E-COMMERCE\DADOS-JSON\produtos.json", mode = "w") as arq:
            json.dump(self.produtos, arq, default = vars)
    
    def Abrir(self):
        self.produtos =[]
        try:
            with open(r"POO2026\pythonn\E-COMMERCE\DADOS-JSON\produtos.json", mode = "r") as arq:
                produtos_json = json.load(arq)
                for obj in produtos_json:
                    p = Produto(obj["id"], obj["desc"], obj["preco"], obj["estoque"], obj["id_categoria"])
                    self.produtos.append(p)
        except FileNotFoundError:
            self.produtos = []

    def Inserir(self, obj):
        self.Abrir()
        if len(self.produtos) == 0: id = 1
        else: id = (max(self.produtos, key = lambda x: x.id).id) + 1
        obj.id = id
        self.produtos.append(obj)
        self.Salvar()

    def Listar(self):
        self.Abrir()
        return self.produtos
    
    def Listar_Id(self, id_requerido):
        self.Abrir()
        for obj in self.produtos:
            if obj.getId() == id_requerido:
                return obj
        return None

    def Excluir(self, id):
        self.Abrir()
        x = self.Listar_Id(id)
        if x is not None:
            self.produtos.remove(x)
            self.Salvar()
            return True
        else: return False

    def Atualizar(self, id):
        self.Abrir()
        x = self.Listar_Id(id.getId())
        if x is not None:
            x.setDesc(id.getDesc())
            x.setPreco(id.getPreco())
            x.setEstoque(id.getEstoque())
            x.setId_Categoria(id.getId_Categoria())
            self.Salvar()
            return True
        else: return False