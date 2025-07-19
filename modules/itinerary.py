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
                
                # Boutons d'action
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"✏️ Modifier", key=f"edit_{idx}"):
                        st.session_state.editing_step = idx
                        st.rerun()
                with col2:
                    if st.button(f"🗑️ Supprimer", key=f"del_{idx}"):
                        data["itinerary"].pop(idx)
                        sync_state()
                        st.rerun()
                
                # Formulaire d'édition
                if st.session_state.get("editing_step") == idx:
                    st.markdown("---")
                    st.markdown("**Modifier cette étape :**")
                    
                    with st.form(f"edit_step_{idx}"):
                        # Convertir la date string en date object pour l'input
                        current_date = date.fromisoformat(row['date'])
                        col1, col2 = st.columns(2)
                        with col1:
                            new_date = st.date_input("Date", value=current_date, key=f"edit_date_{idx}")
                        with col2:
                            # Trouver l'index de la ville actuelle dans la liste
                            current_city_index = 0
                            if row['city'] in japanese_cities:
                                current_city_index = japanese_cities.index(row['city']) + 1
                            new_city = st.selectbox("Ville / Lieu", options=[""] + japanese_cities, index=current_city_index, key=f"edit_city_{idx}")
                        
                        new_activities = st.text_area("Activités prévues", value=row['activities'], key=f"edit_activities_{idx}")
                        new_lodging = st.text_input("Hébergement (nom/lien)", value=row['lodging'], key=f"edit_lodging_{idx}")
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            if st.form_submit_button("💾 Sauvegarder"):
                                data["itinerary"][idx] = {
                                    "date": str(new_date),
                                    "city": new_city,
                                    "activities": new_activities,
                                    "lodging": new_lodging
                                }
                                sync_state()
                                st.session_state.editing_step = None
                                st.success("Étape modifiée avec succès !")
                                st.rerun()
                        with col2:
                            if st.form_submit_button("❌ Annuler"):
                                st.session_state.editing_step = None
                                st.rerun()
    else:
        st.info("Aucune étape d'itinéraire pour l'instant.") 