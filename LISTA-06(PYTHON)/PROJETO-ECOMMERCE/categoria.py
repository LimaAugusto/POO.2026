import json

class Categoria :
    def __init__(self, id, d) :
        self.setID(id)
        self.setDesc(d)

    #---------------SETTERS-------------
    def setID(self, v) :
        if v > 0 : self.id = v
        else : return ValueError("VALOR INVÁLIDO")
    def setDesc(self, v) :
        self.desc = v

    #--------------GETTERS------------
    def getID(self) :
        return self.id
    def getDesc(self) :
        return self.d

class CategoriaDAO :
    def __init__(self) :
        self.categorias = []
    def Salvar(self) :
        with open("categorias.json", mode = "w") as arq :
            json.dump(self.categorias, arq, default = vars)
    def Abrir(self) :
        self.categorias = []
        try :
            with open("categorias.json", mode = "r") as arq :
                categorias_json = json.load(arq)
                for obj in categorias_json :
                    c = Categoria(obj["id"], obj["nome"], obj["email"], obj["fone"])
                    self.categorias.append(c)
        except : FileNotFoundError
        self.categorias = []
    def Inserir(self, obj) :
        self.Abrir()
        self.categorias.append(obj)
        self.Salvar()
    def Listar(self) :
        self.Abrir()
        return self.categorias
    def Listar_ID(self, v) :
        self.Abrir()
        for id in self.categorias :
            if id.getID() == v :
                return id
            else : None
    def Excluir(self, id) :
        self.Abrir()
        x = self.Listar_ID(id)
        if x is not None :
            self.categorias.remove(x)
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