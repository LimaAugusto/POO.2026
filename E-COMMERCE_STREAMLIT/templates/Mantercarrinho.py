import streamlit as st
import pandas as pd
from Views import View
import time
import base64
 
class ManterCarrinhoUI:
    def main():
        st.header("LOJA")
        tab1, tab2, tab3 = st.tabs(["LOJA", "MEU CARRINHO", "MINHAS COMPRAS"])
        with tab1: ManterCarrinhoUI.Loja()
        with tab2: ManterCarrinhoUI.MeuCarrinho()
        with tab3: ManterCarrinhoUI.MinhasCompras()
 
    #----- ABA LOJA (LISTAR + INSERIR NO CARRINHO) -----
 
    def Loja():
        produtos = View.listar_produto()
        if len(produtos) == 0:
            st.write("NENHUM PRODUTO CADASTRADO!")
            return
 
        # LISTAGEM COM IMAGEM
        for obj in produtos:
            col1, col2 = st.columns([1, 3])
            with col1:
                if obj.getImagem():
                    img_bytes = base64.b64decode(obj.getImagem())
                    st.image(img_bytes, use_container_width = True)
                else:
                    st.write("SEM IMAGEM")
            with col2:
                st.write(f"**{obj.getDesc()}**")
                st.write(f"PREÇO: R$ {obj.getPreco():.2f}")
                st.write(f"ESTOQUE: {obj.getEstoque()}")
            st.divider()
 
        st.subheader("ADICIONAR AO CARRINHO")
        op = st.selectbox("PRODUTO", produtos)
        quantidade = int(st.number_input("QUANTIDADE", min_value = 1, step = 1, value = 1))
 
        if st.button("ADICIONAR"):
            id_produto = op.getId()
            id_cliente = st.session_state["cliente_id"]
            try:
                if quantidade > op.getEstoque():
                    st.error("QUANTIDADE INDISPONÍVEL EM ESTOQUE!")
                else:
                    View.inserir_produto_carrinho(quantidade, id_produto, id_cliente)
                    st.success("PRODUTO ADICIONADO AO CARRINHO!")
            except Exception as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()
 
    #----- ABA MEU CARRINHO (VISUALIZAR + LIMPAR + COMPRAR) -----
 
    def MeuCarrinho():
        id_cliente = st.session_state["cliente_id"]
        itens = View.visualizar_carrinho(id_cliente)
 
        if len(itens) == 0:
            st.write("SEU CARRINHO ESTÁ VAZIO!")
            return
 
        list_dic = []
        total = 0
        for item in itens:
            # USA O PREÇO CONGELADO NO MOMENTO EM QUE O ITEM FOI ADICIONADO AO CARRINHO
            preco = item.getPreco()
            subtotal = preco * item.getQuantidade()
            total += subtotal
            list_dic.append({
                "id_produto": item.getId_Produto(),
                "desc": item.getDescricao(),
                "quantidade": item.getQuantidade(),
                "preco_unit": preco,
                "subtotal": subtotal
            })
 
        df = pd.DataFrame(list_dic)
        st.dataframe(df, hide_index = True)
        st.write(f"**TOTAL: R$ {total:.2f}**")
 
        col1, col2 = st.columns(2)
 
        with col1:
            if st.button("FINALIZAR COMPRA"):
                try:
                    if View.comprar_carrinho(id_cliente):
                        st.success("COMPRA REALIZADA COM SUCESSO!")
                    else:
                        st.error("NÃO FOI POSSÍVEL FINALIZAR A COMPRA!")
                except Exception as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
 
        with col2:
            if st.button("LIMPAR CARRINHO"):
                try:
                    View.limpar_carrinho(id_cliente)
                    st.success("CARRINHO LIMPO!")
                except Exception as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
 
    #----- ABA MINHAS COMPRAS (HISTÓRICO AGRUPADO POR VENDA) -----
 
    def MinhasCompras():
        id_cliente = st.session_state["cliente_id"]
        vendas = View.listar_vendas_cliente(id_cliente)
 
        if len(vendas) == 0:
            st.write("VOCÊ AINDA NÃO REALIZOU NENHUMA COMPRA!")
            return
 
        historico = View.listar_compras(id_cliente)
 
        # ORDENA AS VENDAS DA MAIS RECENTE PARA A MAIS ANTIGA
        for venda in sorted(vendas, key = lambda v: v.getId(), reverse = True):
            data_str = venda.getData().strftime("%d/%m/%Y %H:%M")
            st.subheader(f"COMPRA #{venda.getId()} - {data_str}")
 
            itens_venda = [item for item in historico if item.getId() == venda.getId()]
 
            list_dic = []
            for item in itens_venda:
                # USA O PREÇO CONGELADO NO MOMENTO DA COMPRA (NÃO O PREÇO ATUAL DO PRODUTO)
                list_dic.append({
                    "produto": item.getDescricao(),
                    "quantidade": item.getQuantidade(),
                    "preco_unit": item.getPreco(),
                    "subtotal": item.getPreco() * item.getQuantidade()
                })
 
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index = True)
            st.write(f"**TOTAL: R$ {venda.getTotal():.2f}**")
            st.divider()