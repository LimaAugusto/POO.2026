from Views import View

class UIcliente:
    @staticmethod
    def Ler_Opcao():
        try:
            return int(input("ESCOLHA UMA OPÇÃO: "))
        except ValueError:
            return -1
        
    @staticmethod
    def Main(id_cliente):
        while True:
            print("="*40)
            print(" "*12, "MENU")
            print("="*40, "\n")
            print(" "*12, "1 -- Listar produtos")
            print(" "*12, "2 -- Inserir produto no carrinho")
            print(" "*12, "3 -- Visualizar carrinho")
            print(" "*12, "4 -- Limpar carrinho")
            print(" "*12, "5 -- Comprar carrinho")
            print(" "*12, "9 -- Sair\n")
            print("="*40)
            op = UIcliente.Ler_Opcao()
            if op == 1: UIcliente.Listar_produtos()
            if op == 2: UIcliente.Inserir_produto_carrinho(id_cliente)
            if op == 3: UIcliente.Visualizar_carrinho(id_cliente)
            if op == 4: UIcliente.Limpar_carrinho(id_cliente)
            if op == 5: UIcliente.Comprar_carrinho(id_cliente)
            if op == 9:
                print("SAINDO...")
                return 9

    @staticmethod
    def Listar_produtos():
        print("="*40)
        print(" "*12, "LISTA DE PRODUTOS")
        print("="*40, "\n")
        produtos = View.listar_produto()
        if not produtos:
            print("NENHUM PRODUTO CADASTRADO!\n")
        for p in produtos:
            print(p)
    
    @staticmethod
    def Inserir_produto_carrinho(id_cliente):
        UIcliente.Listar_produtos()
        print("="*40)
        print(" "*10, "INSERINDO UM PRODUTO")
        print("="*40, "\n")
        id_produto = int(input("INSIRA O ID DO PRODUTO DESEJADO: "))
        qtd = int(input("INSIRA A QUANTIDADE DESEJADA: "))
        item = View.inserir_produto_carrinho(qtd, id_produto, id_cliente)
        if item == True: print("PRODUTO INSERIDO COM SUCESSO!\n")
        else: print("PRODUTO NÃO ENCONTRADO!\n")

    @staticmethod
    def Visualizar_carrinho(id_cliente):
        itens = View.visualizar_carrinho(id_cliente)
        print("="*40)
        print(" "*12, "LISTA DO SEU CARRINHO")
        print("="*40, "\n")
        for item in itens:
            print(item)
        print("="*40, "\n")

    @staticmethod
    def Limpar_carrinho(id_cliente):
        carrinho = View.limpar_carrinho(id_cliente)
        print("CARRINHO LIMPO!\n")

    @staticmethod
    def Comprar_carrinho(id_cliente):
        carrinho = View.comprar_carrinho(id_cliente)
        if carrinho == True:
            print("COMPRA REALZIADA, AGRADECEMOS A PREFERÊNCIA!\n")
        else: print("CRRINHO ESTÁ VAZIO!")