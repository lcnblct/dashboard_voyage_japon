# Page de la checklist
import streamlit as st
import pandas as pd
from data.models import get_default_checklist
from data.storage import sync_state
from utils.helpers import get_progress_percentage

def display_checklist():
    """Affiche la page de la checklist"""
    st.header("✅ Checklist de Préparation")
    data = st.session_state.data
    checklist = data.get("checklist", get_default_checklist())
    
    # Calcul de la progression
    total_items = len(checklist)
    completed_items = sum(checklist.values())
    progress_percentage = get_progress_percentage(completed_items, total_items)
    
    # Affichage de la progression
    st.subheader(f"📊 Progression : {completed_items}/{total_items} ({progress_percentage:.1f}%)")
    st.progress(progress_percentage / 100)
    
    # Groupes de la checklist
    groups = {
        "📋 Documents Essentiels": [
            "passeport_valide", "billet_avion", "jr_pass", "permis_conduire",
            "assurance", "carte_credit", "especes_yen"
        ],
        "📱 Électronique": [
            "adaptateur", "chargeur_telephone", "batterie_externe", "appareil_photo", "carte_sd"
        ],
        "🧳 Bagages": [
            "valise", "vetements", "chaussures_confortables", "sous_vetements",
            "pyjama", "serviette", "produits_hygiene", "trousse_secours",
            "medicaments", "lunettes_contact"
        ],
        "📄 Préparatifs Administratifs": [
            "banque", "copie_documents", "photos_identite", "adresse_hotel", "itineraire_imprime"
        ],
        "📱 Applications Utiles": [
            "app_transport", "app_traduction", "app_meteo", "app_maps"
        ],
        "🎯 Préparatifs Pratiques": [
            "reservation_hotels", "reservation_restaurants", "activites_reservees",
            "transport_aeroport", "guide_phrase"
        ]
    }
    
    # Labels pour l'affichage
    labels = {
        "passeport_valide": "Passeport valide (6 mois après retour)",
        "billet_avion": "Billet d'avion imprimé/PDF",
        "jr_pass": "Réservation JR Pass",
        "permis_conduire": "Permis de conduire international",
        "assurance": "Assurance voyage",
        "carte_credit": "Carte bancaire internationale",
        "especes_yen": "Prévoir des espèces en yen",
        "adaptateur": "Adaptateur secteur Type A/B",
        "chargeur_telephone": "Chargeur téléphone",
        "batterie_externe": "Batterie externe",
        "appareil_photo": "Appareil photo",
        "carte_sd": "Carte SD de rechange",
        "valise": "Valise/sac à dos",
        "vetements": "Vêtements adaptés à la saison",
        "chaussures_confortables": "Chaussures confortables",
        "sous_vetements": "Sous-vêtements",
        "pyjama": "Pyjama",
        "serviette": "Serviette de toilette",
        "produits_hygiene": "Produits d'hygiène",
        "trousse_secours": "Trousse de premiers secours",
        "medicaments": "Médicaments personnels",
        "lunettes_contact": "Lunettes/contacts de rechange",
        "banque": "Prévenir sa banque",
        "copie_documents": "Copies numériques des documents",
        "photos_identite": "Photos d'identité",
        "adresse_hotel": "Adresses des hôtels notées",
        "itineraire_imprime": "Itinéraire imprimé",
        "app_transport": "App transport (Hyperdia, Google Maps)",
        "app_traduction": "App traduction (Google Translate)",
        "app_meteo": "App météo",
        "app_maps": "App cartes hors ligne",
        "reservation_hotels": "Réservations hôtels confirmées",
        "reservation_restaurants": "Réservations restaurants",
        "activites_reservees": "Activités réservées",
        "transport_aeroport": "Transport aéroport organisé",
        "guide_phrase": "Guide de phrases japonaises"
    }
    
    # Affichage par groupes
    for group_name, items in groups.items():
        st.subheader(group_name)
        
        # Calcul de la progression du groupe
        group_completed = sum(checklist[item] for item in items)
        group_total = len(items)
        group_progress = get_progress_percentage(group_completed, group_total)
        
        st.caption(f"Progression du groupe : {group_completed}/{group_total} ({group_progress:.1f}%)")
        
        # Affichage des items
        for item in items:
            col1, col2 = st.columns([1, 4])
            with col1:
                if st.checkbox("", value=checklist[item], key=f"check_{item}"):
                    checklist[item] = True
                else:
                    checklist[item] = False
            with col2:
                st.write(labels.get(item, item))
        
        st.divider()
    
    # Bouton de réinitialisation
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Réinitialiser la checklist", type="secondary"):
            data["checklist"] = get_default_checklist()
            sync_state()
            st.success("Checklist réinitialisée !")
            st.rerun()
    
    with col2:
        if st.button("💾 Sauvegarder", type="primary"):
            sync_state()
            st.success("Checklist sauvegardée !")
    
    # Message de félicitations si tout est complété
    if completed_items == total_items and total_items > 0:
        st.success("🎊 Félicitations ! Toutes les tâches de la checklist sont complétées !") 