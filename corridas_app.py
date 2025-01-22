# streamlit run corridas_app.py

import pandas as pd
import streamlit as st
from PIL import Image
#import openpyxl as op

#######################################
# CONFICURAÇÃO DA PÁGINA
#######################################

st.set_page_config(
    page_title="Corridas Compartilhadas",
    page_icon=":bar_chart:",
    layout="wide",
)

st.title("ANÁLISE DE CORRIDAS COMPARTILHADAS")
st.markdown("_Versão 1.0_")

with st.sidebar:
    logo = Image.open('imagens/car_2.jpg')
    st.image(logo, use_container_width=True)
    #st.title("Arquivo")
    #uploaded_file = st.sidebar.file_uploader("Escolha um arquivo")

#if uploaded_file is None:
    #st.info("Faça o upload do arquivo", icon="📖")
    #st.stop()


#######################################
# CARREGANDO ARQUIVO
#######################################

@st.cache_data
#def load_data(file):
def load_data(path: str):
    data = pd.read_excel(
        path,
        #engine="openpyxl",
        #sheet_name="Médias",
        #usecols="B:C",
        #skiprows=2,
    )
    return data


#df = load_data(uploaded_file)
df = load_data("./Analise de CorComp_D.xlsx")

with st.expander("Dados"):
    st.dataframe(
        df,
    )

col1, col2 = st.columns(2)

with col1:
    st.bar_chart(df, x="Mês/Ano", y="Valor (R$)")

with col2:
    st.line_chart(df, x="Mês/Ano", y="Valor (R$)")
