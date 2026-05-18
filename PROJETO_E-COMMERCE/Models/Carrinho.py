import json

class Carrinho:
    def __init__(self, id, desc, quantidade, id_produto) :
        self.setID(id)#              <--            ID do carrinho;
        self.setDesc(desc)#             <--         Descrição do carrinho;
        self.setQuantidade(quantidade)#    <--      Quantidade do carrinho;
        self.setIdProduto(id_produto)#        <--   ID do produto do carrinho;

    #---------------SETTERS-------------
    def setID(self, id) :
        if id >= 0 : self.id = id
        else : raise ValueError("VALOR INVÁLIDO")
    def setDesc(self, desc) :
        self.desc = desc
    def setQuantidade(self, qtd) :
        if qtd > 0 : self.quantidade = qtd
        else: raise ValueError("VALOR INVÁLIDO")
    def setIdProduto(self, id) :
        if id >= 0 : self.id_produto = id
        else : raise ValueError("VALOR INVÁLIDO")
    def __str__(self) :
        return f"CARRINHO: ID-{self.id}, DESCRIÇÃO-{self.desc}, QUANTIDADE--{self.quantidade}, ID_PRODUTO--{self.id_produto}"

    #--------------GETTERS------------
    def getID(self) :
        return self.id
    def getDesc(self) :
        return self.desc
    def getQuantidade(self) :
        return self.quantidade
    def getIdProduto(self) :
        return self.id_produto

class CarrinhoDAO :
    def __init__(self) :
        self.carrinho = []
        self.produtos_comprados = []

    def Salvar(self) :
        with open("PROJETO_E-COMMERCE/DADOS-JSON/carrinho.json", mode = "w") as arq :
            json.dump({"carrinho": self.carrinho, "comprados": self.produtos_comprados}, arq, default = vars)

    def Abrir(self) :
        self.carrinho = []
        self.produtos_comprados = []
        try :
            with open("PROJETO_E-COMMERCE/DADOS-JSON//carrinho.json", mode = "r") as arq :
                dados_json = json.load(arq)
                # Lemos apenas o que pertence ao carrinho atual
                if "carrinho" in dados_json:
                    for obj in dados_json["carrinho"] :
                        c = Carrinho(obj["id"], obj["desc"], obj["quantidade"], obj["id_produto"])
                        self.carrinho.append(c)
                
                # Lemos apenas o que pertence ao histórico de compras
                if "comprados" in dados_json:
                    for obj in dados_json["comprados"] :
                        c = Carrinho(obj["id"], obj["desc"], obj["quantidade"], obj["id_produto"])
                        self.produtos_comprados.append(c)
        except  FileNotFoundError :
            pass
    
    def Inserir_produto(self, c) :
        self.Abrir()
        if len(self.carrinho) == 0: c.id = 1
        else: c.id = self.carrinho[0].id
        self.carrinho.append(c)
        self.Salvar()

    def Comprar_carrinho(self):
        self.Abrir()
        if len(self.carrinho) == 0: return False
        if len(self.produtos_comprados) == 0: id = 1
        else: id = (max(self.produtos_comprados, key = lambda x : x.id)).id + 1
        for obj in self.carrinho:
            obj.id = id
            self.produtos_comprados.append(obj)
        self.carrinho = []
        self.Salvar()
        return True

    def Listar_compras(self) :
        self.Abrir()
        self.produtos_comprados.sort(key = lambda x : x.id)
        return self.produtos_comprados

    def Visualizar_carrinho(self):
        self.Abrir()
        self.carrinho.sort(key = lambda x : x.id_produto)
        return self.carrinho

    def Limpar_carrinho(self) :
        self.Abrir()
        self.carrinho = []
        self.Salvar()