from datetime import datetime
from MODELS.Cliente import Cliente, ClienteDAO
from MODELS.Categoria import Categoria, CategoriaDAO
from MODELS.Produto import Produto, ProdutoDAO
from MODELS.Carrinho import Carrinho, CarrinhoDAO
from MODELS.Venda import Venda, VendaDAO

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
        ClienteDAO().Inserir(c)

    @staticmethod
    def listar_cliente():
        return ClienteDAO().Listar()
    
    @staticmethod
    def atualizar_cliente(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        verifica = ClienteDAO().Atualizar(c)
        if verifica == True:
            return True
        else: return False
    
    @staticmethod
    def excluir_cliente(id):
        return ClienteDAO().Excluir(id)
    
    #----- CRUD CLIENTE -----

    #----- CRUD CATEGORIA -----
    
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
        verifica = CategoriaDAO().Atualizar(cat)
        if verifica == True:
            return True
        else: return False
    
    #----- CRUD CATEGORIA -----

    #----- CRUD PRODUTOS -----

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
        c = Produto(id, desc, preco, estoque, id_cat)
        verifica = ProdutoDAO().Atualizar(c)
        if verifica == True:
            return True
        else: return False

    #----- CRUD PRODUTOS -----

    #----- CRUD CARRINHO -----

    @staticmethod
    def inserir_produto_carrinho(quantidade, id_produto, id_cliente):
        produto = ProdutoDAO().Listar_Id(id_produto)
        if produto is None: 
            return False
        item = Carrinho(id = 0, desc = produto.getDesc(), qtd = quantidade, id_produto = id_produto, id_cliente = id_cliente)
        CarrinhoDAO().Inserir_produto(item)
        return True

    @staticmethod
    def listar_produto_carrinho():
        return ProdutoDAO().Listar()
    
    @staticmethod
    def listar_compras(id_cliente):
        return CarrinhoDAO().Listar_compras(id_cliente)
    
    @staticmethod
    def limpar_carrinho(id_cliente):  
        return CarrinhoDAO().Limpar_carrinho(id_cliente)
    
    @staticmethod
    def visualizar_carrinho(id_cliente):
        return CarrinhoDAO().Visualizar_carrinho(id_cliente)
    
    @staticmethod
    def comprar_carrinho(id_cliente):
        # 1. Pegamos os itens que estão atualmente no carrinho do cliente
        itens_carrinho = CarrinhoDAO().Visualizar_carrinho(id_cliente) 
        if not itens_carrinho:
            return False # Retorna falso se o carrinho estiver vazio

        # 2. Calculamos o valor total da compra
        total = 0
        for item in itens_carrinho:
            # Puxamos o produto para descobrir o preço atual dele
            produto = ProdutoDAO().Listar_Id(item.getId_Produto())
            if produto:
                total += produto.getPreco() * item.getQuantidade()

        # 3. Movemos os itens para o histórico.json (seu código original já faz isso muito bem)
        id_compra = CarrinhoDAO().Comprar_carrinho(id_cliente)

        # 4. Se os itens foram para o histórico com sucesso, geramos o "recibo" (a Venda)
        if id_compra:
            # Cria a nova Venda. O atributo 'carrinho' recebe 'False' indicando que o carrinho foi fechado.
            nova_venda = Venda(
                id = id_compra, 
                data = datetime.now(), 
                carrinho = False, 
                total = total, 
                id_cliente = id_cliente
            )
            VendaDAO().Inserir(nova_venda)
            return True
            
        return False
    #----- CRUD CARRINHO -----

    #----- NOVOS MÉTODOS (VENDAS E REAJUSTE) -----

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
            if venda.getId_Cliente() == id_cliente:
                vendas_do_cliente.append(venda)
        return vendas_do_cliente
    
    #----- NOVOS MÉTODOS (VENDAS E REAJUSTE) -----