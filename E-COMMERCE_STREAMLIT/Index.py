from templates.Mantercliente import ManterClienteUI
from templates.Mantercategoria import ManterCategoriaUI
from templates.Manterproduto import ManterProdutoUI
from templates.Mantercarrinho import ManterCarrinhoUI
from templates.Mantervenda import ManterVendaUI
from templates.Reajustarproduto import ReajustarProdutoUI
from templates.Manterpromocao import ManterPromocaoUI
from templates.LoginUI import LoginUI
import streamlit as st
from Views import View

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("MENU", [
            "ENTRAR NO SISTEMA",
            "ABRIR CONTA"])
        if op == "ENTRAR NO SISTEMA": LoginUI.sistema_entrar()
        if op == "ABRIR CONTA": LoginUI.abrir_conta()

    def menu_admin():
        op = st.sidebar.selectbox("MENU", [
            "CADASTRO DE CLIENTES",
            "CADASTRO DE PRODUTOS",
            "CADASTRO DE CATEGORIAS",
            "PROMOÇÕES",
            "REAJUSTAR PRODUTOS",
            "VENDAS"])
        if op == "CADASTRO DE CLIENTES": ManterClienteUI.main()
        if op == "CADASTRO DE PRODUTOS": ManterProdutoUI.main()
        if op == "CADASTRO DE CATEGORIAS": ManterCategoriaUI.main()
        if op == "PROMOÇÕES": ManterPromocaoUI.main()
        if op == "REAJUSTAR PRODUTOS": ReajustarProdutoUI.main()
        if op == "VENDAS": ManterVendaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("MENU", [
            "CARRINHO",])
        if op == "CARRINHO": ManterCarrinhoUI.main()

    def sidebar():
        if "cliente_id" not in st.session_state: IndexUI.menu_visitante()
        else:
            st.sidebar.write("BEM VINDO(A), " + st.session_state["cliente_nome"])
            admin = st.session_state["cliente_nome"] == "admin"
            if admin: IndexUI.menu_admin()
            else: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    def sair_do_sistema():
        if st.sidebar.button("SAIR"):
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            st.rerun()

    def main():
        View.cria_admin()
        IndexUI.sidebar()

IndexUI.main()