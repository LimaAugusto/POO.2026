import json

class Venda :
    def __init__(self, id, d, c, t, idc) :
        self.setID(id)
        self.setData(d)
        self.setCarrinho(c)
        self.setTotal(idc)
        self.setIDCliente(idc)

    #---------------SETTERS-------------
    def setID(self, v) :
        if v > 0 : self.id = v
        else : return ValueError("VALOR INVÁLIDO")
    def setData(self, v) :
        self.data = v
    def setCarrinho(self, v) :
        self.carrinho = v
    def setTotal(self, v) :
        self.total = v

    #--------------GETTERS------------
    def getID(self) :
        return self.id
    def getNome(self) :
        return self.nome
    def setEmail(self) :
        return self.email
    def setFone(self) :
        return self.fone

class ClienteDAO :
    def __init__(self) :
        self.clientes = []
    def Salvar(self) :
        with open("clientes.json", mode = "w") as arq :
            json.dump(self.clientes, arq, default = vars)
    def Abrir(self) :
        self.clientes = []
        try :
            with open("clientes.json", mode = "r") as arq :
                clientes_json = json.load(arq)
                for obj in clientes_json :
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                    self.clientes.append(c)
        except : FileNotFoundError
        self.clientes = []
    def Inserir(self, obj) :
        self.Abrir()
        self.clientes.append(obj)
        self.Salvar()
    def Listar(self) :
        self.Abrir()
        return self.clientes
    def Listar_ID(self, v) :
        self.Abrir()
        for id in self.clientes :
            if id.getID() == v :
                return id
            else : None
    def Excluir(self, id) :
        self.Abrir()
        x = self.Listar_ID(id)
        if x is not None :
            self.clientes.remove(x)
            self.Salvar()
            return True
        else : return False
    def Atualizar(self, id) :
        self.Abrir()
        x = self.Listar_ID(id.getID())
        if x is not None :
            x.setNome(id.getNome())
            x.setEmail(id.getEmail())
            x.setFone(id.getFone())
            self.Salvar()
            return True
        else : return False