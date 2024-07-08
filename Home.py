import streamlit as st

st.set_page_config(
    page_title="Gerenciamento de Recursos",
    page_icon="📊",
)

# Caminho para a logo
logo_path = 'data/atra_logo.png'

# Adiciona a logo no topo da barra lateral com verificação
try:
    with open(logo_path, "rb") as image_file:
        image = Image.open(io.BytesIO(image_file.read()))
        st.sidebar.image(image, use_column_width=True)
except (IOError, Image.UnidentifiedImageError) as e:
    st.sidebar.error(f"Erro ao carregar a imagem: {e}")

st.write("# Bem-vindo ao Gerenciamento de Recursos! 📊")

st.sidebar.success("Selecione uma página acima.")

st.markdown(
    """
    Este é um sistema de gerenciamento de recursos que coleta informações sobre habilidades e disponibilidade de recursos (funcionários).
    **👈 Selecione uma página na barra lateral** para começar.
    """
)
