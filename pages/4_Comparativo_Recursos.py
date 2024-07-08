import streamlit as st
import pandas as pd
import plotly.graph_objs as go

st.set_page_config(page_title="Comparativo de Recursos", page_icon="📈", layout="wide")

logo_path = 'data/atra_logo.png'

# Adiciona a logo no topo da barra lateral
st.sidebar.image(logo_path, use_column_width=True)

file_path = 'data/recursos_v2.xlsx'

# Carregar os dados do arquivo Excel
def load_data():
    df = pd.read_excel(file_path, sheet_name='Sheet1',
                       usecols=['ID Recurso', 'Recurso', 'Ingresso_ao_Time', 'Alocacao',
                                'Skill_Comunicacao', 'Skill_DG', 'Skill_IDMC_DG', 'Skill_IDMC_DQ', 'Skill_Axon',
                                'Skill_EDC', 'Skill_TDM', 'Skill_DPM', 'Skill_DEI', 'Skill_DEQ', 'Skill_PowerCenter',
                                'Skill_Purview', 'Skill_Dataplex', 'Skill_Databrix_Notebooks', 'Skill_Denodo',
                                'Skill_OpenMetadata', 'Skill_Python', 'Skill_Azure'])

# Formatar a data de ingresso ao time
    df['Ingresso_ao_Time'] = pd.to_datetime(df['Ingresso_ao_Time']).dt.strftime('%d/%m/%Y')
    return df

# Formatar os rótulos das habilidades para despoluir
def limpar_rotulos(rotulos):
    return [rotulo.replace('Skill_', '') for rotulo in rotulos]

st.subheader("Comparativo de Recursos")

# Carregar os dados
df = load_data()
recursos = df['Recurso'].unique()

# Separar os filtros de seleção de recursos em duas colunas
col1, col2 = st.columns(2)

with col1:
    recurso1 = st.selectbox("Selecione o Primeiro Recurso", recursos)

with col2:
    recurso2 = st.selectbox("Selecione o Segundo Recurso", recursos)

# Lista do que exibir no perfil do recurso
def exibir_detalhes_perfil(recurso, df):
    perfil = df[df['Recurso'] == recurso]
    if not perfil.empty:
        #st.write(f"**ID Recurso**: {perfil.iloc[0]['ID Recurso']}")
        st.write(f"**Recurso**: {perfil.iloc[0]['Recurso']}")
        st.write(f"**Data de Ingresso ao Time**: {perfil.iloc[0]['Ingresso_ao_Time']}")
        st.write(f"**Alocação**: {perfil.iloc[0]['Alocacao']}")

if recurso1 and recurso2:
    col1, col2 = st.columns(2)

    with col1:
        st.write("### Perfil do Primeiro Recurso")
        exibir_detalhes_perfil(recurso1, df)

        categorias = ['Skill_Comunicacao', 'Skill_DG', 'Skill_IDMC_DG', 'Skill_IDMC_DQ', 'Skill_Axon', 'Skill_EDC',
                      'Skill_TDM', 'Skill_DPM', 'Skill_DEI', 'Skill_DEQ', 'Skill_PowerCenter', 'Skill_Purview',
                      'Skill_Dataplex', 'Skill_Databrix_Notebooks', 'Skill_Denodo', 'Skill_OpenMetadata',
                      'Skill_Python', 'Skill_Azure']

        rotulos_limpos = limpar_rotulos(categorias)

        valores1 = df[df['Recurso'] == recurso1][categorias].values.flatten().tolist()
        valores1 += valores1[:1]

        fig1 = go.Figure()
        fig1.add_trace(go.Scatterpolar(
            r=valores1,
            theta=rotulos_limpos + [rotulos_limpos[0]],
            fill='toself',
            name=recurso1,
            line=dict(color='red')
        ))

        fig1.update_layout(
            title="Radar de Skills",
            width=550,  # Largura do gráfico
            height=400,  # Altura do gráfico
            margin=dict(l=20, r=20, b=20, t=50, pad=4),  # Margens
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 3],
                    tickvals=[1, 2, 3],
                    ticktext=['Baixa', 'Média', 'Alta']
                )),
            showlegend=True
        )

        st.plotly_chart(fig1)

    with col2:
        st.write("### Perfil do Segundo Recurso")
        exibir_detalhes_perfil(recurso2, df)

        valores2 = df[df['Recurso'] == recurso2][categorias].values.flatten().tolist()
        valores2 += valores2[:1]

        fig2 = go.Figure()
        fig2.add_trace(go.Scatterpolar(
            r=valores2,
            theta=rotulos_limpos + [rotulos_limpos[0]],
            fill='toself',
            name=recurso2,
            line=dict(color='blue')
        ))

        fig2.update_layout(
            title="Radar de Skills",
            width=550,  # Largura do gráfico
            height=400,  # Altura do gráfico
            margin=dict(l=20, r=20, b=20, t=50, pad=4),  # Margens
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 3],
                    tickvals=[1, 2, 3],
                    ticktext=['Baixa', 'Média', 'Alta']
                )),
            showlegend=True
        )

        st.plotly_chart(fig2)

