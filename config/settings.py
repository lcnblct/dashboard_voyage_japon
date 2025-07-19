# Configuration de l'application
import streamlit as st

# Configuration de la page
PAGE_CONFIG = {
    "page_title": "Dashboard Voyage Japon",
    "page_icon": "🇯🇵",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "menu_items": {
        'Get Help': None,
        'Report a bug': None,
        'About': "Dashboard de préparation de voyage au Japon 🇯🇵"
    }
}

# Fichier de données
DATA_FILE = "data.json"

# Menu de navigation
NAVIGATION_MENU = [
    "Accueil",
    "Profil de Voyage",
    "Prompt Ultime",
    "Assistant IA",
    "Itinéraire",
    "Calendrier",
    "Vol",
    "Budget",
    "Checklist",
    "Carte",
    "Ressources",
    "Réglages"
]

def configure_page():
    """Configure la page Streamlit avec thème sombre forcé"""
    st.set_page_config(**PAGE_CONFIG)
    
    # Forcer le thème sombre de Streamlit de manière complète
    st.markdown("""
    <style>
        /* Configuration globale pour forcer le mode sombre partout */
        :root {
            --background-color: #0e1117 !important;
            --text-color: #fafafa !important;
            --secondary-background-color: #262730 !important;
            --main-background-color: #0e1117 !important;
            --main-text-color: #fafafa !important;
            --main-secondary-background-color: #262730 !important;
        }
        
        /* Override complet des variables CSS de Streamlit */
        .stApp {
            --background-color: #0e1117 !important;
            --text-color: #fafafa !important;
            --secondary-background-color: #262730 !important;
            --main-background-color: #0e1117 !important;
            --main-text-color: #fafafa !important;
            --main-secondary-background-color: #262730 !important;
        }
        
        /* Forcer tous les éléments à utiliser le thème sombre */
        .stApp > div {
            background-color: #0e1117 !important;
            color: #fafafa !important;
        }
        
        /* Sidebar forcée en mode sombre */
        .css-1d391kg {
            background-color: #262730 !important;
        }
        
        /* Header forcé en mode sombre */
        .css-1v0mbdj {
            background-color: #262730 !important;
        }
        
        /* Tous les éléments de texte */
        .stMarkdown, .stText, .stWrite {
            color: #fafafa !important;
        }
        
        /* Inputs et widgets */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > div,
        .stNumberInput > div > div > input,
        .stDateInput > div > div > input,
        .stTimeInput > div > div > input {
            background-color: #262730 !important;
            color: #fafafa !important;
            border-color: #4a5568 !important;
        }
        
        /* Boutons */
        .stButton > button {
            background-color: #4CAF50 !important;
            color: white !important;
        }
        
        /* Alertes et messages */
        .stAlert {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        /* Métriques */
        .metric-container {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        /* Cartes et conteneurs */
        .stCard {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        /* Onglets */
        .stTabs [data-baseweb="tab-list"] {
            background-color: #262730 !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            color: #fafafa !important;
        }
        
        /* Radio buttons et checkboxes */
        .stRadio > div > div > div > label,
        .stCheckbox > div > div > div > label {
            color: #fafafa !important;
        }
        
        /* Dataframes */
        .stDataFrame {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        /* Tables */
        .stTable {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        /* Charts */
        .stPlotlyChart {
            background-color: #262730 !important;
        }
        
        /* Maps */
        .stMap {
            background-color: #262730 !important;
        }
        
        /* Forcer le thème sombre sur tous les éléments enfants */
        * {
            background-color: inherit !important;
        }
        
        /* Override spécifique pour les éléments qui pourraient hériter du thème clair */
        div[data-testid="stSidebar"] {
            background-color: #262730 !important;
        }
        
        div[data-testid="stSidebar"] * {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        /* Forcer le thème sombre sur les éléments de navigation */
        .css-1d391kg, .css-1v0mbdj, .css-1lcbmhc {
            background-color: #262730 !important;
        }
        
        /* Override pour les éléments de Streamlit qui pourraient utiliser le thème système */
        [data-testid="stAppViewContainer"] {
            background-color: #0e1117 !important;
        }
        
        [data-testid="stAppViewContainer"] * {
            background-color: inherit !important;
        }
    </style>
    """, unsafe_allow_html=True) 