# Page de gestion de l'itinéraire
import streamlit as st
import pandas as pd
from datetime import date
from data.models import get_default_itinerary
from data.storage import sync_state
from data.cities import get_supported_cities

def display_itinerary():
    """Affiche la page de gestion de l'itinéraire"""
    st.header("🗺️ Gestion de l'itinéraire")
    data = st.session_state.data
    
    # Bouton pour générer l'itinéraire par défaut
    if not data.get("itinerary"):
        st.info("💡 Vous n'avez pas encore d'itinéraire. Cliquez sur le bouton ci-dessous pour générer un itinéraire par défaut basé sur votre profil de voyage !")
        
        if st.button("🚀 Générer l'itinéraire par défaut", type="primary"):
            data["itinerary"] = get_default_itinerary()
            data["departure_date"] = "2026-04-19"  # Date de départ du profil
            sync_state()
            st.success("Itinéraire par défaut généré ! Il est basé sur votre profil de voyage et inclut : Tokyo, Hakone, Kyoto, Osaka.")
            st.rerun()
    
    # Liste des villes japonaises populaires
    japanese_cities = get_supported_cities()
    
    with st.form("add_step"):
        col1, col2 = st.columns(2)
        with col1:
            date_step = st.date_input("Date", value=date(2026, 4, 18))
        with col2:
            city = st.selectbox("Ville / Lieu", options=[""] + japanese_cities, index=0)
        activities = st.text_area("Activités prévues")
        lodging = st.text_input("Hébergement (nom/lien)")
        submitted = st.form_submit_button("Ajouter l'étape")
        if submitted and city:
            data["itinerary"].append({
                "date": str(date_step),
                "city": city,
                "activities": activities,
                "lodging": lodging
            })
            # Si la date de départ n'est pas définie, la définir au premier ajout
            if not data["departure_date"]:
                data["departure_date"] = str(date_step)
            sync_state()
            st.success("Étape ajoutée !")
            st.rerun()
    
    # Affichage de l'itinéraire
    if data["itinerary"]:
        st.subheader("Votre itinéraire")
        df = pd.DataFrame(data["itinerary"])
        df = df.sort_values("date")
        for idx, row in df.iterrows():
            with st.expander(f"{row['date']} - {row['city']}"):
                st.markdown(f"**Activités :** {row['activities']}")
                st.markdown(f"**Hébergement :** {row['lodging']}")
                if st.button(f"Supprimer cette étape", key=f"del_{idx}"):
                    data["itinerary"].pop(idx)
                    sync_state()
                    st.rerun()
    else:
        st.info("Aucune étape d'itinéraire pour l'instant.") 