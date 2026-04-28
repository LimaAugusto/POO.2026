import json

class Cliente :
    def __init__(self, id, n, e, f) :
        self.setID(id)
        self.setNome(n)
        self.setEmail(e)
        self.setFone(f)

    #---------------SETTERS-------------
    def setID(self, v) :
        if v > 0 : self.id = v
        else : return ValueError("VALOR INVÁLIDO")
    def setNome(self, v) :
        self.nome = v
    def setEmail(self, v) :
        self.email = v
    def setFone(self, v) :
        self.fone = v

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