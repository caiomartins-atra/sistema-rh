import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Cadastro de Recurso", page_icon="📝")

# Caminho para a logo
logo_path = 'data/atra_logo.png'

# Adiciona a logo no topo da barra lateral
st.sidebar.image(logo_path, use_column_width=True)

# Caminho para o arquivo Excel
file_path = 'data/recursos_v2.xlsx'

def generate_resource_id():
    return str(random.randint(100, 999))

def skill_mapping(skill_value):
    mapping = {"Alta": 1, "Média": 2, "Baixa": 3}
    return mapping.get(skill_value, "")

st.subheader("Cadastro de Recurso")

with st.form(key='cadastro_form'):
    Recurso = st.text_input("Recurso")
    Perfil = st.text_input("Perfil")
    Disponibilidade_DG = st.radio("Disponível para DG?", ("Sim", "Não"))
    Disponibilidade_IA = st.radio("Disponível para IA?", ("Sim", "Não"))
    Ingresso_ao_Time = st.text_input("Data de Ingresso ao Time")
    Ate = st.text_input("Até")
    Duracao = st.text_input("Duração")
    Ano_de_ate = st.text_input("Ano De|Até")
    email = st.text_input("E-mail")
    Local_de_atuacao = st.text_input("Local de Atuação")
    Celular = st.text_input("Celular")
    Qtd_Atuacoes = st.text_input("Quantidade de atuações em projeto")
    Alocacao = st.text_input("Alocação")
    reuniao_one_on_one = st.text_input("Data do último 1:1")
    gestor_one_on_one = st.text_input("Gestor do último 1:1")
    Skill_Comunicacao = st.selectbox("Skill Comunicação", ["Alta", "Média", "Baixa"])
    Skill_DG = st.selectbox("Skill DG", ["Alta", "Média", "Baixa"])
    Skill_IDMC_DG = st.selectbox("Skill IDMC DG", ["Alta", "Média", "Baixa"])
    Skill_IDMC_DQ = st.selectbox("Skill IDMC DQ", ["Alta", "Média", "Baixa"])
    Skill_Axon = st.selectbox("Skill Axon", ["Alta", "Média", "Baixa"])
    Skill_EDC = st.selectbox("Skill EDC", ["Alta", "Média", "Baixa"])
    Skill_TDM = st.selectbox("Skill TDM", ["Alta", "Média", "Baixa"])
    Skill_DPM = st.selectbox("Skill DPM", ["Alta", "Média", "Baixa"])
    Skill_DEI = st.selectbox("Skill DEI", ["Alta", "Média", "Baixa"])
    Skill_DEQ = st.selectbox("Skill DEQ", ["Alta", "Média", "Baixa"])
    Skill_PowerCenter = st.selectbox("Skill PowerCenter", ["Alta", "Média", "Baixa"])
    Skill_Purview = st.selectbox("Skill Purview", ["Alta", "Média", "Baixa"])
    Skill_Dataplex = st.selectbox("Skill Dataplex", ["Alta", "Média", "Baixa"])
    Skill_Databrix_Notebooks = st.selectbox("Skill Databricks Notebooks", ["Alta", "Média", "Baixa"])
    Skill_Denodo = st.selectbox("Skill Denodo", ["Alta", "Média", "Baixa"])
    Skill_OpenMetadata = st.selectbox("Skill OpenMetadata", ["Alta", "Média", "Baixa"])
    Skill_Python = st.selectbox("Skill Python", ["Alta", "Média", "Baixa"])
    Skill_Azure = st.selectbox("Skill Azure", ["Alta", "Média", "Baixa"])

    submit_button = st.form_submit_button(label='Cadastrar')

if submit_button:
    id_recurso = generate_resource_id() # Gera um ID único para o recurso
    st.success(f"Cadastro de Recurso: ID Recurso: {id_recurso}, Recurso: {Recurso}, Perfil: {Perfil}")

    df = pd.read_excel(file_path)

    new_data = {
        'ID Recurso': id_recurso,
        'Recurso': Recurso,
        'Perfil': Perfil,
        'Disponibilidade_DG': 'Sim' if Disponibilidade_DG == 'Sim' else 'Não',
        'Disponibilidade_IA': 'Sim' if Disponibilidade_IA == 'Sim' else 'Não',
        'Ingresso_ao_Time': Ingresso_ao_Time,
        'Ate': Ate,
        'Duracao': Duracao,
        'Ano_de_ate': Ano_de_ate,
        'email': email,
        'Local_de_atuacao': Local_de_atuacao,
        'Celular': Celular,
        'Qtd_Atuacoes': Qtd_Atuacoes,
        'Alocacao': Alocacao,
        'reuniao_one_on_one': reuniao_one_on_one,
        'gestor_one_on_one': gestor_one_on_one,
        'Skill_Comunicacao': Skill_Comunicacao,
        'Skill_DG': Skill_DG,
        'Skill_IDMC_DG': Skill_IDMC_DG,
        'Skill_IDMC_DQ': Skill_IDMC_DQ,
        'Skill_Axon': Skill_Axon,
        'Skill_EDC': Skill_EDC,
        'Skill_TDM': Skill_TDM,
        'Skill_DPM': Skill_DPM,
        'Skill_DEI': Skill_DEI,
        'Skill_DEQ': Skill_DEQ,
        'Skill_PowerCenter': Skill_PowerCenter,
        'Skill_Purview': Skill_Purview,
        'Skill_Dataplex': Skill_Dataplex,
        'Skill_Databrix_Notebooks': Skill_Databrix_Notebooks,
        'Skill_Denodo': Skill_Denodo,
        'Skill_OpenMetadata': Skill_OpenMetadata,
        'Skill_Python': Skill_Python,
        'Skill_Azure': Skill_Azure,
        'De_Para_Skill_Comunicacao': skill_mapping(Skill_Comunicacao),
        'De_Para_Skill_DG': skill_mapping(Skill_DG),
        'De_Para_Skill_IDMC_DG': skill_mapping(Skill_IDMC_DG),
        'De_Para_Skill_IMDC_DQ': skill_mapping(Skill_IDMC_DQ),
        'De_Para_Skill_Axon': skill_mapping(Skill_Axon),
        'De_Para_Skill_EDC': skill_mapping(Skill_EDC),
        'De_Para_Skill_TDM': skill_mapping(Skill_TDM),
        'De_Para_Skill_DPM': skill_mapping(Skill_DPM),
        'De_Para_Skill_DEI': skill_mapping(Skill_DEI),
        'De_Para_Skill_DEQ': skill_mapping(Skill_DEQ),
        'De_Para_Skill_PowerCenter': skill_mapping(Skill_PowerCenter),
        'De_Para_Skill_Purview': skill_mapping(Skill_Purview),
        'De_Para_Skill_Dataplex': skill_mapping(Skill_Dataplex),
        'De_Para_Skill_Databrix_Notebooks': skill_mapping(Skill_Databrix_Notebooks),
        'De_Para_Skill_Denodo': skill_mapping(Skill_Denodo),
        'De_Para_Skill_OpenMetadata': skill_mapping(Skill_OpenMetadata),
        'De_Para_Skill_Python': skill_mapping(Skill_Python),
        'De_Para_Skill_Azure': skill_mapping(Skill_Azure)
    }

    # Converte os novos dados para um DataFrame
    new_data_df = pd.DataFrame([new_data])

    # Adiciona os novos dados ao DataFrame
    df = pd.concat([df, new_data_df], ignore_index=True)

    # Salva o DataFrame atualizado no arquivo Excel
    df.to_excel(file_path, index=False)

    st.success("Dados submetidos com sucesso!")
