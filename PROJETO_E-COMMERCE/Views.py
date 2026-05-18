from Models.Cliente import Cliente, ClienteDAO
from Models.Categoria import Categoria, CategoriaDAO
from Models.Produto import Produto, ProdutoDAO
from Models.Carrinho import Carrinho, CarrinhoDAO
from Models.Venda import Venda, VendaDAO


class View:

    #--------- AUTENTICAÇÃO ----------
    @staticmethod
    def verifica_cria_admin():
        for obj in View.listar_cliente(): 
            if obj.getEmail() == "admin": return
        View.inserir_cliente("admin", "admin", "(84)912345678", "1234")

    @staticmethod 
    def cliente_autenticar(email, senha):
        for obj in View.listar_cliente(): 
            if obj.getEmail() == email and obj.getSenha() == senha:
                return { "id": obj.getID(), "nome": obj.getNome() }
        return None
    #--------- AUTENTICAÇÃO ----------

    #--------- CRUD CLIENTE ----------
    @staticmethod
    def inserir_cliente(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        ClienteDAO().Inserir(c)
    
    @staticmethod
    def listar_cliente():
        return ClienteDAO().Listar()
    
    @staticmethod
    def excluir_cliente(id):
        return ClienteDAO().Excluir(id)
    
    @staticmethod
    def atualizar_cliente(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        ClienteDAO().Atualizar(c)
    #--------- CRUD CLIENTE ----------

    #--------- CRUD CATEGORIA ----------
    @staticmethod
    def inserir_categoria(desc):
        cat = Categoria(0, desc)
        CategoriaDAO().Inserir(cat)
    
    @staticmethod
    def listar_categoria():
        return CategoriaDAO().Listar()
    
    @staticmethod
    def excluir_categoria(id):  
        return CategoriaDAO().Excluir(id)
    
    @staticmethod
    def atualizar_categoria(id, desc):
        cat = Categoria(id, desc)
        CategoriaDAO().Atualizar(cat)
    #--------- CRUD CATEGORIA ----------

    #--------- CRUD PRODUTOS ----------
    @staticmethod
    def inserir_produto(desc, preco, estoque, id_cat):
        p = Produto(0, desc, preco, estoque, id_cat)
        ProdutoDAO().Inserir(p)
    
    @staticmethod
    def listar_produto():
        return ProdutoDAO().Listar()
    
    @staticmethod
    def excluir_produto(id):  
        return ProdutoDAO().Excluir(id)
    
    @staticmethod
    def atualizar_produto(id, desc, preco, estoque, id_cat):
        produto_antigo = ProdutoDAO().Listar_ID(id)
        if produto_antigo is not None:
            c = Produto(id, desc, preco, estoque, id_cat)
            ProdutoDAO().Atualizar(c)
    #--------- CRUD PRODUTOS ----------

    #--------- CRUD CARRINHO ----------
    @staticmethod
    def inserir_produto_carrinho(quantidade, id_produto):
        produto = ProdutoDAO().Listar_ID(id_produto)
        if produto is None:
            return False
        item = Carrinho(id = 0,  desc = produto.desc, quantidade = quantidade, id_produto = id_produto)
        CarrinhoDAO().Inserir_produto(item)
        return True

    @staticmethod
    def listar_produto_carrinho():
        return ProdutoDAO().Listar()
    
    @staticmethod
    def listar_compras():
        return CarrinhoDAO().Listar_compras()
    
    @staticmethod
    def limpar_carrinho():  
        return CarrinhoDAO().Limpar_carrinho()
    
    @staticmethod
    def visualizar_carrinho():
        return CarrinhoDAO().Visualizar_carrinho()
    
    @staticmethod
    def comprar_carrinho():
        return CarrinhoDAO().Comprar_carrinho()
    #--------- CRUD CARRINHO ----------

    #--------- NOVOS MÉTODOS (VENDAS E REAJUSTE) ----------
    @staticmethod
    def reajustar_preco(percentual):
        produtos = ProdutoDAO().Listar()
        for p in produtos:
            novo_preco = p.getPreco() + (p.getPreco() * (percentual / 100))
            p.setPreco(novo_preco)
            ProdutoDAO().Atualizar(p)
            
    @staticmethod
    def listar_vendas_cliente(id_cliente):
        todas_vendas = VendaDAO().Listar()
        vendas_do_cliente = []
        for venda in todas_vendas:
            # Compara o ID salvo na venda com o ID procurado
            if venda.getId_Cliente() == id_cliente:
                vendas_do_cliente.append(venda)
        return vendas_do_cliente
    #--------- NOVOS MÉTODOS (VENDAS E REAJUSTE) ----------