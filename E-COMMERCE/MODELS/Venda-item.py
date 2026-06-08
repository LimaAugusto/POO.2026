import json

class VendaItem:
    def __init__(self, id, qtd, preco, id_venda, id_produto):
        self.setId(id)
        self.setQtd(qtd)
        self.setPreco(preco)
        self.setId_Venda(id_venda)
        self.setId_Produto(id_produto)

    #----- GETTERS -----

    def getId(self):
        return self.id

    def getQtd(self):
        return self.qtd
    
    def getPreco(self):
        return self.preco
    
    def getId_Venda(self):
        return self.id_venda
    
    def getId_Produto(self):
        return self.id_produto

    #----- GETTERS -----

    #----- SETTERS -----

    def setId(self, id):
        if id < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id = id

    def setQtd(self, qtd):
        if qtd < 0: raise ValueError("VALOR INVÁLIDO!")
        self.qtd = qtd

    def setPreco(self, preco):
        if preco < 0.0: raise ValueError("VALOR INVÁLIDO!")
        self.preco = preco

    def setId_Venda(self, id_venda):
        if id_venda < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id_venda = id_venda

    def setId_Produto(self, id_produto):
        if id_produto < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id_produto = id_produto

    #----- SETTERS -----

    #----- TO_STRING -----

    def __str__(self):
        return f"|VENDA-ITEM_ID: {self.id} | QUANTIDADE: {self.qtd} | PREÇO: R${self.preco:.2f} | ID_VENDA: {self.id_venda} | ID_PRODUTO: {self.id_produto}|"
    
    #----- TO_STRING -----

class VendaItemDAO:
    def __init__(self):
        self.vendas_item = []
    
    def Salvar(self):
        with open(r"POO2026\pythonn\E-COMMERCE\DADOS-JSON\vendas_item.json", mode = "w") as arq:
            json.dump(self.vendas_item, arq, default = vars)
    
    def Abrir(self):
        self.vendas_item = []
        try:
            with open(r"POO2026\pythonn\E-COMMERCE\DADOS-JSON\vendas_item.json", mode = "r") as arq:
                v_item_json = json.load(arq)
                for obj in v_item_json:
                    vi = VendaItem(obj["id"], obj["qtd"], obj["preco"], obj["id_venda"], obj["id_produto"])
                    self.vendas_item.append(vi)
        except FileNotFoundError:
            self.vendas_item = []
    
    def Inserir(self, obj):
        self.Abrir()
        self.vendas_item.append(obj)
        self.Salvar()

    def Listar(self):
        self.Abrir()
        return self.vendas_item
    
    def Listar_Id(self, id):
        self.Abrir()
        for obj in self.vendas_item:
            if obj.getId() == id:
                return id
        return None
    
    def Excluir(self, id_requisitado):
        self.Abrir()
        x = self.Listar_Id(id_requisitado)
        if x is not None:
            self.vendas_item.remove(x)
            self.Salvar()
            return True
        return False
    
    def Atualizar(self, id):
        self.Abrir()
        x = self.Listar_Id(id.getId())
        if x is not None:
            x.setQtd(id.getQtd())
            x.setPreco(id.getPreco())
            x.setId_Venda(id.getId_Venda())
            x.setId_Produto(id.getId_Produto())
            return True
        return False