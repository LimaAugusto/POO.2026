import json

class Categoria:
    def __init__(self, id, desc):
        self.setId(id)
        self.setDesc(desc)

    #----- GETTERS -----
    
    def getId(self):
        return self.id
    
    def getDesc(self):
        return self.desc
    
    #----- GETTERS -----

    #----- SETTERS -----

    def setId(self, id):
        if id < 0: raise ValueError("VALOR INVÁLIDO")
        self.id = id
    def setDesc(self, desc):
        self.desc = desc

    #----- SETTERS -----

    #----- TO_STRING -----

    def __str__(self):
        return f"|CATEGORIA_ID: {self.id} | DESCRIÇÃO: {self.desc}|"

    #----- TO_STRING -----

class CategoriaDAO:
    def __init__(self):
        self.categorias = []

    def Salvar(self):
        with open(r"POO2026\pythonn\E-COMMERCE\DADOS-JSON\categorias.json", mode = "w") as arq:
            json.dump(self.categorias, arq, default = vars)

    def Abrir(self):
        self.categorias = []
        try:
            with open(r"POO2026\pythonn\E-COMMERCE\DADOS-JSON\categorias.json", mode = "r") as  arq:
                categorias_json = json.load(arq)
                for obj in categorias_json:
                    cat = Categoria(obj["id"], obj["desc"])
                    self.categorias.append(cat)
        except FileNotFoundError:
            self.categorias = []
    
    def Inserir(self, obj):
        self.Abrir()
        if len(self.categorias) == 0: id = 1
        else: id = (max(self.categorias, key = lambda x: x.id).id) + 1
        obj.id = id
        self.categorias.append(obj)
        self.Salvar()
    
    def Listar(self):
        self.Abrir()
        return self.categorias
    
    def Listar_Id(self, id_escolhido):
        self.Abrir()
        for id in self.categorias:
            if id.getId() == id_escolhido:
                return id
        return None

    def Excluir(self, id):
        self.Abrir()
        cat_id = self.Listar_Id(id)
        if cat_id is not None:
            self.categorias.remove(cat_id)
            self.Salvar()
            return True
        return False

    def Atualizar(self, id):
        self.Abrir()
        cat = self.Listar_Id(id.getId())
        if cat is not None:
            cat.setDesc(id.getDesc())
            self.Salvar()
            return True
        return False