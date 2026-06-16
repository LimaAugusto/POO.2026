import streamlit as st
from Views import View
import time

class ManterEntregaEntregadorUI:
    def main():
        st.header(f"MINHAS ENTREGAS")
        id_entregador = st.session_state["entregador_id"]
        entregas = View.listar_entregas_entregador(id_entregador)

        if len(entregas) == 0:
            st.write("NENHUMA ENTREGA ALOCADA PARA VOCÊ!")
            return

        vendas = {v.getId(): v for v in View.listar_vendas()}
        clientes = {c.getId(): c.getNome() for c in View.listar_cliente()}

        for entrega in entregas:
            venda = vendas.get(entrega.getId_Venda())
            nome_cliente = clientes.get(venda.getId_Cliente(), "?") if venda else "?"
            total = venda.getTotal() if venda else 0

            with st.expander(f"ENTREGA #{entrega.getId()} - VENDA #{entrega.getId_Venda()} - {nome_cliente} - STATUS: {entrega.getStatus()}"):
                st.write(f"**CLIENTE:** {nome_cliente}")
                st.write(f"**TOTAL DA VENDA:** R$ {total:.2f}")
                st.write(f"**STATUS ATUAL:** {entrega.getStatus()}")

                proximo = entrega.proximo_status()
                if proximo:
                    if st.button(f"AVANÇAR PARA '{proximo}'", key = f"btn_{entrega.getId()}"):
                        try:
                            View.avancar_status(entrega.getId())
                            st.success(f"STATUS ATUALIZADO PARA '{proximo}'!")
                        except Exception as erro:
                            st.error(erro)
                        time.sleep(2)
                        st.rerun()
                else:
                    st.success("✅ ENTREGA CONCLUÍDA!")
