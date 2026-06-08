import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.setId(id)
        self.setNome(nome)
        self.setEmail(email)
        self.setFone(fone)
        self.setSenha(senha)
    
    # ----- GETTERS -----

    def getId(self):
        return self.id
    
    def getNome(self):
        return self.nome
    
    def getEmail(self):
        return self.email
    
    def getFone(self):
        return self.fone
    
    def getSenha(self):
        return self.senha
    
    # ----- GETTERS -----

    # ----- SETTERS -----

    def setId(self, id):
        if id < 0: raise ValueError("ID INVÁLIDO!")
        self.id = id

    def setNome(self, nome):
        self.nome = nome

    def setEmail(self, email):
        self.email = email

    def setFone(self, fone):
        self.fone = fone

    def setSenha(self, senha):
        self.senha = senha
        
    # ----- SETTERS -----

    #----- TO_STRING -----

    def __str__(self):
        return f"|CLIENTE_ID: {self.id} | NOME: {self.nome} | EMAIL: {self.email} | FONE: {self.fone} | SENHA: {self.senha}|"

    #----- TO_STRING -----

class ClienteDAO:
    def __init__(self):
        self.clientes = []
    
    def Salvar(self):
        with open(r"POO2026\pythonn\E-COMMERCE\DADOS-JSON\clientes.json", mode = "w") as arq:
            json.dump(self.clientes, arq, default = vars)
    
    def Abrir(self):
        self.clientes = []
        try:
            with open(r"POO2026\pythonn\E-COMMERCE\DADOS-JSON\clientes.json", mode = "r") as arq:
                clientes_json = json.load(arq)
                for obj in clientes_json:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
                    self.clientes.append(c)
        except FileNotFoundError:
            self.clientes = []

    def Inserir(self, obj):
        self.Abrir()
        if len(self.clientes) == 0: id = 1
        else: id = (max(self.clientes, key = lambda x: x.id).id) + 1
        obj.id = id
        self.clientes.append(obj)
        self.Salvar()

    def Listar(self):
        self.Abrir()
        self.clientes.sort(key = lambda x: x.nome)
        return self.clientes
    
    def Listar_Id(self, id_pedido):
        self.Abrir()
        for id in self.clientes:
            if id.getId() == id_pedido:
                return id
            else: None

    def Excluir(self, id):
        self.Abrir()
        x = self.Listar_Id(id)
        if x is not None:
            self.clientes.remove(x)
            self.Salvar()
        else: False

    def Atualizar(self, id):
        self.Abrir()
        x = self.Listar_Id(id.getId())
        if x is not None:
            x.setNome(id.getNome())
            x.setEmail(id.getEmail())
            x.setFone(id.getFone())
            x.setSenha(id.getSenha())
            self.Salvar()
            return True
        else: return False