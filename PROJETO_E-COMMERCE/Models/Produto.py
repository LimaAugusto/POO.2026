import json

class Produto :
    def __init__(self, id, desc, preco, estoque, id_categoria) :
        self.setID(id)#          <--             ID do produto;
        self.setDesc(desc)#         <--          Descrição do produto;
        self.setPreco(preco)#          <--       Preco do produto;
        self.setEstoque(estoque)#         <--    Quantidade de produtos no estoque;
        self.setId_Categoria(id_categoria)#  <-- ID da categoria;

    #---------------SETTERS-------------
    def setID(self, id: int) :
        # Verifica se o valor passado é um inteiro positivo
        if id >= 0 : self.id = id
        # Se tentar passar texto, número, etc., o código avisa do erro
        else : raise ValueError("VALOR INVÁLIDO")

    def setDesc(self, desc: str) :
        # Verifica se o valor passado é uma string
        if isinstance(desc, str) : self.desc = desc
        # Se tentar passar número, etc., o código avisa do erro
        else : raise ValueError("DIGITE TEXTO")

    def setPreco(self, preco: float) :
        # Verifica se o valor passado é um inteiro positivo
        if preco > 0.0 : self.preco = preco
        # Se tentar passar texto, número, etc., o código avisa do erro
        else : raise ValueError("VALOR INVÁLIDO")

    def setEstoque(self, valor: int) :
        # Verifica se o valor passado é um inteiro positivo
        if valor > 0 : self.estoque = valor
        # Se tentar passar texto, número, etc., o código avisa do erro
        else : raise ValueError("VALOR INVÁLIDO")

    def setId_Categoria(self, id: int) :
        # Verifica se o valor passado é um inteiro positivo
        if id > 0 : self.id_categoria = id
        # Se tentar passar texto, número, etc., o código avisa do erro
        else : raise ValueError("VALOR INVÁLIDO")

    def __str__(self) :
        return f"PRODUTO: ID-{self.id}, DESCRIÇÃO-{self.desc}, PREÇO-R${self.preco:.2f}, ESTOQUE-{self.estoque}, ID CATEGORIA-{self.id_categoria}"
    #-----------------------------------

    #--------------GETTERS------------
    def getID(self) :
        return self.id
    def getDesc(self) :
        return self.desc
    def getPreco(self) :
        return self.preco
    def getEstoque(self) :
        return self.estoque
    def getId_Categoria(self) :
        return self.id_categoria
    #-----------------------------------

class ProdutoDAO :
    def __init__(self) :
        self.produtos = []
    def Salvar(self) :
        with open("PROJETO_E-COMMERCE/DADOS-JSON/produtos.json", mode = "w") as arq :
            json.dump(self.produtos, arq, default = vars)
    def Abrir(self) :
        self.produtos = []
        try :
            with open("PROJETO_E-COMMERCE/DADOS-JSON/produtos.json", mode = "r") as arq :
                produtos_json = json.load(arq)
                for obj in produtos_json :
                    c = Produto(obj["id"], obj["desc"], obj["preco"], obj["estoque"], obj["id_categoria"])
                    self.produtos.append(c)
        except  FileNotFoundError :
            self.produtos = []
    def Inserir(self, obj) :
        self.Abrir()
        if len(self.produtos) == 0 : id = 1
        else: id = (max(self.produtos, key = lambda x : x.id).id) + 1
        obj.id = id
        self.produtos.append(obj)
        self.Salvar()
    def Listar(self) :
        self.Abrir()
        return self.produtos
    def Listar_ID(self, v) :
        self.Abrir()
        for id in self.produtos :
            if id.getID() == v :
                return id
            else : None
    def Excluir(self, id) :
        self.Abrir()
        x = self.Listar_ID(id)
        if x is not None :
            self.produtos.remove(x)
            self.Salvar()
            return True
        else : return False
    def Atualizar(self, id) :
        self.Abrir()
        x = self.Listar_ID(id.getID())
        if x is not None :
            x.setDesc(id.getDesc())
            x.setPreco(id.getPreco())
            x.setEstoque(id.getEstoque())
            x.setId_Categoria(id.getId_Categoria())
            self.Salvar()
            return True
        else : return False