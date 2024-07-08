import streamlit as st
import pandas as pd
import plotly.graph_objs as go

st.set_page_config(page_title="Gráficos de Skills", page_icon="📈")

# Caminho para a logo
logo_path = 'data/atra_logo.png'

# Adiciona a logo no topo da barra lateral
st.sidebar.image(logo_path, use_column_width=True)

file_path = 'data/recursos_v2.xlsx'

def load_data():
    df = pd.read_excel(file_path, sheet_name='Sheet1',
                       usecols=['ID Recurso', 'Recurso', 'Skill_Comunicacao', 'Skill_DG', 'Skill_IDMC_DG',
                                'Skill_IDMC_DQ', 'Skill_Axon', 'Skill_EDC', 'Skill_TDM', 'Skill_DPM', 'Skill_DEI',
                                'Skill_DEQ', 'Skill_PowerCenter', 'Skill_Purview', 'Skill_Dataplex',
                                'Skill_Databrix_Notebooks', 'Skill_Denodo', 'Skill_OpenMetadata', 'Skill_Python',
                                'Skill_Azure'])
    return df

st.subheader("Gráfico de Skills")

df = load_data()
recursos = df['Recurso'].unique()
recurso1 = st.selectbox("Selecione o Primeiro Recurso", recursos)
recurso2 = st.selectbox("Selecione o Segundo Recurso", recursos)

if recurso1 and recurso2:
    selected_df = df[(df['Recurso'] == recurso1) | (df['Recurso'] == recurso2)]

    categories = ['Skill_Comunicacao', 'Skill_DG', 'Skill_IDMC_DG', 'Skill_IDMC_DQ', 'Skill_Axon', 'Skill_EDC',
                  'Skill_TDM', 'Skill_DPM', 'Skill_DEI', 'Skill_DEQ', 'Skill_PowerCenter', 'Skill_Purview',
                  'Skill_Dataplex', 'Skill_Databrix_Notebooks', 'Skill_Denodo', 'Skill_OpenMetadata', 'Skill_Python',
                  'Skill_Azure']

    fig = go.Figure()

    for i, row in selected_df.iterrows():
        values = row[categories].values.flatten().tolist()
        values += values[:1]
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories + [categories[0]],
            fill='toself',
            name=row['Recurso']
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 3],
                tickvals=[1, 2, 3],
                ticktext=['Baixa', 'Média', 'Alta']
            )),
        showlegend=True
    )

    st.plotly_chart(fig)
