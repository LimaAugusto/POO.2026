import streamlit as st
from Views import View
import time

class ReajustarProdutoUI:
    def main():
        st.header("REAJUSTAR PREÇOS")
        st.write("INFORME O PERCENTUAL DE REAJUSTE A SER APLICADO EM TODOS OS PRODUTOS.")
        st.write("USE VALORES POSITIVOS PARA AUMENTAR E NEGATIVOS PARA REDUZIR (EX.: 10 PARA +10%, -5 PARA -5%).")

        percentual = float(st.number_input("PERCENTUAL DE REAJUSTE (%)", step = 0.5, value = 0.0))

        if st.button("REAJUSTAR"):
            try:
                View.reajustar_preco(percentual)
                st.success("PREÇOS REAJUSTADOS COM SUCESSO!")
            except Exception as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()
