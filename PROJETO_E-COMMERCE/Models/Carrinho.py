import json

class Carrinho:
    def __init__(self, id, desc, quantidade, id_produto, id_cliente) :
        self.setID(id)#           <--             ID do carrinho;
        self.setDesc(desc)#          <--          Descrição do carrinho;
        self.setQuantidade(quantidade)# <--       Quantidade do carrinho;
        self.setIdProduto(id_produto)#     <--    ID do produto do carrinho;
        self.setIdCliente(id_cliente)#        <-- ID do cliente do devido carirnho;

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
    def setIdCliente(self, id) :
        if id >= 0 : self.id_cliente = id
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
                        c = Carrinho(obj["id"], obj["desc"], obj["quantidade"], obj["id_produto"], obj["id_cliente"])
                        self.carrinho.append(c)
                
                # Lemos apenas o que pertence ao histórico de compras
                if "comprados" in dados_json:
                    for obj in dados_json["comprados"] :
                        c = Carrinho(obj["id"], obj["desc"], obj["quantidade"], obj["id_produto"], obj["id_cliente"])
                        self.produtos_comprados.append(c)
        except  FileNotFoundError :
            pass
    
    def Inserir_produto(self, c) :
        self.Abrir()
        if len(self.carrinho) == 0: c.id = 1
        else: c.id = max(self.carrinho, key = lambda x : x.id).id + 1
        self.carrinho.append(c)
        self.Salvar()

    def Comprar_carrinho(self, id_cliente):
        self.Abrir()
        # Filtra apenas os itens ativos que pertencem a este cliente específico
        itens_cliente = [obj for obj in self.carrinho if obj.id_cliente == id_cliente]
        if len(itens_cliente) == 0: return False
        
        if len(self.produtos_comprados) == 0: id_compra = 1
        else: id_compra = max(self.produtos_comprados, key=lambda x: x.id).id + 1
        
        for obj in itens_cliente:
            obj.id = id_compra
            self.produtos_comprados.append(obj)
            self.carrinho.remove(obj) # Remove o item do carrinho ativo do cliente
            
        self.Salvar()
        return True
    
    def Listar_compras(self, id_cliente) :
        self.Abrir()
        compras_cliente = [obj for obj in self.produtos_comprados if obj.id_cliente == id_cliente]
        compras_cliente.sort(key=lambda x: x.id)
        return compras_cliente

    def Visualizar_carrinho(self, id_cliente):
        self.Abrir()
        carrinho_cliente = [obj for obj in self.carrinho if obj.id_cliente == id_cliente]
        carrinho_cliente.sort(key=lambda x: x.id_produto)
        return carrinho_cliente

    def Limpar_carrinho(self, id_cliente) :
        self.Abrir()
        self.carrinho = [obj for obj in self.carrinho if obj.id_cliente != id_cliente]
        self.Salvar()