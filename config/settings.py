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
    """Configure la page Streamlit"""
    st.set_page_config(**PAGE_CONFIG) 