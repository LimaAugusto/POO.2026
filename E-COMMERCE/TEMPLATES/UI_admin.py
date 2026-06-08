from Views import View

class UIadmin:
    @staticmethod
    def Ler_Opcao():
        try:
            return int(input("ESCOLHA UMA OPÇÃO: "))
        except ValueError:
            return -1
        
    @staticmethod
    def Main():
        while True:
            op = UIadmin.Menu_principal()
            if op == 1: UIadmin.Menu_cliente()
            if op == 2: UIadmin.Menu_categoria()
            if op == 3: UIadmin.Menu_produto()
            if op == 4: UIadmin.Listar_vendas()
            if op == 9:
                print("SAINDO...")
                return 9

    @staticmethod
    def Menu_principal():
        print("="*40)
        print(" "*12, "MENU PRINCIPAL")
        print("="*40, "\n")
        print(" "*10, "1 -- MENU CLIENTE")
        print(" "*10, "2 -- MENU CATEGORIA")
        print(" "*10, "3 -- MENU PRODUTO")
        print(" "*10, "4 -- LISTAR VENDAS")
        print(" "*10, "9 -- RETORNAR\n")
        print("="*40)
        return UIadmin.Ler_Opcao()
    
    # ==========================================
    #          MENU E CRUD: CLIENTE
    # ==========================================

    @staticmethod
    def Menu_cliente():
        print("="*40)
        print(" "*12, "MENU CLIENTE")
        print("="*40, "\n")
        print(" "*10, "1 -- INSERIR CLIENTE")
        print(" "*10, "2 -- LISTAR CLIENTES")
        print(" "*10, "3 -- ATUALIZAR CLIENTE")
        print(" "*10, "4 -- EXCLUIR CLIENTE")
        print(" "*10, "9 -- RETORNAR\n")
        print("="*40)
        while True:
            op = UIadmin.Ler_Opcao()
            if op == 1: UIadmin.Inserir_cliente()
            if op == 2: UIadmin.Listar_cliente()
            if op == 3: UIadmin.Atualizar_cliente()
            if op == 4: UIadmin.Excluir_cliente()
            if op == 9: break

    @staticmethod
    def Inserir_cliente():
        print("="*40)
        print(" "*10, "INSERINDO CLIENTE NOVO")
        print("="*40, "\n")
        nome = input("INSIRA SEU NOME: ")
        email = input("INSIRA UM EMAIL: ")
        fone = input("INSIRA SEU TELEFONE: ")
        senha = input("INSIRA UMA SENHA: ")
        View.inserir_cliente(nome, email, fone, senha)
        print("\nCLIENTE INSERIDO COM SUCESSO!")

    @staticmethod
    def Listar_cliente():
        print("="*40)
        print(" "*12, "LISTA DE CLIENTES")
        print("="*40, "\n")
        clientes = View.listar_cliente()
        if not clientes:
            print("NENHUM CLIENTE CADASTRADO!")
        for c in clientes:
            print(c)
        print("\n")

    @staticmethod
    def Atualizar_cliente():
        UIadmin.Listar_cliente()
        print("="*40)
        print(" "*11, "ATUALIZANDO CLIENTE")
        print("="*40, "\n")
        id_cliente = int(input("INSIRA O ID DO CLIENTE DESEJADO: "))
        nome = input("INSIRA SEU NOVO NOME: ")
        email = input("INSIRA UM NOVO EMAIL: ")
        fone = input("INSIRA SEU NOVO TELEFONE: ")
        senha = input("INSIRA UMA NOVA SENHA: ")
        new = View.atualizar_cliente(id_cliente, nome, email, fone, senha)
        if new == True:
            print("\nCLIENTE ATUALIZADO COM SUCESSO!")
        else:
            print("\nALGO DEU ERRADO!")

    @staticmethod
    def Excluir_cliente():
        UIadmin.Listar_cliente()
        print("="*40)
        print(" "*12, "EXCLUINDO CLIENTE")
        print("="*40, "\n")
        id_cliente = int(input("INSIRA O ID DO CLIENTE À SER EXCLUÍDO: "))
        ex = View.excluir_cliente(id_cliente)
        if ex == False:
            print("\nALGO DEU ERRADO!")
        print("\nCLIENTE EXCLUÍDO COM SUCESSO!")
            
    # ==========================================
    #           MENU E CRUD: CATEGORIA
    # ==========================================
    
    @staticmethod
    def Menu_categoria():
        print("="*40)
        print(" "*12, "MENU CATEGORIA")
        print("="*40, "\n")
        print(" "*10, "1 -- INSERIR CATEGORIA")
        print(" "*10, "2 -- LISTAR CATEGORIAS")
        print(" "*10, "3 -- ATUALIZAR CATEGORIA")
        print(" "*10, "4 -- EXCLUIR CATEGORIA")
        print(" "*10, "9 -- RETORNAR\n")
        print("="*40)
        while True:
            op = UIadmin.Ler_Opcao()
            if op == 1: UIadmin.Inserir_categoria()
            if op == 2: UIadmin.Listar_categoria()
            if op == 3: UIadmin.Atualizar_categoria()
            if op == 4: UIadmin.Excluir_categoria()
            if op == 9: break

    @staticmethod
    def Inserir_categoria():
        print("="*40)
        print(" "*10, "INSERINDO CATEGORIA NOVA")
        print("="*40, "\n")
        desc = input("INSIRA A DESCRIÇÃO: ")
        View.inserir_categoria(desc)
        print("\nCATEGORIA INSERIDA COM SUCESSO!")

    @staticmethod
    def Listar_categoria():
        print("="*40)
        print(" "*10, "LISTA DE CATEGORIAS")
        print("="*40, "\n")
        categorias = View.listar_categoria()
        if not categorias:
            print("\nNENHUMA CATEGORIA CADASTRADA!")
        for c in categorias:
            print(c)
        print("\n")

    @staticmethod
    def Atualizar_categoria():
        UIadmin.Listar_categoria()
        print("="*40)
        print(" "*10, "ATUALIZANDO CATEGORIA")
        print("="*40, "\n")
        id_categoria = int(input("INSIRA O ID DA CATEGORIA DESEJADA: "))
        desc = input("INSIRA UMA NOVA DESCRIÇÃO: ")
        new = View.atualizar_categoria(id_categoria, desc)
        if new:
            print("\nCATEGORIA ATUALIZADA COM SUCESSO!")
        else:
            print("\nALGO DEU ERRADO!")

    @staticmethod
    def Excluir_categoria():
        UIadmin.Listar_categoria()
        print("="*40)
        print(" "*12, "EXCLUINDO CATEGORIA")
        print("="*40, "\n")
        id_categoria = int(input("INSIRA O ID DA CATEGORIA À SER EXCLUÍDO: "))
        ex = View.excluir_categoria(id_categoria)
        if ex == False:
            print("\nALGO DEU ERRADO!")
        else: print("\nCATEGORIA EXCLUÍDA COM SUCESSO!")

    # ==========================================
    #          MENU E CRUD: PRODUTO
    # ==========================================

    @staticmethod
    def Menu_produto():
        print("="*40)
        print(" "*12, "MENU PRODUTO")
        print("="*40, "\n")
        print(" "*10, "1 -- INSERIR PRODUTO")
        print(" "*10, "2 -- LISTAR PRODUTOS")
        print(" "*10, "3 -- ATUALIZAR PRODUTO")
        print(" "*10, "4 -- EXCLUIR PRODUTO")
        print(" "*10, "5 -- REAJUSTAR PREÇOS")
        print(" "*10, "9 -- RETORNAR\n")
        print("="*40)
        while True:
            op = UIadmin.Ler_Opcao()
            if op == 1: UIadmin.Inserir_produto()
            if op == 2: UIadmin.Listar_produto()
            if op == 3: UIadmin.Atualizar_produto()
            if op == 4: UIadmin.Excluir_produto()
            if op == 5: UIadmin.Reajustar_preco()
            if op == 9: break

    @staticmethod
    def Inserir_produto():
        print("="*40)
        print(" "*10, "INSERINDO PRODUTO NOVO")
        print("="*40, "\n")
        desc = input("INSIRA A DESCRIÇÃO: ")
        preco = float(input("INSIRA O PREÇO BASE: "))
        estoque = int(input("INSIRA A QUANTIDADE ATUAL NO ESTOQUE: "))
        id_cat = int(input("INSIRA O ID DA CATEGORIA: "))
        View.inserir_produto(desc, preco, estoque, id_cat)
        print("\nPRODUTO INSERIDO COM SUCESSO!")
    
    @staticmethod
    def Listar_produto():
        print("="*40)
        print(" "*12, "LISTA DE PRODUTOS")
        print("="*40, "\n")
        produtos = View.listar_produto()
        if not produtos:
            print("\nNENHUM PRODUTO CADASTRADO!")
        for p in produtos:
            print(p)
        print("\n")

    @staticmethod
    def Atualizar_produto():
        UIadmin.Listar_produto()
        print("="*40)
        print(" "*10, "ATUALIZANDO PRODUTO")
        print("="*40, "\n")
        id_produto = int(input("INSIRA O ID DO PRODUTO DESEJADO: "))
        desc = input("INSIRA UMA NOVA DESCRIÇÃO: ")
        preco = float(input("INSIRA UM NOVO PREÇO: "))
        estoque = int(input("INSIRA A QUANTIDADE ATUAL NO ESTOQUE: "))
        id_cat = int(input("INSIRA O ID ATUAL DA CATEGORIA: "))
        new = View.atualizar_produto(id_produto, desc, preco, estoque, id_cat)
        if new:
           print("\nPRODUTO ATUALIZADO COM SUCESSO!")
        else:
            print("\nALGO DEU ERRADO!")

    @staticmethod
    def Excluir_produto():
        UIadmin.Listar_produto()
        print("="*40)
        print(" "*10, "EXCLUINDO PRODUTO")
        print("="*40, "\n")
        id_produto = int(input("INSIRA O ID DO PRODUTO À SER EXCLUÍDO: "))
        ex = View.excluir_produto(id_produto)
        if ex == False:
            print("\nALGO DEU ERRADO!")
        print("\nPRODUTO EXCLUÍDO COM SUCESSO!")

    @staticmethod
    def Reajustar_preco():
        UIadmin.Listar_produto()
        print("="*40)
        print(" "*10, "REAJUSTAR PREÇOS")
        print("="*40, "\n")
        try:
            percentual = float(input("DIGITE O PERCENTUAL DE REAJUSTE (EX: 10 PARA 10%): "))
            View.reajustar_preco(percentual)
            print("PREÇOS REAJUSTADOS!")
        except ValueError:
            print("VALOR INSERIDO É INVÁLIDO!")