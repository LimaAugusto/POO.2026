from datetime import datetime
from models.cliente import Cliente, ClienteDAO
from models.categoria import Categoria, CategoriaDAO
from models.produto import Produto, ProdutoDAO
#from models.carrinho import Carrinho, CarrinhoDAO
from models.venda import Venda, VendaDAO

class View:

    #----- AUTENTICAÇÃO -----

    @staticmethod
    def cria_admin():
        for obj in View.listar_cliente():
            if obj.getEmail() == "admin": return
        View.inserir_cliente("admin", "admin", "(84)987654321", "1234")
  
    @staticmethod
    def usuario_autenticar(email, senha):
        for obj in View.listar_cliente():
            if obj.getEmail() == email and obj.getSenha() == senha:
                return { "id" : obj.getId(), "nome" : obj.getNome() }
        return None
    
    #----- AUTENTICAÇÃO -----

    #----- CRUD CLIENTE -----

    @staticmethod
    def inserir_cliente(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        ClienteDAO().inserir(c)

    @staticmethod
    def listar_cliente():
        return ClienteDAO().listar()
    
    @staticmethod
    def atualizar_cliente(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        verifica = ClienteDAO().atualizar(c)
        if verifica == True:
            return True
        else: return False
    
    @staticmethod
    def excluir_cliente(id):
        c = Cliente(id, "nome", "email", "fone", "senha")
        return ClienteDAO().excluir(c)
    
    #----- CRUD CLIENTE -----

    #----- CRUD CATEGORIA -----
    
    @staticmethod
    def inserir_categoria(desc):
        cat = Categoria(0, desc)
        CategoriaDAO().inserir(cat)
    
    @staticmethod
    def listar_categoria():
        return CategoriaDAO().listar()
    
    @staticmethod
    def excluir_categoria(id):
        c = Categoria(id, "desc")
        return CategoriaDAO().excluir(c)
    
    @staticmethod
    def atualizar_categoria(id, desc):
        cat = Categoria(id, desc)
        verifica = CategoriaDAO().atualizar(cat)
        if verifica == True:
            return True
        else: return False
    
    #----- CRUD CATEGORIA -----

    #----- CRUD PRODUTOS -----

    @staticmethod
    def inserir_produto(desc, preco, estoque, id_cat):
        p = Produto(0, desc, preco, estoque, id_cat)
        ProdutoDAO().inserir(p)
    
    @staticmethod
    def listar_produto():
        return ProdutoDAO().listar()
    
    @staticmethod
    def excluir_produto(id):
        p = Produto(id, "desc", 00.0, 0, 0)
        return ProdutoDAO().excluir(p)
    
    @staticmethod
    def atualizar_produto(id, desc, preco, estoque, id_cat):
        c = Produto(id, desc, preco, estoque, id_cat)
        verifica = ProdutoDAO().atualizar(c)
        if verifica == True:
            return True
        else: return False

    #----- CRUD PRODUTOS -----

    #----- NOVOS MÉTODOS (VENDAS E REAJUSTE) -----

    @staticmethod
    def reajustar_preco(percentual):
        produtos = ProdutoDAO().listar()
        for p in produtos:
            novo_preco = p.getPreco() + (p.getPreco() * (percentual / 100))
            p.setPreco(novo_preco)
            ProdutoDAO().atualizar(p)
            
    @staticmethod
    def listar_vendas_cliente(id_cliente):
        todas_vendas = VendaDAO().listar()
        vendas_do_cliente = []
        for venda in todas_vendas:
            if venda.getId_Cliente() == id_cliente:
                vendas_do_cliente.append(venda)
        return vendas_do_cliente
    
    #----- NOVOS MÉTODOS (VENDAS E REAJUSTE) -----