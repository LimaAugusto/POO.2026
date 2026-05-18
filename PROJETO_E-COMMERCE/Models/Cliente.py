import json

class Cliente :
    def __init__(self, id, nome, email, fone, senha) :
        self.setID(id)#   <--              ID do cliente;
        self.setNome(nome)#  <--           Nome do cliente;
        self.setEmail(email)#   <--        Email do cliente;
        self.setFone(fone)#        <--     Fone do cliente;
        self.setSenha(senha)#         <--  Senha do cliente

    #---------------SETTERS-------------
    def setID(self, v) :
        if v >= 0: self.id = v
        else: raise ValueError("VALOR INVÁLIDO")
    def setNome(self, v) :
        self.nome = v
    def setEmail(self, v) :
        self.email = v
    def setFone(self, v) :
        self.fone = v
    def setSenha(self, v) :
        self.senha = v
    def __str__(self) :
        return f"Cliente: ID-{self.id}, NOME-{self.nome}, EMAIL-{self.email}, FONE-{self.fone}"

    #--------------GETTERS------------
    def getID(self) :
        return self.id
    def getNome(self) :
        return self.nome
    def getEmail(self) :
        return self.email
    def getFone(self) :
        return self.fone
    def getSenha(self) :
        return self.senha

class ClienteDAO :
    def __init__(self) :
        self.clientes = []
    def Salvar(self) :
        with open("PROJETO_E-COMMERCE/DADOS-JSON/clientes.json", mode = "w") as arq :
            json.dump(self.clientes, arq, default = vars)
    def Abrir(self) :
        self.clientes = []
        try :
            with open("PROJETO_E-COMMERCE/DADOS-JSON/clientes.json", mode = "r") as arq :
                clientes_json = json.load(arq)
                for obj in clientes_json :
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
                    self.clientes.append(c)
        except  FileNotFoundError :
            self.clientes = []
    def Inserir(self, obj) :
        self.Abrir()
        if len(self.clientes) == 0 : id = 1
        else: id = (max(self.clientes, key = lambda x : x.id).id) + 1
        obj.id = id
        self.clientes.append(obj)
        self.Salvar()
    def Listar(self) :
        self.Abrir()
        self.clientes.sort(key = lambda x : x.nome)
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
            x.setSenha(id.getSenha())
            self.Salvar()
            return True
        else : return False