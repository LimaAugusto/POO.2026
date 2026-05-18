import json
from datetime import datetime

def conversor_json(obj):
    if isinstance(obj, datetime): # Se for um objeto/atributo em datetime
        return obj.isoformat() # Converte a data para string no formato ISO
    return vars(obj) # Se não, retorna atributos normais do objeto, ou data em string, se já estiver

class Venda :
    def __init__(self, id, data, carrinho, total, id_cliente) :
        self.setID(id)
        self.setData(data)
        self.setCarrinho(carrinho)
        self.setTotal(total)
        self.setId_Cliente(id_cliente)

    #---------------SETTERS-------------
    def setID(self, id: int) :
        # Verifica se o valor passado é um inteiro positivo
        if id > 0 : self.id = id
        # Se tentar passar texto, número, etc., o código avisa do erro
        else : raise ValueError("VALOR INVÁLIDO")

    def setData(self, data) :
        if isinstance(data, str) :
            try :
                self.data = datetime.fromisoformat(data)
            except ValueError :
                self.data = datetime.strptime(data, "%d/%m/%Y %H:%M")
        else :
            self.data = data

    def setCarrinho(self, carrinho: bool) : # True == carrinho aberto para compras, False == carrinho fechado para compras
        # Verifica se o valor passado já é do tipo booleano (bool)
        if isinstance(carrinho, bool): self.carrinho = carrinho
        # Se tentar passar texto, número, etc., o código avisa do erro 
        else: raise ValueError("O carrinho deve ser um valor booleano (True ou False)")

    def setTotal(self, total) :
        self.total = total

    def setId_Cliente(self, id: int) :
        # Verifica se o valor passado é um inteiro positivo
        if id > 0 : self.id_cliente = id
        # Se tentar passar texto, número, etc., o código avisa do erro
        else : raise ValueError("VALOR INVÁLIDO")

    def __str__(self) :
        return f"VENDA: ID-{self.id}, DATA-{self.data}, CARRINHO-{self.carrinho}, TOTAL-{self.total}, ID CLIENTE-{self.id_cliente}"
    #-----------------------------------

    #--------------GETTERS------------
    def getID(self) :
        return self.id
    def getData(self) :
        return self.data
    def getCarrinho(self) :
        return self.carrinho
    def getTotal(self) :
        return self.total
    def getId_Cliente(self) :
        return self.id_cliente
    #-----------------------------------

class VendaDAO :
    def __init__(self) :
        self.vendas = []
    def Salvar(self) :
        with open("PROJETO_E-COMMERCE/DADOS-JSON/vendas.json", mode = "w") as arq :
            json.dump(self.vendas, arq, default = conversor_json)
    def Abrir(self) :
        self.vendas = []
        try :
            with open("PROJETO_E-COMMERCE/DADOS-JSON/vendas.json", mode = "r") as arq :
                vendas_json = json.load(arq)
                for obj in vendas_json :
                    c = Venda(obj["id"], obj["data"], obj["carrinho"], obj["total"], obj["id_cliente"])
                    self.vendas.append(c)
        except  FileNotFoundError :
            self.vendas = []
    def Inserir(self, obj) :
        self.Abrir()
        self.vendas.append(obj)
        self.Salvar()
    def Listar(self) :
        self.Abrir()
        return self.vendas
    def Listar_ID(self, v) :
        self.Abrir()
        for id in self.vendas :
            if id.getID() == v :
                return id
            else : None
    def Excluir(self, id) :
        self.Abrir()
        x = self.Listar_ID(id)
        if x is not None :
            self.vendas.remove(x)
            self.Salvar()
            return True
        else : return False
    def Atualizar(self, id) :
        self.Abrir()
        x = self.Listar_ID(id.getID())
        if x is not None :
            x.setData(id.getData())
            x.setCarrinho(id.getCarrinho())
            x.setTotal(id.getTotal())
            x.setId_Cliente(id.getId_Cliente())
            self.Salvar()
            return True
        else : return False