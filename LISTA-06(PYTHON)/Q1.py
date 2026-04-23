import json

class Cliente :
    def __init__(self, id, n, e, f) :
        self.setID(id)
        self.setNome(n)
        self.setEmail(e)
        self.setFone(f)

    def setID(self, v) :
        if v >= 0 : self.id = v
        else : raise ValueError("ID INVÁLIDO")
    def setNome(self, v) :
        self.nome = v
    def setEmail(self, v) :
        self.email = v
    def setFone(self, v) :
        self.fone = v
    
    def getID(self) :
        return self.id
    def getNome(self) :
        return self.nome
    def getEmail(self) :
        return self.email
    def getFone(self) :
        return self.fone
    def __str__(self) :
        return f"Cliente: ID-{self.id}, NOME-{self.nome}, EMAIL-{self.email}, FONE-{self.fone}"

class ClienteDAO :
    def __init__(self):
        self.objetos = []
    def Inserir(self, obj) :
        self.Abrir()
        self.objetos.append(obj)
        self.Salvar()
    def Listar(self) :
        self.Abrir()
        return self.objetos
    def Salvar(self) :
        with open("clientes.json", mode = "w") as arquivo :
            json.dump(self.objetos, arquivo, default = vars)
    def Abrir(self) :
        self.objetos = []
        try :
            with open("clientes.json", mode = "r") as arquivo :
                clientes_json = json.load(arquivo)
                for obj in clientes_json :
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                    self.objetos.append(c)
        except FileNotFoundError :
            self.objetos = []
    def Listar_ID(self, v) :
        self.Abrir()
        for id in self.objetos :
            if id.getID() == v :
                return id
            else : None
    def Excluir(self, id) :
        self.Abrir()
        x = self.Listar_ID(id)
        if x is not None :
            self.objetos.remove(x)
            self.Salvar()
            return True
        else : return False
    def Atualizar(self, id) :
        self.Abrir()
        x = self.Listar_ID(id.getID())
        if x is not None :
            x.setNome(id.getNome())
            x.setEmail(id.getEmail())
            x.setFone(id.getFone())
            self.Salvar()
            return True
        else : return False
class UI:
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.listar_id()
            if op == 4: UI.excluir()
            if op == 5: UI.atualizar()
    @staticmethod
    def menu():
        print("1-Inserir 2-Listar 3-Listar_ID 4-Excluir 5-Atualizar 9-Fim")
        return int(input("Informe uma opção: "))
    
    @staticmethod
    def inserir():
        print("Cadastro de Clientes")
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o fone: ")
        c = Cliente(id, nome, email, fone)
        ClienteDAO().Inserir(c)
    
    @staticmethod
    def listar():
        print("----LISTAGEM DE CLIENTES----")
        for c in ClienteDAO().Listar(): print(c)
    
    @staticmethod
    def listar_id():
        print("----SCANNER DE ID----")
        id_procurado = int(input("Digite o id que deseja procurar: "))
        cliente = ClienteDAO()
        procurar = cliente.Listar_ID(id_procurado)
        if procurar is None :
            print("Cliente com este ID não encontrado!")
        else :
            print(f"Cliente com este ID encontrado! \n{procurar}")
    
    @staticmethod
    def excluir():
        print("----EXCLUSÃO DE CLIENTE----")
        id = int(input("Digite o ID do cliente que deseja excluir: "))
        DAO = ClienteDAO()
        procurar = DAO.Excluir(id)
        if procurar == True : print("Excluído com sucesso!")
        else : ("ID não encontrado!")
    
    @staticmethod
    def atualizar():
        print("----ATUALIZAÇÃO DE DADOS PESSOAIS----")
        id = int(input("Digite o ID do cliente que deseja alterar: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o  novo email: ")
        fone = input("Informe o novo fone: ")
        c = Cliente(id, nome, email, fone)
        ClienteDAO().Atualizar(c)
        print("Atualização Completa!")

UI.main()