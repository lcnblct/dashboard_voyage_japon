# Dashboard Voyage Japon - Application principale refactorisée
import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime, date
import folium
from streamlit_folium import st_folium

# Import des modules refactorisés
from config.settings import configure_page, NAVIGATION_MENU
from config.styles import apply_styles
from config import force_dark_theme
from data.storage import load_data, sync_state
from utils.helpers import check_password

# Import des modules
from modules.home import display_home
from modules.travel_profile import display_travel_profile
from modules.prompt_generator import display_prompt_generator
from modules.ai_assistant import display_ai_assistant
from modules.itinerary import display_itinerary
from modules.calendar import display_calendar
from modules.flight import display_flight
from modules.budget import display_budget
from modules.checklist import display_checklist
from modules.map import display_map
from modules.resources import display_resources
from modules.settings import display_settings

# Configuration de la page
configure_page()

# Forçage global du thème sombre
force_dark_theme()

# Application des styles
apply_styles()

# Configuration supplémentaire pour forcer le thème sombre
st.markdown("""
<style>
    /* FORÇAGE ULTIME DU THÈME SOMBRE - AUCUNE EXCEPTION */
    /* Override global pour empêcher tout thème clair */
    :root {
        color-scheme: dark !important;
    }
    
    /* Forcer le thème sombre sur tous les éléments */
    html, body, .stApp, .stApp > div, .stApp > div > div {
        background-color: #0e1117 !important;
        color: #fafafa !important;
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
    
    /* Forcer le thème sombre sur tous les éléments enfants */
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
    
    /* Forcer le thème sombre sur les éléments spécifiques de Streamlit */
    div[data-testid="stSidebar"] {
        background-color: #262730 !important;
    }
    
    div[data-testid="stSidebar"] * {
        background-color: #262730 !important;
        color: #fafafa !important;
    }
    
    /* Override pour les éléments de navigation */
    .css-1d391kg, .css-1v0mbdj, .css-1lcbmhc, .css-1v0mbdj {
        background-color: #262730 !important;
    }
    
    /* Forcer le thème sombre sur tous les widgets Streamlit */
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
    
    /* Override pour les éléments de base */
    .stMarkdown, .stText, .stWrite, p, span, div {
        color: #fafafa !important;
    }
    
    /* Forcer le thème sombre sur les éléments de base */
    html, body {
        background-color: #0e1117 !important;
        color: #fafafa !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Initialisation de session_state ---
if "initialized" not in st.session_state:
    st.session_state.data = load_data()
    st.session_state.initialized = True

# --- Protection par code d'accès ---
check_password()

# --- Navigation principale ---
choix = st.sidebar.radio("Navigation", NAVIGATION_MENU, format_func=lambda x: x)

st.sidebar.markdown("---")
st.sidebar.info("🇯🇵 Application de préparation de voyage au Japon — par votre assistant IA")

# --- Routage des pages ---
if choix == "Accueil":
    display_home()
elif choix == "Profil de Voyage":
    display_travel_profile()
elif choix == "Prompt Ultime":
    display_prompt_generator()
elif choix == "Assistant IA":
    display_ai_assistant()
elif choix == "Itinéraire":
    display_itinerary()
elif choix == "Calendrier":
    display_calendar()
elif choix == "Vol":
    display_flight()
elif choix == "Budget":
    display_budget()
elif choix == "Checklist":
    display_checklist()
elif choix == "Carte":
    display_map()
elif choix == "Ressources":
    display_resources()
elif choix == "Réglages":
    display_settings() 