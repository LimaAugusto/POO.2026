import streamlit as st
import time
from Views import View

class LoginUI:
    def main():
        st.header("ENTRAR NO SISTEMA")
        email = st.text_input("E-MAIL")
        senha = st.text_input("SENHA", type="password")
        if st.button("ENTRAR"):
            c = View.usuario_autenticar(email, senha)
            if c == None: st.write("E-MAIL OU SENHA INVÁLIDO(S)!")
            else:
                st.session_state["cliente_id"] = c["id"]
                st.session_state["cliente_nome"] = c["nome"]
            time.sleep(2)    
            st.rerun()