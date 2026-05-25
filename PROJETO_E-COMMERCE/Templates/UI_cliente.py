from Views import View

class UIcliente:

    @staticmethod
    def Ler_Opcao():
        try:
            return int(input("Escolha: "))
        except ValueError:
            return -1
        
    @staticmethod
    def Main(id_cliente):
        while True:
            print("1-Listar produtos")
            print("2-Inserir produto no carrinho")
            print("3-Visualizar carrinho")
            print("4-Comprar carrinho")
            print("5-Limpar minhas compras")
            print("9-Sair")
            op = UIcliente.Ler_Opcao()     
            if op == 1: UIcliente.Produto_listar()
            if op == 2: UIcliente.Carrinho_inserir_produto(id_cliente)
            if op == 3: UIcliente.Carrinho_visualizar(id_cliente)
            if op == 4: UIcliente.Carrinho_comprar(id_cliente)
            if op == 5: UIcliente.Carrinho_limpar(id_cliente)
            if op == 9: return 9

    @staticmethod
    def Produto_listar():
        produtos = View.listar_produto_carrinho()
        if not produtos:
            print("Nenhum produto cadastrado ou encontrado.")
        else:
            print("\n--- LISTA DE PRODUTOS ---")
            for p in produtos:
                print(p)
    
    @staticmethod
    def Carrinho_inserir_produto(id_cliente):
        UIcliente.Produto_listar()
        id_produto = int(input("Insira o ID do produto desejado >> "))
        quantidade = int(input("Insira a quantidade desejada deste produto >> "))
        if View.inserir_produto_carrinho(quantidade, id_produto, id_cliente): 
            print("ADICIONADO COM SUCESSO!")
        else: 
            print("PRODUTO NÃO ENCONTRADO!")
    
    @staticmethod
    def Carrinho_visualizar(id_cliente):
        print("\n--- ITENS DO SEU CARRINHO ---")
        # Pede à View apenas os itens que pertencem a este cliente
        itens = View.visualizar_carrinho(id_cliente)
        if len(itens) == 0:
            print("Carrinho vazio!")
        else:
            for item in itens:
                print(item)

    @staticmethod
    def Carrinho_comprar(id_cliente):
        if View.comprar_carrinho(id_cliente):
            print("Compra realizada com sucesso!")
        else:
            print("Carrinho vazio!")
    
    @staticmethod
    def Carrinho_limpar(id_cliente):
        View.limpar_carrinho(id_cliente)
        print("Carrinho limpo!")