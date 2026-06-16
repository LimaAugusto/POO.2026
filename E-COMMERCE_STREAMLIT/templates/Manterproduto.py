import streamlit as st
import pandas as pd
from Views import View
import time
import base64

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
            for obj in produtos:
                col1, col2 = st.columns([1, 3])
                with col1:
                    if obj.getImagem():
                        img_bytes = base64.b64decode(obj.getImagem())
                        st.image(img_bytes, use_container_width = True)
                    else:
                        st.write("SEM IMAGEM")
                with col2:
                    st.write(f"**ID:** {obj.getId()}")
                    st.write(f"**DESCRIÇÃO:** {obj.getDesc()}")
                    st.write(f"**PREÇO:** R$ {obj.getPreco():.2f}")
                    st.write(f"**ESTOQUE:** {obj.getEstoque()}")
                    st.write(f"**ID CATEGORIA:** {obj.getId_Categoria()}")
                st.divider()

    def Inserir():
        descricao = st.text_input("INFORME A DESCRIÇÃO")
        preco = float(st.number_input("INFORME O PREÇO"))
        estoque = int(st.number_input("INFORME A QUANTIDADE NO ESTOQUE"))
        id_categoria = int(st.number_input("INFORME O ID DA CATEGORIA"))
        arquivo = st.file_uploader("IMAGEM DO PRODUTO (OPCIONAL)", type = ["png", "jpg", "jpeg", "webp"])
        if st.button("INSERIR"):
            try:
                imagem = base64.b64encode(arquivo.read()).decode("utf-8") if arquivo else None
                View.inserir_produto(descricao, preco, estoque, id_categoria, imagem)
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

            # MOSTRA A IMAGEM ATUAL, SE HOUVER
            if op.getImagem():
                st.write("IMAGEM ATUAL:")
                img_bytes = base64.b64decode(op.getImagem())
                st.image(img_bytes, width = 200)

            descricao = st.text_input("INFORME SUA NOVA DESCRIÇÃO", op.getDesc())
            preco = float(st.number_input("INFORME SEU NOVO PREÇO", op.getPreco()))
            estoque = int(st.number_input("INFORME A NOVA QUANTIDADE NO ESTOQUE", op.getEstoque()))
            id_categoria = int(st.number_input("INFORME O NOVO OU MESMO ID DA CATEGORIA", op.getId_Categoria()))
            arquivo = st.file_uploader("NOVA IMAGEM (DEIXE VAZIO PARA MANTER A ATUAL)", type = ["png", "jpg", "jpeg", "webp"])

            if st.button("ATUALIZAR"):
                id = op.getId()
                try:
                    # SE FIZER UPLOAD DE UMA NOVA IMAGEM, USA ELA; CASO CONTRÁRIO, MANTÉM A ATUAL
                    imagem = base64.b64encode(arquivo.read()).decode("utf-8") if arquivo else op.getImagem()
                    View.atualizar_produto(id, descricao, preco, estoque, id_categoria, imagem)
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