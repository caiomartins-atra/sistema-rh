import streamlit as st

st.set_page_config(page_title="Atra GPT", page_icon="🤖")

st.markdown(
    """
    <style>
    .header {
        font-size: 36px;
        font-weight: bold;
        color: #FF4B4B;
    }
    .subheader {
        font-size: 24px;
        font-weight: bold;
        color: #4B4BFF;
    }
    .link {
        font-size: 20px;
        font-weight: bold;
        color: #1E90FF;
        text-decoration: none;
    }
    .link:hover {
        color: #FF6347;
    }
    .image-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .image {
        max-width: 80%;
        height: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="header">Atra GPT</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="subheader">Veja o Atra GPT!</div>
    <p>Acesse o Atra GPT clicando no link abaixo:</p>
    <a href="https://app-backend-hbdynjwt73tc4.azurewebsites.net/" class="link">Atra GPT</a>
    """,
    unsafe_allow_html=True,
)

