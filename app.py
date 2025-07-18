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
from data.storage import load_data, sync_state
from utils.helpers import check_password

# Import des pages
from pages.home import display_home
from pages.travel_profile import display_travel_profile
from pages.itinerary import display_itinerary
from pages.calendar import display_calendar
from pages.flight import display_flight
from pages.budget import display_budget
from pages.checklist import display_checklist
from pages.map import display_map
from pages.resources import display_resources
from pages.settings import display_settings

# Configuration de la page
configure_page()

# Application des styles
apply_styles()

# --- Initialisation de session_state ---
if "initialized" not in st.session_state:
    st.session_state.data = load_data()
    st.session_state.initialized = True

# --- Protection par mot de passe ---
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