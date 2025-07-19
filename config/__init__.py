# Configuration du thème sombre forcé
import streamlit as st

def force_dark_theme():
    """Force le thème sombre de manière globale"""
    st.markdown("""
    <style>
        /* FORÇAGE GLOBAL DU THÈME SOMBRE */
        :root {
            color-scheme: dark !important;
        }
        
        /* Override complet pour empêcher tout thème clair */
        html, body, .stApp, .stApp > div, .stApp > div > div {
            background-color: #0e1117 !important;
            color: #fafafa !important;
        }
        
        /* Variables CSS forcées */
        .stApp {
            --background-color: #0e1117 !important;
            --text-color: #fafafa !important;
            --secondary-background-color: #262730 !important;
            --main-background-color: #0e1117 !important;
            --main-text-color: #fafafa !important;
            --main-secondary-background-color: #262730 !important;
        }
        
        /* Override pour tous les éléments */
        .stApp *,
        .stApp > div *,
        .stApp > div > div *,
        [data-testid="stSidebar"] *,
        [data-testid="stSidebar"] > div *,
        [data-testid="stAppViewContainer"] *,
        [data-testid="stAppViewContainer"] > div * {
            background-color: inherit !important;
            color: inherit !important;
        }
        
        /* Sidebar forcée */
        div[data-testid="stSidebar"] {
            background-color: #262730 !important;
        }
        
        div[data-testid="stSidebar"] * {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        /* Navigation forcée */
        .css-1d391kg, .css-1v0mbdj, .css-1lcbmhc {
            background-color: #262730 !important;
        }
        
        /* Widgets forcés */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > div,
        .stNumberInput > div > div > input,
        .stDateInput > div > div > input,
        .stTimeInput > div > div > input,
        .stTextArea > div > div > textarea {
            background-color: #262730 !important;
            color: #fafafa !important;
            border-color: #4a5568 !important;
        }
        
        /* Texte forcé */
        .stMarkdown, .stText, .stWrite, p, span, div {
            color: #fafafa !important;
        }
        
        /* Base forcée */
        html, body {
            background-color: #0e1117 !important;
            color: #fafafa !important;
        }
    </style>
    """, unsafe_allow_html=True) 