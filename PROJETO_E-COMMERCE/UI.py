from Templates.UI_admin import UIadmin
from Templates.UI_cliente import UIcliente
from Views import View

class UI:
    __usuario = None     

    def menu_visitante():
        print("1-Entrar no Sistema, 2-Abrir Conta, 9-Fim")
        op = int(input("Informe uma opção: "))           
        if op == 1: UI.visitante_entrar()
        if op == 2: UI.visitante_criar_conta()
        return op

    @classmethod
    def main(cls):
        View.verifica_cria_admin()
        UI.menu()
        
    @classmethod
    def menu(cls):
        op = 0
        while op != 9:
            if cls.__usuario == None: 
                # usuário não está logado
                op = UI.menu_visitante()
            else:
                # usuário está logado, verifica se é o admin
                admin = cls.__usuario["nome"] == "admin"
                # mensagem de bem-vindo
                print("IF Comércio Eletrônico 2026.1")
                print("Bem-vindo(a), " + cls.__usuario["nome"])
                # menu do usuário: admin ou cliente
                if admin: 
                    if UIadmin.Main() == 9: UI.usuario_sair()
                else: 
                    if UIcliente.Main() == 9: UI.usuario_sair()

    @classmethod
    def visitante_entrar(cls):
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")
        cls.__usuario = View.cliente_autenticar(email, senha)
        if cls.__usuario == None: print("Usuário ou senha inválidos")

    @classmethod
    def visitante_criar_conta(cls):
        print("\n=== ABRIR CONTA ===")
        nome = input("Informe o seu nome: ")
        email = input("Informe o seu e-mail: ")
        fone = input("Informe o seu telefone: ")
        senha = input("Crie uma senha: ")
        
        
        View.inserir_cliente(nome, email, fone, senha)
        print("Conta criada com sucesso! Faça o login para entrar no sistema.")

    @classmethod
    def usuario_sair(cls):
        cls.__usuario = None

from UI import UI

if __name__ == "__main__":
    UI.main()