import streamlit as st
import pandas as pd
from Views import View
import time

class ManterClienteUI:
    def main():
        st.header("CADASTRO DE CLIENTES")
        tab1, tab2, tab3, tab4 = st.tabs(["LISTAR", "INSERIR", "ATUALIZAR", "EXCLUIR"])
        with tab1: ManterClienteUI.Listar()
        with tab2: ManterClienteUI.Inserir()
        with tab3: ManterClienteUI.Atualizar()
        with tab4: ManterClienteUI.Excluir()

    def Listar():
        clientes = View.listar_cliente()
        if len(clientes) == 0: st.write ("NENHUM CLIENTE CADASTRADO!")
        else:
            list_dic = []
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index = True, column_order = ["id", "nome", "email", "fone"])

    def Inserir():
        nome = st.text_input("DIGITE SEU NOME")
        email = st.text_input("DIGITE SEU EMAIL")
        fone = st.text_input("DIGITE SEU TELEFONE")
        senha = st.text_input("DIGITE UMA SENHA", type = "password")
        if st.button("INSERIR"):
            try:
                View.inserir_cliente(nome, email, fone, senha)
                st.success("CLIENTE INSRIDO COM SUCESSO!")
            except Exception as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def Atualizar():
        clientes = View.listar_cliente()
        if len(clientes) == 0: st.write("NENHUM CLIENTE CADASTRADO!")
        else:
            op = st.selectbox("ATUALIZAÇÃO DE CLIENTES", clientes)
            nome = st.text_input("INFORME SEU NOVO NOME", op.getNome())
            email = st.text_input("INFORME SEU NOVO EMAIL", op.getEmail())
            fone = st.text_input("INFORME SEU NOVO TELEFONE", op.getFone())
            senha = st.text_input("INFORME SUA NOVA SENHA", op.getSenha(), type="password")
            if st.button("ATUALIZAR"):
                    id = op.getId()
                    try: 
                        View.atualizar_cliente(id, nome, email, fone, senha)
                        st.success("CLIENTE ATUALIZADO!")
                    except Exception as erro:
                        st.error(erro)
                    time.sleep(2)
                    st.rerun()

    def Excluir():
        clientes = View.listar_cliente()
        if len(clientes) == 0: st.write("NENHUM CLIENTE CADASTRADO!")
        else:
            op = st.selectbox("EXCLUSÃO DE CLIENTES", clientes)
            if st.button("EXCLUIR"):
                id = op.getId()
                try: 
                    View.excluir_cliente(id)
                    st.success("CLIENTE EXCLUÍDO!")
                except Exception as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()