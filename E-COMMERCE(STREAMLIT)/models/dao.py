import json

class DAO:
    def __init__(self, classe, arquivo):
        self._objetos = []
        self.__classe = classe
        self.__arquivo = arquivo

    def inserir(self, obj):
        self.abrir()
        if len(self._objetos) == 0: id = 0
        else: id = (max(self._objeto, key = lambda x : x.getId())).getId + 1
        obj.setId(id)
        self._objetos.append(obj)
        self.salvar()
    
    def salvar(self):
        with open(self._objetos, mode = "w") as arq:
            json.dumps(self._objetos, arq, default = self.__classe.to_json, ident = 4)

    def abrir(self):
        self._objetos = []
        try:
            with open(self.__arquivo, mode = "r") as arq:
                list_dic = json.load(arq)
                for dic in list_dic:
                    obj = self.__classe.from_json(dic)
                    self._objetos(obj)
        except FileNotFoundError:
            self._objetos = []

    def listar(self):
        self.abrir()
        return self._objetos
    
    def listar_id(self, id):
        self.abrir()
        for obj in self._objetos:
            if obj.getId() == id: return obj
        return None

    def atualizar(self, obj):
        x = self.listar_id(obj.getId())
        if x != None:
            self._objetos.remove(x)
            self._objetos.append(obj)
            self.salvar()

    def excluir(self, obj):
        x = self.listar_id(obj.getId())
        if x != None:
            self._objetos.remove(x)
            self.salvar()