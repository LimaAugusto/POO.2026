import json

class Categoria :
    def __init__(self, id, desc) :
        self.setID(id)#   <--     ID da categoria do item;
        self.setDesc(desc)#  <--  Descrição do item;

    #---------------SETTERS-------------
    def setID(self, id) :
        if id >= 0 : self.id = id
        else : raise ValueError("VALOR INVÁLIDO")
    def setDesc(self, desc) :
        self.desc = desc
    def __str__(self) :
        return f"CATEGORIA: ID-{self.id}, DESCRIÇÃO-{self.desc}"

    #--------------GETTERS------------
    def getID(self) :
        return self.id
    def getDesc(self) :
        return self.desc

class CategoriaDAO :
    def __init__(self) :
        self.categorias = []
    def Salvar(self) :
        with open("PROJETO_E-COMMERCE/DADOS-JSON/categorias.json", mode = "w") as arq :
            json.dump(self.categorias, arq, default = vars)
    def Abrir(self) :
        self.categorias = []
        try :
            with open("PROJETO_E-COMMERCE/DADOS-JSON/categorias.json", mode = "r") as arq :
                categorias_json = json.load(arq)
                for obj in categorias_json :
                    c = Categoria(obj["id"], obj["desc"])
                    self.categorias.append(c)
        except  FileNotFoundError :
            self.categorias = []
    def Inserir(self, cat) :
        self.Abrir()
        if len(self.categorias) == 0 : id = 1
        else: id = (max(self.categorias, key = lambda x : x.id).id) + 1
        cat.id = id
        self.categorias.append(cat)
        self.Salvar()
    def Listar(self) :
        self.Abrir()
        return self.categorias
    def Listar_ID(self, id_escolhido) :
        self.Abrir()
        for id in self.categorias :
            if id.getID() == id_escolhido :
                return id
            else : None
    def Excluir(self, id) :
        self.Abrir()
        cat_id = self.Listar_ID(id)
        if cat_id is not None :
            self.categorias.remove(cat_id)
            self.Salvar()
            return True
        else : return False
    def Atualizar(self, id) :
        self.Abrir()
        cat = self.Listar_ID(id.getID())
        if cat is not None :
            cat.setDesc(id.getDesc())
            self.Salvar()
            return True
        else : return False