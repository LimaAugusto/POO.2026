import json
class Carrinho:
    def __init__(self, id, desc, qtd, id_produto, id_cliente):
        self.setId(id)
        self.setDescricao(desc)
        self.setQuantidade(qtd)
        self.setId_Produto(id_produto)
        self.setId_Cliente(id_cliente)

    #----- GETTERS -----

    def getId(self):
        return self.id
    
    def getDescricao(self):
        return self.descricao
    
    def getQuantidade(self):
        return self.qtd
    
    def getId_Produto(self):
        return self.id_produto
    
    def getId_Cliente(self):
        return self.id_cliente

    #----- GETTERS -----

    #----- SETTERS -----

    def setId(self, id):
        if id < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id = id

    def setDescricao(self, desc):
        self.desc = desc

    def setQuantidade(self, qtd):
        if qtd < 0: raise ValueError("VALOR INVÁLIDO!")
        self.qtd = qtd

    def setId_Produto(self, id_produto):
        if id_produto < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id_produto = id_produto

    def setId_Cliente(self, id_cliente):
        if id_cliente < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id_cliente = id_cliente

    #----- SETTERS -----

    #----- TO_STRING -----

    def __str__(self):
        return f"|CARRINHO_ID: {self.id} | DESCRIÇÃO: {self.desc} | QUANTIDADE: {self.qtd} | ID_PRODUTO: {self.id_produto} | ID_CLIENTE: {self.id_cliente}|"

    #----- TO_STRING -----

class CarrinhoDAO:
    def __init__(self):
        self.carrinho = []
        self.historico = []

    def Salvar(self):
        with open(r"carrinho.json", mode = "w") as arq:
            json.dump({"carrinho": self.carrinho, "historico": self.historico}, arq, default = vars)
    
    def Abrir(self):
        self.carrinho = []
        self.historico = []
        try:
            with open(r"POO2026\pythonn\E-COMMERCE\DADOS-JSON\carrinho.json", mode = "r") as arq:
                dados_json = json.load(arq)
                if "carrinho" in dados_json:
                    for obj in dados_json["carrinho"]:
                        c = Carrinho(obj["id"], obj["desc"], obj["qtd"], obj["id_produto"], obj["id_cliente"])
                        self.carrinho.append(c)
                        
                if "historico" in dados_json:
                    for obj in dados_json["historico"]:
                        c = Carrinho(obj["id"], obj["desc"], obj["qtd"], obj["id_produto"], obj["id_cliente"])
                        self.historico.append(c)
        except FileNotFoundError:
            self.carrinho = []
            self.historico = []

    def Inserir_produto(self, obj):
        self.Abrir()
        if len(self.carrinho) == 0: id = 1
        else: id = (max(self.carrinho, key = lambda x: x.id).id) + 1
        obj.id = id
        self.carrinho.append(obj)
        self.Salvar()

    def Comprar_carrinho(self, id_cliente):
        self.Abrir()
        # Filtra apenas os itens ativos que pertencem a este cliente específico
        itens_cliente = [obj for obj in self.carrinho if obj.id_cliente == id_cliente]
        if len(itens_cliente) == 0: return False
        
        if len(self.historico) == 0: id_compra = 1
        else: id_compra = max(self.historico, key=lambda x: x.id).id + 1
        
        for obj in itens_cliente:
            obj.id = id_compra
            self.historico.append(obj)
            self.carrinho.remove(obj) # Remove o item do carrinho ativo do cliente    
        self.Salvar()
        return id_compra

    def Listar_compras(self, id_cliente) :
        self.Abrir()
        compras_cliente = [obj for obj in self.historico if obj.id_cliente == id_cliente]
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

    def Retornar_historico(self):
        self.Abrir()
        self.historico.sort(key = lambda x: x.id)
        return self.historico