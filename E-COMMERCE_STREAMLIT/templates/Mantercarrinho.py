import streamlit as st
import pandas as pd
from Views import View
import time
from datetime import datetime

class ManterCarrinhoUI:
    def main():
        st.header("LOJA")
        tab1 = st.tabs("LISTAR PRODUTOS")
        with tab1: ManterCarrinhoUI.Listar_produtos()
        # with tab2: pass
        # with tab3: pass
        # with tab4: pass
        # with tab5: pass

    def Listar_produtos():
        produtos = View.listar_produto()
        if len(produtos) == 0: st.write("NENHUM PRODUTO CADASTRADO!")
        else:
            list_dic = []
            for obj in produtos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index = True, column_order = ["id", "desc", "preco", "estoque", "id_categoria"])

    # def Inserir_produtos():
    #     c = View.listar_cliente(st.session_state["cliente_id"])
    #     produtos = View.listar_produto()
    #     if len(produtos) == 0: st.write("NENHUM PRODUTO CADASTRADO!")
    #     else:
    #         op = st.selectbox("INSERÇÃO DE PRODUTOS", produtos)
    #         quantidade = st.text_input("QUANTIDADE")
    #         if st.button("INSERIR"):
    #             id_produto = op.getId()
    #             id_cliente = c.getId()
    #             try: 
    #                 View.inserir_produto_carrinho(quantidade, id_produto, id_cliente)
    #                 st.success("PRODUTO ADICIONADO!")
    #             except Exception as erro:
    #                 st.error(erro)
    #             time.sleep(2)
    #             st.rerun()





        # def inserir_produto_carrinho(quantidade, id_produto, id_cliente):
        # produto = ProdutoDAO().listar_id(id_produto)
        # if produto is None: 
        #     return False
        # item = Carrinho(id = 0, desc = produto.getDesc(), qtd = quantidade, id_produto = id_produto, id_cliente = id_cliente)
        # CarrinhoDAO().Inserir_produto(item)
        # return True