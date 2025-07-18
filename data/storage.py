# Gestion du stockage des données
import json
import os
import streamlit as st
from .models import (
    get_default_checklist, 
    get_default_travel_profile, 
    get_default_itinerary,
    get_default_flight_info,
    get_default_budget_planning,
    migrate_checklist
)
from config.settings import DATA_FILE

def load_data():
    """Charge les données depuis le fichier JSON ou crée des données par défaut"""
    if not os.path.exists(DATA_FILE):
        data = {
            "departure_date": None,
            "itinerary": [],
            "budget": [],
            "checklist": get_default_checklist(),
            "travel_profile": get_default_travel_profile(),
            "flight_info": get_default_flight_info(),
            "budget_planning": get_default_budget_planning()
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    else:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        # Migration de la checklist si nécessaire
        if "checklist" in data:
            old_checklist = data["checklist"]
            new_checklist = get_default_checklist()
            
            # Vérifie si la migration est nécessaire
            if len(old_checklist) < len(new_checklist):
                data["checklist"] = migrate_checklist(old_checklist)
        
        # Ajout du profil de voyage si absent
        if "travel_profile" not in data:
            data["travel_profile"] = get_default_travel_profile()
        
        # Ajout des informations de vol si absent
        if "flight_info" not in data:
            data["flight_info"] = get_default_flight_info()
        
        # Ajout du budget prévisionnel si absent
        if "budget_planning" not in data:
            data["budget_planning"] = get_default_budget_planning()
        
        # Sauvegarde les données migrées
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    return data

def save_data(data):
    """Sauvegarde les données dans le fichier JSON"""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def export_data():
    """Exporte les données au format JSON pour sauvegarde"""
    data = st.session_state.data
    return json.dumps(data, indent=2, ensure_ascii=False)

def sync_state():
    """Synchronise l'état de session avec le fichier de données"""
    save_data(st.session_state.data) 