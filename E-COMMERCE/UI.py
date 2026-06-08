from TEMPLATES.UI_admin import UIadmin
from TEMPLATES.UI_cliente import UIcliente
from Views import View


class UI:
    __user = None # Cria uma varável da própria classe UI, uma variável que armazena os dados do usuário

    @classmethod # Usa o classmethod para poder usar o atributo da prórpia classe UI
    def main(cls):
        View.cria_admin() # Chama o método Cria_admin da View, que vai criar um admin caso não houver um
        cls.menu()  # Após isso, chama método menu
    
    @classmethod
    def menu(cls):
        op = 0
        while op != 9:
            if cls.__user is None: # Se a variável é none, então não tem ninguém logado
                op = cls.menu_visitante() # Se não tem ninguém logado, op chama o método do menu_visitante
            else:
                print("\nIF | COMÉRCIO ELETRÔNICO 2026.1")
                print("BEM VINDO(A), " + cls.__user["nome"])

                admin = cls.__user["nome"] == "admin" # Cria uma varável admin que retorna True para "admin" e False para "não admin" 
                if admin:
                    if UIadmin.Main() == 9: UI.usuario_sair() # Se admin é True, chama o método UIadmin
                else:
                    if UIcliente.Main(cls.__user["id"]) == 9: UI.usuario_sair() # Se admin é False, chama o método UIcliente 
    
    @staticmethod # É um método estático pois ele não mexe com o atributo da classe, ele faz isso por meio das classes interiores
    def menu_visitante():
        print("="*40)
        print(" "*12, "MENU VISITANTE")
        print("="*40, "\n")
        print("1 - ENTRAR   2 - CRIAR CONTA   9 - EXIT\n")
        op = int(input("ESCOLHA UMA OPÇÃO: "))
        if op == 1: UI.usuario_entrar() # Chama o usuário_entrar
        if op == 2: UI.usuario_criar_conta() # Chama o usuário_criar_conta
        return op # Retorna op, isso só acontece se o op for = 9. Se for 1 ou 2, o while do menu principal continua rodando
    
    @classmethod
    def usuario_entrar(cls):
        email = input("INFORME SEU EMAIL: ")
        senha = input("INFORME SUA SENHA: ") # Usuário coloca email e senha
        cls.__user = View.usuario_autenticar(email, senha) # Método chama outro método do view para autenticar o usuário, se é válido
        if cls.__user is None: print("\nEMAIL OU SENHA INVÁLIDO(S)!\n") # Se o atributo continua None, então ele retorna um aviso de erro
    
    @classmethod
    def usuario_sair(cls):
        cls.__user = None # Esvaziar o atributo é igual a deslogar do usuário

    @classmethod
    def usuario_criar_conta(cls):
        print("="*40)
        print(" "*12, "CRIAÇÃO DE CONTA")
        print("="*40, "\n")
        nome  = input(" INFORME O SEU NOME: ")
        email = input(" INFORME UM EMAIL: ")
        fone  = input(" INFORME UM TELEFONE PARA CONTATO: ")
        senha = input(" INFORME SUA SENHA: ") # Preenche todas as informações para criar o cliente

        View.inserir_cliente(nome, email, fone, senha) # Chama o método de inserir_cliente da View
        print("\nCONTA CRIADA COM SUCESSO!\nEFETUE LOGIN PARA ENTRAR NO SISTEMA.")

from UI import UI

if __name__ == "__main__":
    UI.main()