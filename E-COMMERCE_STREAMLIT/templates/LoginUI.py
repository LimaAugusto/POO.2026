import streamlit as st
import time
from Views import View

class LoginUI:
    def sistema_entrar():
        st.header("ENTRAR NO SISTEMA")
        email = st.text_input("E-MAIL")
        senha = st.text_input("SENHA", type="password")
        if st.button("ENTRAR"):
            try:
                c = View.usuario_autenticar(email, senha)
                if c == None: st.write("E-MAIL OU SENHA INVÁLIDO(S)!")
                else:
                    st.session_state["cliente_id"] = c["id"]
                    st.session_state["cliente_nome"] = c["nome"]
            except Exception as erro:
                st.error(erro)
                time.sleep(2)    
                st.rerun()
        
    def abrir_conta():
        st.header("CADASTRO")
        nome = st.text_input("NOME")
        email = st.text_input("E-MAIL")
        fone = st.number_input("TELEFONE")
        senha = st.text_input("SENHA")
        if st.button("CRIAR"):
            try:
                c = View.inserir_cliente(nome, email, fone, senha)
                st.session_state["cliente_id"] = c["id"]
                st.session_state["cliente_nome"] = c["nome"]
                st.success("CLIENTE INSERIDO!")
            except Exception as erro:
                st.error(erro) 
                time.sleep(2)
                st.rerun()

    def entrar_entregador():
        st.header("ENTRAR COMO ENTREGADOR")
        email = st.text_input("E-MAIL")
        senha = st.text_input("SENHA", type = "password")
        if st.button("ENTRAR"):
            try:
                e = View.autenticar_entregador(email, senha)
                if e is None:
                    st.error("E-MAIL OU SENHA INVÁLIDO(S)!")
                else:
                    st.session_state["entregador_id"] = e["id"]
                    st.session_state["entregador_nome"] = e["nome"]
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)

    def cadastrar_entregador():
        st.header("CADASTRO DE ENTREGADOR")
        nome = st.text_input("NOME")
        email = st.text_input("E-MAIL")
        fone = st.text_input("TELEFONE")
        senha = st.text_input("SENHA", type = "password")
        if st.button("CADASTRAR"):
            try:
                e = View.inserir_entregador(nome, email, fone, senha)
                st.session_state["entregador_id"] = e["id"]
                st.session_state["entregador_nome"] = e["nome"]
                st.success("ENTREGADOR CADASTRADO!")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)