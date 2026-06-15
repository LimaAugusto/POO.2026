import streamlit as st
import pandas as pd
from Views import View

class ManterVendaUI:
    def main():
        st.header("LISTA DE VENDAS")
        ManterVendaUI.Listar()

    def Listar():
        vendas = View.listar_vendas()
        if len(vendas) == 0:
            st.write("NENHUMA VENDA REALIZADA!")
            return

        # MONTA UM DICIONÁRIO id_cliente -> nome PARA EXIBIR O NOME EM VEZ DO ID
        clientes = View.listar_cliente()
        nomes_clientes = {c.getId(): c.getNome() for c in clientes}

        # CARREGA TODO O HISTÓRICO UMA ÚNICA VEZ (EVITA RE-LER O ARQUIVO PARA CADA VENDA)
        historico = View.listar_historico_completo()

        # TABELA RESUMIDA
        list_dic = []
        for venda in sorted(vendas, key = lambda v: v.getId(), reverse = True):
            list_dic.append({
                "id": venda.getId(),
                "data": venda.getData().strftime("%d/%m/%Y %H:%M"),
                "cliente": nomes_clientes.get(venda.getId_Cliente(), f"CLIENTE #{venda.getId_Cliente()}"),
                "total": venda.getTotal()
            })
        df = pd.DataFrame(list_dic)
        st.dataframe(df, hide_index = True, column_order = ["id", "data", "cliente", "total"])

        st.subheader("DETALHES POR VENDA")

        # EXPANDER POR VENDA, COM OS ITENS COMPRADOS
        for venda in sorted(vendas, key = lambda v: v.getId(), reverse = True):
            data_str = venda.getData().strftime("%d/%m/%Y %H:%M")
            nome_cliente = nomes_clientes.get(venda.getId_Cliente(), f"CLIENTE #{venda.getId_Cliente()}")

            with st.expander(f"VENDA #{venda.getId()} - {nome_cliente} - {data_str} - R$ {venda.getTotal():.2f}"):
                itens_venda = [item for item in historico if item.getId() == venda.getId() and item.getId_Cliente() == venda.getId_Cliente()]

                if len(itens_venda) == 0:
                    st.write("NENHUM ITEM ENCONTRADO PARA ESTA VENDA.")
                    continue

                itens_dic = []
                for item in itens_venda:
                    itens_dic.append({
                        "produto": item.getDescricao(),
                        "quantidade": item.getQuantidade(),
                        "preco_unit": item.getPreco(),
                        "subtotal": item.getPreco() * item.getQuantidade()
                    })

                df_itens = pd.DataFrame(itens_dic)
                st.dataframe(df_itens, hide_index = True)