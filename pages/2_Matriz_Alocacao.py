import streamlit as st

st.set_page_config(page_title="Matriz de Alocação", page_icon="📊")

# Caminho para a logo
logo_path = 'data/atra_logo.png'

# Adiciona a logo no topo da barra lateral
st.sidebar.image(logo_path, use_column_width=True)

image_path_matriz = 'data/matriz.png'

st.subheader("Matriz de Alocação")
st.image(image_path_matriz)
