import streamlit as st

st.set_page_config(
    page_title="Gerenciamento de Recursos",
    page_icon="📊",
)

st.write("# Bem-vindo ao Gerenciamento de Recursos! 📊")

st.sidebar.success("Selecione uma página acima.")

st.markdown(
    """
    Este é um sistema de gerenciamento de recursos que coleta informações sobre habilidades e disponibilidade de recursos (funcionários).
    **👈 Selecione uma página na barra lateral** para começar.
    """
)
