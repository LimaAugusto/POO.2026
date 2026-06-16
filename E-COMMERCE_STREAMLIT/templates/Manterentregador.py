import streamlit as st
import pandas as pd
from Views import View
import time

class ManterEntregadorUI:
    def main():
        st.header("ENTREGADORES")
        tab1, tab2, tab3 = st.tabs(["LISTAR", "INSERIR", "EXCLUIR"])
        with tab1: ManterEntregadorUI.Listar()
        with tab2: ManterEntregadorUI.Inserir()
        with tab3: ManterEntregadorUI.Excluir()

    def Listar():
        entregadores = View.listar_entregador()
        if len(entregadores) == 0:
            st.write("NENHUM ENTREGADOR CADASTRADO!")
            return
        list_dic = [{"id": e.getId(), "nome": e.getNome(), "email": e.getEmail(), "fone": e.getFone()} for e in entregadores]
        df = pd.DataFrame(list_dic)
        st.dataframe(df, hide_index = True)

    def Inserir():
        nome = st.text_input("NOME")
        email = st.text_input("E-MAIL")
        fone = st.text_input("TELEFONE")
        senha = st.text_input("SENHA", type = "password")
        if st.button("INSERIR"):
            try:
                View.inserir_entregador(nome, email, fone, senha)
                st.success("ENTREGADOR CADASTRADO!")
            except Exception as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def Excluir():
        entregadores = View.listar_entregador()
        if len(entregadores) == 0:
            st.write("NENHUM ENTREGADOR CADASTRADO!")
            return
        op = st.selectbox("ENTREGADOR", entregadores)
        if st.button("EXCLUIR"):
            try:
                View.excluir_entregador(op.getId())
                st.success("ENTREGADOR EXCLUÍDO!")
            except Exception as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()
