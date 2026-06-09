import streamlit as st
import pandas as pd
from Views import View
import time

class ManterCategoriaUI:
    def main():
        st.header("CADASTRO DE CATEGORIAS")
        tab1, tab2, tab3, tab4 = st.tabs(["LISTAR", "INSERIR", "ATUALIZAR", "EXCLUIR"])
        with tab1: ManterCategoriaUI.Listar()
        with tab2: ManterCategoriaUI.Inserir()
        with tab3: ManterCategoriaUI.Atualizar()
        with tab4: ManterCategoriaUI.Excluir()

    def Listar():
        categorias = View.listar_categoria()
        if len(categorias) == 0: st.write("NENHUMA CATEGORIA CADASTRADA!")
        else:
            list_dic = []
            for obj in categorias: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index = True, column_order = ["id", "desc"])

    def Inserir():
        descricao = st.text_input("INFORME A DESCRIÇÃO")
        if st.button("INSERIR"):
            try:
                View.listar_categoria(descricao)
                st.success("CATEGORIA INSERIDA")
            except Exception as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def Atualizar():
        categorias = View.listar_categoria()
        if len(categorias) == 0: st.write("NENHUMA CATEGORIA CADASTRADA!")
        else:
            op = st.selectbox("ATUALIZAÇÃO DE CATEGORIAS", categorias)
            descricao = st.text_input("INFORME SUA NOVA DESCRIÇÃO", op.getDesc())
            if st.button("ATUALIZAR"):
                    id = op.getId()
                    try: 
                        View.atualizar_categoria(id, descricao)
                        st.success("CATEGORIA ATUALIZADA!")
                    except Exception as erro:
                        st.error(erro)
                    time.sleep(2)
                    st.rerun()

    def Excluir():
        categorias = View.listar_categoria()
        if len(categorias) == 0: st.write("NENHUM CATEGORIA CADASTRADA!")
        else:
            op = st.selectbox("EXCLUSÃO DE CATEGORIAS", categorias)
            if st.button("EXCLUIR"):
                id = op.getId()
                try: 
                    View.excluir_categoria(id)
                    st.success("CATEGORIA EXCLUÍDO!")
                except Exception as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()