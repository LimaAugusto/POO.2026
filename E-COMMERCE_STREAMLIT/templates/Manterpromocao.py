import streamlit as st
import pandas as pd
from Views import View
import time
from datetime import datetime, date

class ManterPromocaoUI:
    def main():
        st.header("PROMOÇÕES")
        tab1, tab2, tab3 = st.tabs(["LISTAR", "INSERIR", "EXCLUIR"])
        with tab1: ManterPromocaoUI.Listar()
        with tab2: ManterPromocaoUI.Inserir()
        with tab3: ManterPromocaoUI.Excluir()

    def Listar():
        promocoes = View.listar_promocao()
        categorias = View.listar_categoria()
        nomes_cat = {c.getId(): c.getDesc() for c in categorias}

        if len(promocoes) == 0:
            st.write("NENHUMA PROMOÇÃO CADASTRADA!")
            return

        agora = datetime.now()
        list_dic = []
        for p in promocoes:
            ativa = p.getData_Inicio() <= agora <= p.getData_Fim()
            list_dic.append({
                "id": p.getId(),
                "categoria": nomes_cat.get(p.getId_Categoria(), f"CATEGORIA #{p.getId_Categoria()}"),
                "início": p.getData_Inicio().strftime("%d/%m/%Y"),
                "fim": p.getData_Fim().strftime("%d/%m/%Y"),
                "desconto (%)": p.getPercentual(),
                "status": "✅ ATIVA" if ativa else "⏸ INATIVA"
            })

        df = pd.DataFrame(list_dic)
        st.dataframe(df, hide_index = True)

    def Inserir():
        categorias = View.listar_categoria()
        if len(categorias) == 0:
            st.write("NENHUMA CATEGORIA CADASTRADA!")
            return

        categoria = st.selectbox("CATEGORIA", categorias)
        col1, col2 = st.columns(2)
        with col1:
            data_inicio = st.date_input("DATA DE INÍCIO", value = date.today())
        with col2:
            data_fim = st.date_input("DATA DE FIM", value = date.today())

        percentual = float(st.number_input("PERCENTUAL DE DESCONTO (%)", min_value = 0.1, max_value = 100.0, step = 0.5, value = 10.0))

        if st.button("INSERIR"):
            try:
                # CONVERTE date PARA datetime PARA COMPATIBILIDADE COM O MODELO
                dt_inicio = datetime.combine(data_inicio, datetime.min.time())
                dt_fim = datetime.combine(data_fim, datetime.max.time().replace(microsecond = 0))
                View.inserir_promocao(categoria.getId(), dt_inicio, dt_fim, percentual)
                st.success("PROMOÇÃO INSERIDA!")
            except Exception as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def Excluir():
        promocoes = View.listar_promocao()
        if len(promocoes) == 0:
            st.write("NENHUMA PROMOÇÃO CADASTRADA!")
            return

        op = st.selectbox("PROMOÇÃO", promocoes)
        if st.button("EXCLUIR"):
            try:
                View.excluir_promocao(op.getId())
                st.success("PROMOÇÃO EXCLUÍDA!")
            except Exception as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()