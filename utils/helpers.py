# Fonctions utilitaires pour l'application
import streamlit as st
from datetime import datetime, date

def check_password():
    """Vérifie le mot de passe de l'application"""
    def password_entered():
        if st.session_state["password"] == st.secrets["PASSWORD"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Efface le mot de passe de la session
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input(
            "Mot de passe", type="password", on_change=password_entered, key="password"
        )
        if "password_correct" in st.session_state and not st.session_state["password_correct"]:
            st.error("Mot de passe incorrect")
        st.stop()
    elif not st.session_state["password_correct"]:
        st.text_input(
            "Mot de passe", type="password", on_change=password_entered, key="password"
        )
        st.error("Mot de passe incorrect")
        st.stop()

def format_currency(amount):
    """Formate un montant en euros"""
    return f"{amount:.2f} €"

def calculate_days_until_departure(departure_date):
    """Calcule le nombre de jours jusqu'au départ"""
    if not departure_date:
        return None
    
    if isinstance(departure_date, str):
        departure_date = datetime.strptime(departure_date, "%Y-%m-%d").date()
    
    days_left = (departure_date - date.today()).days
    return days_left

def get_progress_percentage(completed, total):
    """Calcule le pourcentage de progression"""
    if total == 0:
        return 0
    return (completed / total) * 100

def format_date_for_display(date_str):
    """Formate une date pour l'affichage"""
    if not date_str:
        return "Non définie"
    
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d/%m/%Y")
    except:
        return date_str 