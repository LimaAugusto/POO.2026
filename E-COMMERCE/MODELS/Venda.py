import json
from datetime import datetime

# ESSE CONVERSOR VERIFICA SE O OBJETO É DO TIPO DATETIME:
# SE SIM, ELE RETORNA O OBJETO, AGORA TRANSFORMADO EM STRING NO FORMATO ISO(INTERNACIONAL).
# SE NÃO, ELE USA O VARS PARA RETORNAR OS ATRIBUTOS NORMAIS DO OBJETO, COMO UMA STRING, POR EXEMPLO.
def conversor_json(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return vars(obj) 

class Venda:
    def __init__(self, id, data, carrinho, total, id_cliente):
        self.setId(id)
        self.setData(data)
        self.setCarrinho(carrinho)
        self.setTotal(total)
        self.setId_Cliente(id_cliente)

    #----- GETTERS -----

    def getId(self):
        return self.id_cliente
    
    def getData(self):
        return self.data
    
    def getCarrinho(self):
        return self.carrinho
    
    def getTotal(self):
        return self.total
    
    def getId_Cliente(self):
        return self.id_cliente

    #----- GETTERS -----

    #----- SETTERS -----

    def setId(self, id):
        if id < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id = id

    def setData(self, data):
        if isinstance(data, str): # Se a data for uma string:
            try:
                self.data = datetime.fromisoformat(data) # Tenta passar para o formato ISO(internacional) EX.: 2026-05-26 15:30:00
            except ValueError: # Se for uma string e não estiver no padrão internacional, ele tenta forçar para o formato brasileiro: DD/MM/AAAA HH:MM
                self.data = datetime.strptime(data, "%d/%m/%Y %H:%M")
        else: self.data = data # Se não for uma string, pode ser um núemro, etc. ele apenas atribui o valor ao self.data

    def setCarrinho(self, carrinho): # CARRINHO ABERTO = TRUE | CARRINHO FECHADO = FALSE
        if isinstance(carrinho, bool): self.carrinho = carrinho
        else: raise ValueError("O CARRINHO DEVE SER UM VALOR BOOLEANO!")

    def setTotal(self, total):
        if total < 0: raise ValueError("VALOR INVÁLIDO!")
        self.total = total

    def setId_Cliente(self, id_cliente):
        if id_cliente < 0: raise ValueError("VALOR INVÁLIDO!")
        self.id_cliente = id_cliente

    #----- SETTERS -----

    #----- TO_STRING -----

    def __str__(self):
        return f"|VENDA_ID: {self.id} | DATA: {self.data} | CARRINHO: {self.carrinho} | TOTAL: R${self.total:.2f} | ID_CLIENTE: {self.id_cliente}|"

    #----- TO_STRING -----

class VendaDAO:
    def __init__(self):
        self.vendas = []
    
    def Salvar(self):
        with open(r"POO2026\pythonn\E-COMMERCE\DADOS-JSON\vendas.json", mode = "w") as arq:
            json.dump(self.vendas, arq, default = conversor_json)
    
    def Abrir(self):
        self.vendas = []
        try:
            with open(r"POO2026\pythonn\E-COMMERCE\DADOS-JSON\vendas.json", mode = "r") as arq:
                vendas_json = json.load(arq)
                for obj in vendas_json:
                    v = Venda(obj["id"], obj["data"], obj["carrinho"], obj["total"], obj["id_cliente"])
                    self.vendas.append(v)
        except FileNotFoundError:
            self.vendas = []
    
    def Inserir(self, obj):
        self.Abrir()
        self.vendas.append(obj)
        self.Salvar()

    def Listar(self):
        self.Abrir()
        return self.vendas
    
    def Listar_Id(self, id):
        self.Abrir()
        for obj in self.vendas:
            if obj.getId() == id:
                return id
        return None

    def Excluir(self, id_requisitado):
        self.Abrir()
        x = self.Listar_Id(id_requisitado)
        if x is not None:
            self.vendas.remove(x)
            self.Salvar()
            return True
        return False
    
    def Atualizar(self, id):
        self.Abrir()
        x = self.Listar_Id(id.getId())
        if x is not None:
            x.setData(id.getData())
            x.setCarrinho(id.getCarrinho())
            x.setTotal(id.getTotal())
            x.setId_Cliente(id.getId_Cliente())
            self.Salvar()
            return True
        return False