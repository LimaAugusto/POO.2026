import streamlit as st
import pandas as pd
from Views import View
import time

class ManterEntregaAdminUI:
    def main():
        st.header("CONTROLE DE ENTREGAS")
        tab1, tab2 = st.tabs(["ALOCAR ENTREGADOR", "ACOMPANHAR ENTREGAS"])
        with tab1: ManterEntregaAdminUI.Alocar()
        with tab2: ManterEntregaAdminUI.Acompanhar()

    def Alocar():
        vendas = View.listar_vendas()
        entregadores = View.listar_entregador()

        if len(vendas) == 0:
            st.write("NENHUMA VENDA REALIZADA AINDA!")
            return
        if len(entregadores) == 0:
            st.write("NENHUM ENTREGADOR CADASTRADO!")
            return

        clientes = View.listar_cliente()
        nomes_clientes = {c.getId(): c.getNome() for c in clientes}

        # FILTRA APENAS VENDAS SEM ENTREGA ALOCADA
        vendas_sem_entrega = [v for v in vendas if View.listar_entrega_venda(v.getId()) is None]

        if len(vendas_sem_entrega) == 0:
            st.write("TODAS AS VENDAS JÁ POSSUEM ENTREGA ALOCADA!")
            return

        venda = st.selectbox(
            "VENDA",
            vendas_sem_entrega,
            format_func = lambda v: f"VENDA #{v.getId()} - {nomes_clientes.get(v.getId_Cliente(), '?')} - R$ {v.getTotal():.2f}"
        )
        entregador = st.selectbox("ENTREGADOR", entregadores)

        if st.button("ALOCAR"):
            try:
                View.alocar_entrega(venda.getId(), entregador.getId())
                st.success(f"ENTREGADOR {entregador.getNome()} ALOCADO PARA A VENDA #{venda.getId()}!")
            except Exception as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def Acompanhar():
        entregas = View.listar_entrega()
        if len(entregas) == 0:
            st.write("NENHUMA ENTREGA ALOCADA AINDA!")
            return

        vendas = {v.getId(): v for v in View.listar_vendas()}
        clientes = {c.getId(): c.getNome() for c in View.listar_cliente()}
        entregadores = {e.getId(): e.getNome() for e in View.listar_entregador()}

        list_dic = []
        for e in entregas:
            venda = vendas.get(e.getId_Venda())
            list_dic.append({
                "entrega_id": e.getId(),
                "venda_id": e.getId_Venda(),
                "cliente": clientes.get(venda.getId_Cliente(), "?") if venda else "?",
                "entregador": entregadores.get(e.getId_Entregador(), "?"),
                "status": e.getStatus()
            })

        df = pd.DataFrame(list_dic)
        st.dataframe(df, hide_index = True)
