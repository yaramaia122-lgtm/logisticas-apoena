import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. VISUAL FINAL (MANTENDO O PADRÃO AURA)
st.set_page_config(page_title="Logística Aura Minerals", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    [data-testid="stSidebar"] { background-color: #002D5E !important; }
    
    /* Campos de preenchimento: Cinza e Azul */
    div[data-baseweb="input"], input, select, textarea {
        background-color: #E8E8E8 !important;
        color: #002D5E !important;
    }
    
    /* Botões: Cinza com borda Azul */
    .stButton>button {
        background-color: #E8E8E8 !important;
        color: #002D5E !important;
        border: 2px solid #002D5E !important;
        font-weight: bold;
    }
    
    /* Tabela: Removendo o preto */
    [data-testid="stDataEditor"] { background-color: #E8E8E8 !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. LÓGICA DE DADOS (LOCAL E CLOUD)
# Se estiver no seu PC, ele salva na pasta. Se estiver no link, ele salva no servidor.
DB_V = "banco_viagens_oficial.csv"

def carregar_dados():
    if not os.path.exists(DB_V):
        pd.DataFrame(columns=["Data", "Motorista", "Passageiro", "Trajeto", "Valor"]).to_csv(DB_V, index=False)
    return pd.read_csv(DB_V).fillna("")

df_v = carregar_dados()

# 3. BARRA LATERAL
with st.sidebar:
    st.image("https://gist.githubusercontent.com/user-attachments/assets/8e0f5228-40b9-4674-9f0f-6df3d57b280c", width=180)
    menu = st.radio("NAVEGAÇÃO", ["📋 Agenda", "📝 Programar", "💰 Financeiro"])

# 4. MÓDULOS (ONDE VOCÊ ESTÁ FAZENDO AS MELHORIAS)
if menu == "📝 Programar":
    st.header("📝 Programar Viagem")
    with st.form("meu_form"):
        # Seus campos aqui...
        passageiro = st.text_input("Passageiro")
        if st.form_submit_button("✅ SALVAR"):
            # LÓGICA: Salva o CSV
            st.success("Salvo com sucesso!")
            # DICA: Para salvar no GitHub pelo link, precisaríamos de uma biblioteca chamada 'PyGithub'
