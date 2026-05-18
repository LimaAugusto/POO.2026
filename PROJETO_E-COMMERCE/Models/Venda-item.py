import json

class VendaItem :
    def __init__(self, id, qtd, preco, id_venda, id_produto) :
        self.setID(id)#     <--             ID do item da venda;
        self.setQtd(qtd)#      <--          Quantidade do item para na venda;
        self.setPreco(preco)#     <--       Preço do item na venda;
        self.setId_Venda(id_venda)#  <--    ID da venda; 
        self.setId_Produto(id_produto)# <-- ID do produto;

    #---------------SETTERS-------------
    def setID(self, id: int) :
        # Verifica se o valor passado é um inteiro positivo
        if id > 0 : self.id = id
        # Se tentar passar texto, número, etc., o código avisa do erro
        else : raise ValueError("VALOR INVÁLIDO")

    def setQtd(self, qtd: int) :
        # Verifica se o valor passado é um inteiro positivo
        if qtd > 0 : self.qtd = qtd
        # Se tentar passar texto, número, etc., o código avisa do erro
        else : raise ValueError("VALOR INVÁLIDO")

    def setPreco(self, preco: float) :
        # Verifica se o valor passado é um inteiro positivo
        if preco > 0.0 : self.preco = preco
        # Se tentar passar texto, número, etc., o código avisa do erro
        else : raise ValueError("VALOR INVÁLIDO")

    def setId_Venda(self, id: int) :
        # Verifica se o valor passado é um inteiro positivo
        if id > 0 : self.id_venda = id
        # Se tentar passar texto, número, etc., o código avisa do erro
        else : raise ValueError("VALOR INVÁLIDO")

    def setId_Produto(self, id: int) :
        # Verifica se o valor passado é um inteiro positivo
        if id > 0 : self.id_produto = id
        # Se tentar passar texto, número, etc., o código avisa do erro
        else : raise ValueError("VALOR INVÁLIDO")

    def __str__(self) :
        return f"VENDA ITEM: ID-{self.id}, QUANTIDADE-{self.qtd}, PRECO-{self.preco}, ID DA VENDA-{self.id_venda}, ID DO PRODUTO-{self.id_produto}"
    #-----------------------------------

    #--------------GETTERS------------
    def getID(self) :
        return self.id
    def getQtd(self) :
        return self.qtd
    def getPreco(self) :
        return self.preco
    def getId_Venda(self) :
        return self.id_venda
    def getId_Produto(self) :
        return self.id_produto
    #-----------------------------------

class VendaItemDAO :
    def __init__(self) :
        self.vendas_item = []
    def Salvar(self) :
        with open("PROJETO_E-COMMERCE/DADOS-JSON/vendas_item.json", mode = "w") as arq :
            json.dump(self.vendas_item, arq, default = vars)
    def Abrir(self) :
        self.vendas_item = []
        try :
            with open("PROJETO_E-COMMERCE/DADOS-JSON/vendas_item.json", mode = "r") as arq :
                vendas_item_json = json.load(arq)
                for obj in vendas_item_json :
                    c = VendaItem(obj["id"], obj["qtd"], obj["preco"], obj["id_venda"], obj["id_produto"])
                    self.vendas_item.append(c)
        except  FileNotFoundError :
            self.vendas_item = []
    def Inserir(self, obj) :
        self.Abrir()
        self.vendas_item.append(obj)
        self.Salvar()
    def Listar(self) :
        self.Abrir()
        return self.vendas_item
    def Listar_ID(self, v) :
        self.Abrir()
        for id in self.vendas_item :
            if id.getID() == v :
                return id
            else : None
    def Excluir(self, id) :
        self.Abrir()
        x = self.Listar_ID(id)
        if x is not None :
            self.vendas_item.remove(x)
            self.Salvar()
            return True
        else : return False
    def Atualizar(self, id) :
        self.Abrir()
        x = self.Listar_ID(id.getID())
        if x is not None :
            x.setQtd(id.getQtd())
            x.setPreco(id.getPreco())
            x.setId_Venda(id.getId_Venda())
            x.setId_Produto(id.getId_Produto())
            self.Salvar()
            return True
        else : return False