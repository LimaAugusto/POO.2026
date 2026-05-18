from Views import View

class UIadmin:
    @staticmethod
    def Ler_Opcao():
        try:
            return int(input("Escolha: "))
        except ValueError:
            return -1

    @staticmethod    
    def Main():
        while True:
            op = UIadmin.Menu_principal()
            if op == 1: UIadmin.Menu_cliente()
            if op == 2: UIadmin.Menu_produto()
            if op == 3: UIadmin.Menu_categoria()
            if op == 4: UIadmin.listar_vendas() 
            if op == 9: 
                print("DESLIGANDO...")
                return 9
    
    @staticmethod
    def Menu_principal():
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Menu Cliente")
        print("2 - Menu Produto")
        print("3 - Menu Categoria")
        print("4 - Listar Vendas") 
        print("9 - Sair")
        return UIadmin.Ler_Opcao()

    @staticmethod
    def listar_vendas():
        print("\n-- LISTA DE VENDAS (TODOS OS CLIENTES) --")
        vendas = View.listar_vendas()
        if not vendas:
            print("Nenhuma venda realizada ainda.")
        else:
            for v in vendas:
                print(v)
    
    # ==========================================
    # MENU E CRUD: CLIENTE
    # ==========================================
    @staticmethod
    def Menu_cliente():
        while True:
            print("\n=== MENU CLIENTE ===")
            print("1 - Inserir")
            print("2 - Excluir")
            print("3 - Listar")
            print("4 - Atualizar")
            print("9 - Voltar")
            op = UIadmin.Ler_Opcao()
            if op == 1: UIadmin.inserir_cliente()
            if op == 2: UIadmin.excluir_cliente()
            if op == 3: UIadmin.listar_cliente()
            if op == 4: UIadmin.atualizar_cliente()
            if op == 9: break

    @staticmethod
    def inserir_cliente():
        print("\n-- INSERIR CLIENTE --")
        nome = input("Nome: ")
        email = input("E-mail: ")
        fone = input("Telefone: ")
        senha = input("Senha: ")
        View.inserir_cliente(nome, email, fone, senha)
        print("Cliente inserido com sucesso!")

    @staticmethod
    def listar_cliente():
        print("\n-- LISTA DE CLIENTES --")
        clientes = View.listar_cliente()
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for c in clientes:
                print(c)

    @staticmethod
    def excluir_cliente():
        UIadmin.listar_cliente()
        print("\n-- EXCLUIR CLIENTE --")
        id_cliente = int(input("Digite o ID do cliente a ser excluído: "))
        View.excluir_cliente(id_cliente)
        print("Cliente excluído com sucesso!")

    @staticmethod
    def atualizar_cliente():
        UIadmin.listar_cliente()
        print("\n-- ATUALIZAR CLIENTE --")
        id_cliente = int(input("Digite o ID do cliente a ser atualizado: "))
        nome = input("Novo Nome: ")
        email = input("Novo E-mail: ")
        fone = input("Novo Telefone: ")
        View.atualizar_cliente(id_cliente, nome, email, fone)
        print("Cliente atualizado com sucesso!")

    # ==========================================
    # MENU E CRUD: PRODUTO
    # ==========================================
    @staticmethod
    def Menu_produto():
        while True:
            print("\n=== MENU PRODUTO ===")
            print("1 - Inserir")
            print("2 - Excluir")
            print("3 - Listar")
            print("4 - Atualizar")
            print("5 - Reajustar Preços") 
            print("9 - Voltar")
            op = UIadmin.Ler_Opcao()
            if op == 1: UIadmin.inserir_produto()
            if op == 2: UIadmin.excluir_produto()
            if op == 3: UIadmin.listar_produto()
            if op == 4: UIadmin.atualizar_produto()
            if op == 5: UIadmin.reajustar_precos()
            if op == 9: break

    @staticmethod
    def inserir_produto():
        print("\n-- INSERIR PRODUTO --")
        desc = input("Descrição: ")
        preco = float(input("Preço: R$ "))
        estoque = int(input("Estoque: "))
        id_cat = int(input("ID da Categoria: "))
        View.inserir_produto(desc, preco, estoque, id_cat)
        print("Produto inserido com sucesso!")

    @staticmethod
    def listar_produto():
        print("\n-- LISTA DE PRODUTOS --")
        produtos = View.listar_produto()
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for p in produtos:
                print(p)

    @staticmethod
    def excluir_produto():
        UIadmin.listar_produto()
        print("\n-- EXCLUIR PRODUTO --")
        id_produto = int(input("Digite o ID do produto a ser excluído: "))
        View.excluir_produto(id_produto)
        print("Produto excluído com sucesso!")

    @staticmethod
    def atualizar_produto():
        UIadmin.listar_produto()
        print("\n-- ATUALIZAR PRODUTO --")
        id_produto = int(input("Digite o ID do produto a ser atualizado: "))
        desc = input("Nova Descrição: ")
        preco = float(input("Novo Preço: R$ "))
        estoque = int(input("Novo Estoque: "))
        id_cat = int(input("Novo ID da Categoria: "))
        View.atualizar_produto(id_produto, desc, preco, estoque, id_cat)
        print("Produto atualizado com sucesso!")

    @staticmethod
    def reajustar_precos():
        print("\n-- REAJUSTAR PREÇOS --")
        try:
            percentual = float(input("Digite o percentual de reajuste (ex: 10 para 10%): "))
            View.reajustar_preco(percentual)
            print("Preços reajustados com sucesso!")
        except ValueError:
            print("Valor inválido inserido!")

    # ==========================================
    # MENU E CRUD: CATEGORIA
    # ==========================================
    @staticmethod
    def Menu_categoria():
        while True: 
            print("\n=== MENU CATEGORIA ===")
            print("1 - Inserir")
            print("2 - Excluir")
            print("3 - Listar")
            print("4 - Atualizar")
            print("9 - Voltar")
            op = UIadmin.Ler_Opcao()
            if op == 1: UIadmin.inserir_categoria()
            if op == 2: UIadmin.excluir_categoria()
            if op == 3: UIadmin.listar_categoria()
            if op == 4: UIadmin.atualizar_categoria()
            if op == 9: break

    @staticmethod
    def inserir_categoria():
        print("\n-- INSERIR CATEGORIA --")
        desc = input("Descrição da categoria: ")
        View.inserir_categoria(desc)
        print("Categoria inserida com sucesso!")

    @staticmethod
    def listar_categoria():
        print("\n-- LISTA DE CATEGORIAS --")
        categorias = View.listar_categoria()
        if not categorias:
            print("Nenhuma categoria cadastrada.")
        else:
            for c in categorias:
                print(c)

    @staticmethod
    def excluir_categoria():
        UIadmin.listar_categoria()
        print("\n-- EXCLUIR CATEGORIA --")
        id_cat = int(input("Digite o ID da categoria a ser excluída: "))
        View.excluir_categoria(id_cat)
        print("Categoria excluída com sucesso!")

    @staticmethod
    def atualizar_categoria():
        UIadmin.listar_categoria()
        print("\n-- ATUALIZAR CATEGORIA --")
        id_cat = int(input("Digite o ID da categoria a ser atualizada: "))
        desc = input("Nova Descrição: ")
        View.atualizar_categoria(id_cat, desc)
        print("Categoria atualizada com sucesso!")