import json
from datetime import datetime

# ==========================================
#       CLASSES DO MODELO
# ==========================================

class Cliente:
    def __init__(self, id: int, n: str, e: str, f: str):
        self._id = id
        self._nome = n
        self._email = e
        self._fone = f

    # Getters e Setters
    def get_id(self): return self._id
    def set_id(self, id: int): self._id = id
    
    def get_nome(self): return self._nome
    def set_nome(self, nome: str): self._nome = nome
    
    def get_email(self): return self._email
    def set_email(self, email: str): self._email = email
    
    def get_fone(self): return self._fone
    def set_fone(self, fone: str): self._fone = fone

    def __str__(self):
        return f"Cliente [ID: {self._id}] - {self._nome} | E-mail: {self._email} | Fone: {self._fone}"


class Categoria:
    def __init__(self, id: int, d: str):
        self._id = id
        self._descricao = d

    # Getters e Setters
    def get_id(self): return self._id
    def set_id(self, id: int): self._id = id
    
    def get_descricao(self): return self._descricao
    def set_descricao(self, descricao: str): self._descricao = descricao

    def __str__(self):
        return f"Categoria [ID: {self._id}] - {self._descricao}"


class Produto:
    def __init__(self, id: int, d: str, p: float, e: int, idCategoria: int = 0):
        self._id = id
        self._descricao = d
        self._preco = p
        self._estoque = e
        self._idCategoria = idCategoria

    # Getters e Setters
    def get_id(self): return self._id
    def set_id(self, id: int): self._id = id
    
    def get_descricao(self): return self._descricao
    def set_descricao(self, descricao: str): self._descricao = descricao
    
    def get_preco(self): return self._preco
    def set_preco(self, preco: float): self._preco = preco
    
    def get_estoque(self): return self._estoque
    def set_estoque(self, estoque: int): self._estoque = estoque
    
    def get_idCategoria(self): return self._idCategoria
    def set_idCategoria(self, idCategoria: int): self._idCategoria = idCategoria

    def __str__(self):
        return f"Produto [ID: {self._id}] - {self._descricao} | R${self._preco:.2f} | Estoque: {self._estoque} | ID Categoria: {self._idCategoria}"


class Venda:
    def __init__(self, id: int, data: str = "", carrinho: bool = True, total: float = 0.0, idCliente: int = 0):
        self._id = id
        self._data = data
        self._carrinho = carrinho
        self._total = total
        self._idCliente = idCliente

    # Getters e Setters
    def get_id(self): return self._id
    def set_id(self, id: int): self._id = id
    
    def get_data(self): return self._data
    def set_data(self, data: str): 
        if data  == True:  self._data = data
        else: datetime.now().strftime("%d/%m/%Y %H:%M")
    def get_carrinho(self): return self._carrinho
    def set_carrinho(self, carrinho: bool): self._carrinho = carrinho
    
    def get_total(self): return self._total
    def set_total(self, total: float): self._total = total
    
    def get_idCliente(self): return self._idCliente
    def set_idCliente(self, idCliente: int): self._idCliente = idCliente

    def __str__(self):
        return f"Venda [ID: {self._id}] - Data: {self._data} | Carrinho: {self._carrinho} | Total: R${self._total:.2f} | ID Cliente: {self._idCliente}"


class VendaItem:
    def __init__(self, id: int, q: int, p: float, idVenda: int = 0, idProduto: int = 0):
        self._id = id
        self._qtd = q
        self._preco = p
        self._idVenda = idVenda
        self._idProduto = idProduto

    # Getters e Setters
    def get_id(self): return self._id
    def set_id(self, id: int): self._id = id
    
    def get_qtd(self): return self._qtd
    def set_qtd(self, qtd: int): self._qtd = qtd
    
    def get_preco(self): return self._preco
    def set_preco(self, preco: float): self._preco = preco
    
    def get_idVenda(self): return self._idVenda
    def set_idVenda(self, idVenda: int): self._idVenda = idVenda
    
    def get_idProduto(self): return self._idProduto
    def set_idProduto(self, idProduto: int): self._idProduto = idProduto

    def __str__(self):
        return f"Item [ID: {self._id}] - Venda {self._idVenda} | Produto {self._idProduto} | Qtd: {self._qtd} | Preço: R${self._preco:.2f}"


# ==========================================
#       CLASSES DE PERSISTÊNCIA (DAO)
# ==========================================

class ClienteDAO:
    objetos = []

    @classmethod
    def Inserir(cls, obj: Cliente):
        cls.objetos.append(obj)

    @classmethod
    def Listar(cls):
        return cls.objetos

    @classmethod
    def Listar_Id(cls, id: int):
        for obj in cls.objetos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def Atualizar(cls, obj: Cliente):
        c = cls.Listar_Id(obj.get_id())
        if c:
            c.set_nome(obj.get_nome())
            c.set_email(obj.get_email())
            c.set_fone(obj.get_fone())

    @classmethod
    def Excluir(cls, obj: Cliente):
        c = cls.Listar_Id(obj.get_id())
        if c:
            cls.objetos.remove(c)

    @classmethod
    def Salvar(cls):
        with open('clientes.json', 'w') as f:
            json.dump([vars(obj) for obj in cls.objetos], f)

    @classmethod
    def Abrir(cls):
        try:
            with open('clientes.json', 'r') as f:
                dados = json.load(f)
                cls.objetos = [Cliente(d['_id'], d['_nome'], d['_email'], d['_fone']) for d in dados]
        except FileNotFoundError:
            cls.objetos = []


class CategoriaDAO:
    objetos = []

    @classmethod
    def Inserir(cls, obj: Categoria):
        cls.objetos.append(obj)

    @classmethod
    def Listar(cls):
        return cls.objetos

    @classmethod
    def Listar_Id(cls, id: int):
        for obj in cls.objetos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def Atualizar(cls, obj: Categoria):
        c = cls.Listar_Id(obj.get_id())
        if c:
            c.set_descricao(obj.get_descricao())

    @classmethod
    def Excluir(cls, obj: Categoria):
        c = cls.Listar_Id(obj.get_id())
        if c:
            cls.objetos.remove(c)

    @classmethod
    def Salvar(cls):
        with open('categorias.json', 'w') as f:
            json.dump([vars(obj) for obj in cls.objetos], f)

    @classmethod
    def Abrir(cls):
        try:
            with open("categorias.json", "r") as f:
                dados = json.load(f)
                cls.objetos = [Categoria(d["_id"], d["_descricao"]) for d in dados]
        except FileNotFoundError:
            cls.objetos = []


class ProdutoDAO:
    objetos = []

    @classmethod
    def Inserir(cls, obj: Produto):
        cls.objetos.append(obj)

    @classmethod
    def Listar(cls):
        return cls.objetos

    @classmethod
    def Listar_Id(cls, id: int):
        for obj in cls.objetos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def Atualizar(cls, obj: Produto):
        p = cls.Listar_Id(obj.get_id())
        if p:
            p.set_descricao(obj.get_descricao())
            p.set_preco(obj.get_preco())
            p.set_estoque(obj.get_estoque())
            p.set_idCategoria(obj.get_idCategoria())

    @classmethod
    def Excluir(cls, obj: Produto):
        p = cls.Listar_Id(obj.get_id())
        if p:
            cls.objetos.remove(p)

    @classmethod
    def Salvar(cls):
        with open('produtos.json', 'w') as f:
            json.dump([vars(obj) for obj in cls.objetos], f)

    @classmethod
    def Abrir(cls):
        try:
            with open('produtos.json', 'r') as f:
                dados = json.load(f)
                cls.objetos = [Produto(d['_id'], d['_descricao'], d['_preco'], d['_estoque'], d['_idCategoria']) for d in dados]
        except FileNotFoundError:
            cls.objetos = []


class VendaDAO:
    objetos = []

    @classmethod
    def Inserir(cls, obj: Venda): cls.objetos.append(obj)

    @classmethod
    def Listar(cls): return cls.objetos

    @classmethod
    def Listar_Id(cls, id: int):
        for obj in cls.objetos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def Atualizar(cls, obj: Venda):
        v = cls.Listar_Id(obj.get_id())
        if v:
            v.set_data(obj.get_data())
            v.set_carrinho(obj.get_carrinho())
            v.set_total(obj.get_total())
            v.set_idCliente(obj.get_idCliente())

    @classmethod
    def Excluir(cls, obj: Venda):
        v = cls.Listar_Id(obj.get_id())
        if v: cls.objetos.remove(v)

    @classmethod
    def Salvar(cls):
        with open('vendas.json', 'w') as f:
            json.dump([vars(obj) for obj in cls.objetos], f)

    @classmethod
    def Abrir(cls):
        try:
            with open('vendas.json', 'r') as f:
                dados = json.load(f)
                cls.objetos = [Venda(d['_id'], d['_data'], d['_carrinho'], d['_total'], d['_idCliente']) for d in dados]
        except FileNotFoundError:
            cls.objetos = []


class VendaItemDAO:
    objetos = []

    @classmethod
    def Inserir(cls, obj: VendaItem): cls.objetos.append(obj)

    @classmethod
    def Listar(cls): return cls.objetos

    @classmethod
    def Listar_Id(cls, id: int):
        for obj in cls.objetos:
            if obj.get_id() == id: return obj
        return None

    @classmethod
    def Atualizar(cls, obj: VendaItem):
        vi = cls.Listar_Id(obj.get_id())
        if vi:
            vi.set_qtd(obj.get_qtd())
            vi.set_preco(obj.get_preco())
            vi.set_idVenda(obj.get_idVenda())
            vi.set_idProduto(obj.get_idProduto())

    @classmethod
    def Excluir(cls, obj: VendaItem):
        vi = cls.Listar_Id(obj.get_id())
        if vi: cls.objetos.remove(vi)

    @classmethod
    def Salvar(cls):
        with open('venda_itens.json', 'w') as f:
            json.dump([vars(obj) for obj in cls.objetos], f)

    @classmethod
    def Abrir(cls):
        try:
            with open('venda_itens.json', 'r') as f:
                dados = json.load(f)
                cls.objetos = [VendaItem(d['_id'], d['_qtd'], d['_preco'], d['_idVenda'], d['_idProduto']) for d in dados]
        except FileNotFoundError:
            cls.objetos = []


# ==========================================
#           INTERFACE (UI)
# ==========================================

class UI:
    @staticmethod
    def Menu():
        print("\n" + "="*30)
        print(" SISTEMA DE COMÉRCIO ELETRÔNICO ")
        print("="*30)
        print(" 1 - Inserir Cliente     5 - Inserir Categoria    9 - Inserir Produto")
        print(" 2 - Listar Clientes     6 - Listar Categorias   10 - Listar Produtos")
        print(" 3 - Atualizar Cliente   7 - Atualizar Categoria 11 - Atualizar Produto")
        print(" 4 - Excluir Cliente     8 - Excluir Categoria   12 - Excluir Produto")
        print(" 0 - Finalizar Aplicação")
        print("="*30)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    @staticmethod
    def Main():
        ClienteDAO.Abrir()
        CategoriaDAO.Abrir()
        ProdutoDAO.Abrir()
        VendaDAO.Abrir()
        VendaItemDAO.Abrir()

        op = -1
        while op != 0:
            op = UI.Menu()
            
            # --- CLIENTE ---
            if op == 1: UI.InserirCliente()
            elif op == 2: UI.ListarClientes()
            elif op == 3: UI.AtualizarCliente()
            elif op == 4: UI.ExcluirCliente()
            
            # --- CATEGORIA ---
            elif op == 5: UI.InserirCategoria()
            elif op == 6: UI.ListarCategorias()
            elif op == 7: UI.AtualizarCategoria()
            elif op == 8: UI.ExcluirCategoria()
            
            # --- PRODUTO ---
            elif op == 9: UI.InserirProduto()
            elif op == 10: UI.ListarProdutos()
            elif op == 11: UI.AtualizarProduto()
            elif op == 12: UI.ExcluirProduto()
            
            elif op == 0:
                print("Salvando dados e finalizando...")
                ClienteDAO.Salvar()
                CategoriaDAO.Salvar()
                ProdutoDAO.Salvar()
                VendaDAO.Salvar()
                VendaItemDAO.Salvar()
            else:
                print("Opção inválida.")

    # ------ MÉTODOS CRUD CLIENTE ------
    @staticmethod
    def InserirCliente():
        id = int(input("ID: "))
        nome = input("Nome: ")
        email = input("E-mail: ")
        fone = input("Fone: ")
        ClienteDAO.Inserir(Cliente(id, nome, email, fone))
        print("Cliente inserido com sucesso!")

    @staticmethod
    def ListarClientes():
        for c in ClienteDAO.Listar():
            print(c)

    @staticmethod
    def AtualizarCliente():
        UI.ListarClientes()
        id = int(input("ID do cliente a atualizar: "))
        nome = input("Novo Nome: ")
        email = input("Novo E-mail: ")
        fone = input("Novo Fone: ")
        ClienteDAO.Atualizar(Cliente(id, nome, email, fone))
        print("Cliente atualizado.")

    @staticmethod
    def ExcluirCliente():
        UI.ListarClientes()
        id = int(input("ID do cliente a excluir: "))
        c = Cliente(id, "", "", "")
        ClienteDAO.Excluir(c)
        print("Cliente excluído.")

    # ------ MÉTODOS CRUD CATEGORIA ------
    @staticmethod
    def InserirCategoria():
        id = int(input("ID: "))
        descricao = input("Descrição: ")
        CategoriaDAO.Inserir(Categoria(id, descricao))
        print("Categoria inserida com sucesso!")

    @staticmethod
    def ListarCategorias():
        for c in CategoriaDAO.Listar():
            print(c)

    @staticmethod
    def AtualizarCategoria():
        UI.ListarCategorias()
        id = int(input("ID da categoria a atualizar: "))
        descricao = input("Nova Descrição: ")
        CategoriaDAO.Atualizar(Categoria(id, descricao))
        print("Categoria atualizada.")

    @staticmethod
    def ExcluirCategoria():
        UI.ListarCategorias()
        id = int(input("ID da categoria a excluir: "))
        c = Categoria(id, "")
        CategoriaDAO.Excluir(c)
        print("Categoria excluída.")

    # ------ MÉTODOS CRUD PRODUTO ------
    @staticmethod
    def InserirProduto():
        id = int(input("ID: "))
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        UI.ListarCategorias()
        idCategoria = int(input("ID da Categoria (Acima): "))
        ProdutoDAO.Inserir(Produto(id, descricao, preco, estoque, idCategoria))
        print("Produto inserido com sucesso!")

    @staticmethod
    def ListarProdutos():
        for p in ProdutoDAO.Listar():
            print(p)

    @staticmethod
    def AtualizarProduto():
        UI.ListarProdutos()
        id = int(input("ID do produto a atualizar: "))
        descricao = input("Nova Descrição: ")
        preco = float(input("Novo Preço: "))
        estoque = int(input("Novo Estoque: "))
        idCategoria = int(input("Novo ID de Categoria: "))
        ProdutoDAO.Atualizar(Produto(id, descricao, preco, estoque, idCategoria))
        print("Produto atualizado.")

    @staticmethod
    def ExcluirProduto():
        UI.ListarProdutos()
        id = int(input("ID do produto a excluir: "))
        p = Produto(id, "", 0.0, 0, 0)
        ProdutoDAO.Excluir(p)
        print("Produto excluído.")

# ==========================================
# INÍCIO DO PROGRAMA
# ==========================================

UI.Main()