# Page d'accueil
import streamlit as st
import pandas as pd
from datetime import datetime, date
from data.models import get_default_travel_profile
from utils.helpers import calculate_days_until_departure, get_progress_percentage, format_currency

def display_home():
    """Affiche la page d'accueil avec le tableau de bord"""
    st.title("Tableau de Bord pour votre voyage au Japon 🇯🇵")
    data = st.session_state.data
    
    # Affichage du profil de voyage
    profile = data.get("travel_profile", get_default_travel_profile())
    
    # Métriques principales
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Date de départ
        dep_date = data.get("departure_date") or profile.get("arrival_date")
        if dep_date:
            days_left = calculate_days_until_departure(dep_date)
            if days_left is not None:
                st.metric("Jours restants avant le départ", f"{days_left} jours" if days_left >= 0 else "Départ passé")
            else:
                st.info("Veuillez renseigner la date de départ dans l'itinéraire.")
        else:
            st.info("Veuillez renseigner la date de départ dans l'itinéraire.")
    
    with col2:
        # Budget
        total = sum([b["amount"] for b in data.get("budget", [])])
        budget_per_day = profile.get("budget_per_day", 150)
        st.metric("Budget total dépensé", format_currency(total))
        st.caption(f"Budget cible : {budget_per_day}€/jour")
    
    with col3:
        # Progression checklist
        checklist = data.get("checklist", {})
        total_items = len(checklist)
        completed_items = sum(checklist.values())
        progress_percentage = get_progress_percentage(completed_items, total_items)
        st.metric("Progression checklist", f"{completed_items}/{total_items} ({progress_percentage:.1f}%)")
    
    # Résumé du profil de voyage
    st.subheader("👥 Votre Profil de Voyage")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Voyageurs :** {profile.get('travelers', 'Non défini')}")
        st.info(f"**Expérience :** {profile.get('experience', 'Non défini')}")
        st.info(f"**Priorité N°1 :** {profile.get('priority_1', 'Non définie')}")
    
    with col2:
        st.info(f"**Rythme :** {profile.get('travel_rhythm', 3)}/5 (1=très cool, 5=très intense)")
        st.info(f"**Tolérance foule :** {profile.get('crowd_tolerance', 3)}/5 (1=je fuis, 5=ça me stimule)")
        st.info(f"**Intérêt musées :** {profile.get('museums_interest', 3)}/5")
    
    # Recommandations rapides basées sur le profil
    st.subheader("🎯 Recommandations Rapides")
    
    recommendations = []
    
    if profile.get("museums_interest", 3) >= 4:
        recommendations.append("🏛️ **Musées prioritaires** : Musée national de Tokyo, Musée Ghibli")
    
    if profile.get("modern_architecture", 3) >= 4:
        recommendations.append("🏢 **Architecture moderne** : Tokyo Skytree, Shibuya Scramble")
    
    if profile.get("hiking_interest", 3) >= 4:
        recommendations.append("🏔️ **Randonnées** : Mont Takao, Alpes japonaises")
    
    if profile.get("onsen_importance", 3) >= 4:
        recommendations.append("♨️ **Onsen** : Hakone, Kusatsu")
    
    if "Sumo" in profile.get("specific_interests", ""):
        recommendations.append("🤼 **Sumo** : Réservation obligatoire pour les tournois")
    
    if profile.get("travel_rhythm", 3) >= 4:
        recommendations.append("⚡ **Rythme intense** : Planifier 2-3 activités par jour")
    
    # Affichage des recommandations
    if recommendations:
        for rec in recommendations[:3]:  # Limiter à 3 recommandations principales
            st.info(rec)
    else:
        st.info("Complétez votre profil de voyage pour recevoir des recommandations personnalisées !")
    
    # Prochaine tâche prioritaire
    checklist_labels = [
        # Documents essentiels
        ("passeport_valide", "Passeport valide (6 mois après retour)"),
        ("billet_avion", "Billet d'avion imprimé/PDF"),
        ("jr_pass", "Réservation JR Pass"),
        ("permis_conduire", "Permis de conduire international"),
        ("assurance", "Assurance voyage"),
        ("carte_credit", "Carte bancaire internationale"),
        ("especes_yen", "Prévoir des espèces en yen"),
        
        # Électronique
        ("adaptateur", "Adaptateur secteur Type A/B"),
        ("chargeur_telephone", "Chargeur téléphone"),
        ("batterie_externe", "Batterie externe"),
        ("appareil_photo", "Appareil photo"),
        ("carte_sd", "Carte SD de rechange"),
        
        # Bagages
        ("valise", "Valise/sac à dos"),
        ("vetements", "Vêtements adaptés à la saison"),
        ("chaussures_confortables", "Chaussures confortables"),
        ("sous_vetements", "Sous-vêtements"),
        ("pyjama", "Pyjama"),
        ("serviette", "Serviette de toilette"),
        ("produits_hygiene", "Produits d'hygiène"),
        ("trousse_secours", "Trousse de premiers secours"),
        ("medicaments", "Médicaments personnels"),
        ("lunettes_contact", "Lunettes/contacts de rechange"),
        
        # Préparatifs administratifs
        ("banque", "Prévenir sa banque"),
        ("copie_documents", "Copies numériques des documents"),
        ("photos_identite", "Photos d'identité"),
        ("adresse_hotel", "Adresses des hôtels notées"),
        ("itineraire_imprime", "Itinéraire imprimé"),
        
        # Applications utiles
        ("app_transport", "App transport (Hyperdia, Google Maps)"),
        ("app_traduction", "App traduction (Google Translate)"),
        ("app_meteo", "App météo"),
        ("app_maps", "App cartes hors ligne"),
        
        # Préparatifs pratiques
        ("reservation_hotels", "Réservations hôtels confirmées"),
        ("reservation_restaurants", "Réservations restaurants"),
        ("activites_reservees", "Activités réservées"),
        ("transport_aeroport", "Transport aéroport organisé"),
        ("guide_phrase", "Guide de phrases japonaises")
    ]
    
    next_task = next((label for key, label in checklist_labels if not checklist.get(key)), None)
    if next_task:
        st.warning(f"🎯 Prochaine tâche à faire : {next_task}")
    elif completed_items == total_items and total_items > 0:
        st.success("🎊 Toutes les tâches de la checklist sont complétées !") 