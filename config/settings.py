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
    
    # Forcer le thème sombre de Streamlit
    st.markdown("""
    <style>
        /* Configuration globale pour forcer le mode sombre */
        :root {
            --background-color: #0e1117;
            --text-color: #fafafa;
            --secondary-background-color: #262730;
        }
        
        /* Override des variables CSS de Streamlit */
        .stApp {
            --background-color: #0e1117 !important;
            --text-color: #fafafa !important;
            --secondary-background-color: #262730 !important;
        }
    </style>
    """, unsafe_allow_html=True) 