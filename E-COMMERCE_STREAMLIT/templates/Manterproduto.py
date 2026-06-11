import streamlit as st
import pandas as pd
from Views import View
import time

class ManterProdutoUI:
    def main():
        st.header("CADASTRO DE PRODUTOS")
        tab1, tab2, tab3, tab4 = st.tabs(["LISTAR", "INSERIR", "ATUALIZAR", "EXCLUIR"])
        with tab1: ManterProdutoUI.Listar()
        with tab2: ManterProdutoUI.Inserir()
        with tab3: ManterProdutoUI.Atualizar()
        with tab4: ManterProdutoUI.Excluir()

    def Listar():
        produtos = View.listar_produto()
        if len(produtos) == 0: st.write("NENHUM PRODUTO CADASTRADO!")
        else:
            list_dic = []
            for obj in produtos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index = True, column_order = ["id", "desc", "preco", "estoque", "id_categoria"])

    def Inserir():
        descricao = st.text_input("INFORME A DESCRIÇÃO")
        preco = float(st.text_input("INFORME O PREÇO"))
        estoque = int(st.text_input("INFORME A QUANTIDADE NO ESTOQUE"))
        id_categoria = int(st.text_input("INFORME O ID DA CATEGORIA"))
        if st.button("INSERIR"):
            try:
                View.inserir_produto(descricao, preco, estoque, id_categoria)
                st.success("PRODUTO INSERIDO")
            except Exception as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def Atualizar():
        produtos = View.listar_produto()
        if len(produtos) == 0: st.write("NENHUM PRODUTO CADASTRADO!")
        else:
            op = st.selectbox("ATUALIZAÇÃO DE PRODUTOS", produtos)
            descricao = st.text_input("INFORME SUA NOVA DESCRIÇÃO", op.getDesc())
            preco = float(st.text_input("INFORME SEU NOVO PREÇO", op.getPreco()))
            estoque = int(st.text_input("INFORME A NOVA QUANTIDADE NO ESTOQUE", op.getEstoque()))
            id_categoria = int(st.text_input("INFORME O NOVO OU MESMO ID DA CATEGORIA", op.getId_Categoria()))
            if st.button("ATUALIZAR"):
                    id = op.getId()
                    try: 
                        View.atualizar_produto(id, descricao, preco, estoque, id_categoria)
                        st.success("PRODUTO ATUALIZADO!")
                    except Exception as erro:
                        st.error(erro)
                    time.sleep(2)
                    st.rerun()

    def Excluir():
        produtos = View.listar_produto()
        if len(produtos) == 0: st.write("NENHUM PRODUTO CADASTRADO!")
        else:
            op = st.selectbox("EXCLUSÃO DE PRODUTOS", produtos)
            if st.button("EXCLUIR"):
                id = op.getId()
                try: 
                    View.excluir_produto(id)
                    st.success("PRODUTO EXCLUÍDO!")
                except Exception as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()