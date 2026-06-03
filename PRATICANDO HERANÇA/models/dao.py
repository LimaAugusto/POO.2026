import json

class DAO:
    def __init__(self, classe, arq):
        self._objetos = [] # Para a lista de objetos que servirá de modelo para cada objeto dao não se misturarem, colocamos como protegido, porque assim também podemos acessar pela classe
        self.__classe = classe # Atributo para a classe específica que será passada
        self.__arquivo = arq # Atributo para o arquivo específico json de cada classe de objeto

    def inserir(self, obj):
        self.abrir()
        if len(self._objetos) == 0: id = 1
        else: id = (max(self._objetos, key = lambda x : x.getId())).getId() + 1
        obj.setId(id)
        self._objetos.append(obj)
        self.salvar()

    def salvar(self):
        with open(self.__arquivo, mode = "w") as arq:
            json.dump(self._objetos, arq, default = self.__classe.to__json, ident = 4)

    def abrir(self):
        self._objetos = []
        try:
            with open(self.__arquivo, mode = "r") as arq:
                list_dic = json.load(arq)
                for dic in list_dic:
                    obj = self.__classe.from_json(dic)
                    self._objetos.append(obj)
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
