# Page du profil de voyage
import streamlit as st
from datetime import datetime
from data.models import get_default_travel_profile
from data.storage import sync_state

def display_travel_profile():
    """Affiche la page du profil de voyage"""
    st.header("👥 Profil de Voyage Personnalisé")
    data = st.session_state.data
    profile = data.get("travel_profile", get_default_travel_profile())
    
    # Informations de base
    st.subheader("📋 Informations de Base")
    col1, col2 = st.columns(2)
    with col1:
        profile["travelers"] = st.text_input("Voyageurs", value=profile["travelers"])
        profile["arrival_date"] = st.date_input("Date d'arrivée", value=datetime.strptime(profile["arrival_date"], "%Y-%m-%d").date()).strftime("%Y-%m-%d")
        profile["experience"] = st.selectbox("Expérience au Japon", ["Première fois", "Déjà visité", "Expérimenté"], index=0 if profile["experience"] == "Première fois" else 1)
    with col2:
        profile["budget_per_day"] = st.number_input("Budget par jour (€)", min_value=50, max_value=500, value=profile["budget_per_day"])
        profile["current_reservations"] = st.text_input("Réservations actuelles", value=profile["current_reservations"])
        profile["constraints"] = st.text_input("Contraintes spécifiques", value=profile["constraints"])
    
    # Préférences géographiques
    st.subheader("🗺️ Préférences Géographiques")
    col1, col2 = st.columns(2)
    with col1:
        profile["geographic_orientation"] = st.text_input("Orientation géographique", value=profile["geographic_orientation"])
        profile["priority_1"] = st.text_input("Priorité N°1 du voyage", value=profile["priority_1"])
    with col2:
        profile["importance_cliches"] = st.slider("Importance des symboles 'clichés'", 1, 5, profile["importance_cliches"])
    
    # Rythme et style
    st.subheader("⚡ Rythme et Style de Voyage")
    col1, col2 = st.columns(2)
    with col1:
        profile["travel_rhythm"] = st.slider("Rythme général (1=très cool, 5=très intense)", 1, 5, profile["travel_rhythm"])
        profile["planning_preference"] = st.slider("Préférence planning (1=100% impro, 5=tout planifié)", 1, 5, profile["planning_preference"])
        profile["morning_evening"] = st.slider("Matin ou soir (1=oiseau de nuit, 5=lève-tôt)", 1, 5, profile["morning_evening"])
    with col2:
        profile["crowd_tolerance"] = st.slider("Tolérance à la foule (1=je fuis, 5=ça me stimule)", 1, 5, profile["crowd_tolerance"])
        profile["local_interaction"] = st.slider("Interaction avec locaux (1=observateur, 5=prêt à engager)", 1, 5, profile["local_interaction"])
        profile["city_transport"] = st.text_input("Déplacements en ville", value=profile["city_transport"])
    
    profile["golden_week_strategy"] = st.text_input("Stratégie Golden Week", value=profile["golden_week_strategy"])
    
    # Hébergement
    st.subheader("🏨 Hébergement")
    col1, col2 = st.columns(2)
    with col1:
        profile["accommodation_style"] = st.text_input("Style d'hébergement", value=profile["accommodation_style"])
        profile["ryokan_interest"] = st.slider("Intérêt Ryokan (1=pas intéressé, 5=incontournable)", 1, 5, profile["ryokan_interest"])
        profile["onsen_importance"] = st.slider("Importance onsen (1=pas important, 5=critère essentiel)", 1, 5, profile["onsen_importance"])
    with col2:
        profile["tattoos"] = st.selectbox("Tatouages", ["Non", "Oui"], index=0 if "Non" in profile["tattoos"] else 1)
        profile["hotel_location"] = st.text_input("Emplacement hôtel", value=profile["hotel_location"])
        profile["jr_pass_strategy"] = st.text_input("Stratégie JR Pass", value=profile["jr_pass_strategy"])
    
    profile["long_distance"] = st.text_input("Voyages longue distance", value=profile["long_distance"])
    profile["internet_need"] = st.text_input("Besoin Internet", value=profile["internet_need"])
    
    # Nourriture
    st.subheader("🍜 Nourriture et Boissons")
    col1, col2 = st.columns(2)
    with col1:
        profile["cuisine_preferences"] = st.text_input("Préférences cuisine", value=profile["cuisine_preferences"])
        profile["restaurant_adventure"] = st.slider("Aventure restaurants (1=menu anglais, 5=aventure totale)", 1, 5, profile["restaurant_adventure"])
    with col2:
        profile["local_drinks"] = st.slider("Intérêt boissons locales (1=pas intéressé, 5=très curieux)", 1, 5, profile["local_drinks"])
        profile["sweet_breaks"] = st.slider("Importance pauses sucrées (1=pas mon truc, 5=priorité)", 1, 5, profile["sweet_breaks"])
    
    # Centres d'intérêt
    st.subheader("🎯 Centres d'Intérêt")
    
    # Culture et histoire
    st.markdown("**Culture & Histoire**")
    col1, col2 = st.columns(2)
    with col1:
        profile["temples_interest"] = st.slider("Temples et sanctuaires (1=juste majeurs, 5=le plus possible)", 1, 5, profile["temples_interest"])
        profile["castles_interest"] = st.slider("Châteaux samouraïs (1=pas priorité, 5=incontournable)", 1, 5, profile["castles_interest"])
        profile["museums_interest"] = st.slider("Musées (1=préfère dehors, 5=passionné)", 1, 5, profile["museums_interest"])
    with col2:
        profile["ww2_history"] = st.text_input("Histoire XXe siècle", value=profile["ww2_history"])
        profile["traditional_workshops"] = st.slider("Ateliers traditionnels (1=observer, 5=essayer)", 1, 5, profile["traditional_workshops"])
    
    # Pop culture et vie urbaine
    st.markdown("**Pop Culture & Vie Urbaine**")
    col1, col2 = st.columns(2)
    with col1:
        profile["manga_anime"] = st.slider("Manga/Anime (1=aucun, 5=otaku confirmé)", 1, 5, profile["manga_anime"])
        profile["gaming"] = st.slider("Jeux vidéo (1=pas du tout, 5=à fond)", 1, 5, profile["gaming"])
        profile["modern_architecture"] = st.slider("Architecture moderne (1=préfère ancien, 5=j'adore)", 1, 5, profile["modern_architecture"])
    with col2:
        profile["nightlife"] = st.text_input("Vie nocturne", value=profile["nightlife"])
        profile["unusual_experiences"] = st.slider("Expériences insolites (1=très peu, 5=on est là pour ça)", 1, 5, profile["unusual_experiences"])
        profile["contemporary_art"] = st.slider("Art contemporain (1=pas mon truc, 5=passionné)", 1, 5, profile["contemporary_art"])
    
    # Nature et extérieur
    st.markdown("**Nature & Extérieur**")
    col1, col2 = st.columns(2)
    with col1:
        profile["nature_importance"] = st.slider("Importance nature (1=préfère ville, 5=essentiel)", 1, 5, profile["nature_importance"])
        profile["hiking_interest"] = st.slider("Randonnées (1=pas du tout, 5=passionné)", 1, 5, profile["hiking_interest"])
    with col2:
        profile["japanese_gardens"] = st.slider("Jardins japonais (1=pas priorité, 5=incontournable)", 1, 5, profile["japanese_gardens"])
        profile["coastal_landscapes"] = st.slider("Paysages côtiers (1=pas intéressé, 5=très important)", 1, 5, profile["coastal_landscapes"])
    
    # Shopping et spécificités
    st.subheader("🛍️ Shopping et Spécificités")
    col1, col2 = st.columns(2)
    with col1:
        profile["shopping"] = st.text_input("Shopping", value=profile["shopping"])
        profile["photography"] = st.slider("Photographie (1=pas du tout, 5=passionné)", 1, 5, profile["photography"])
    with col2:
        profile["specific_interests"] = st.text_input("Intérêts spécifiques", value=profile["specific_interests"])
        profile["activities_to_avoid"] = st.text_input("Activités à éviter", value=profile["activities_to_avoid"])
    
    # Format et attentes
    st.subheader("📝 Format et Attentes")
    profile["detail_level"] = st.text_input("Niveau de détail souhaité", value=profile["detail_level"])
    profile["important_advice"] = st.text_input("Conseils importants", value=profile["important_advice"])
    
    # Bouton de sauvegarde
    if st.button("💾 Sauvegarder le profil", type="primary"):
        data["travel_profile"] = profile
        sync_state()
        st.success("Profil sauvegardé avec succès !") 