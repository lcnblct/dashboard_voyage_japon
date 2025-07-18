# Dépendances nécessaires (pour requirements.txt) :
# streamlit
# pandas
# folium
# streamlit-folium
# (et json, inclus dans la stdlib)

import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime, date
import folium
from streamlit_folium import st_folium

# Configuration du thème sombre
st.set_page_config(
    page_title="Dashboard Voyage Japon",
    page_icon="🇯🇵",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "Dashboard de préparation de voyage au Japon 🇯🇵"
    }
)

# Configuration du thème sombre
st.markdown("""
<style>
    /* Configuration du thème sombre */
    .stApp {
        background-color: #0e1117;
        color: #fafafa;
    }
    
    /* Sidebar sombre */
    .css-1d391kg {
        background-color: #262730;
    }
    
    /* Titres */
    h1, h2, h3, h4, h5, h6 {
        color: #fafafa !important;
    }
    
    /* Texte */
    p, div, span {
        color: #fafafa !important;
    }
    
    /* Métriques */
    .metric-container {
        background-color: #262730;
        border-radius: 8px;
        padding: 10px;
        margin: 5px 0;
    }
    
    /* Cartes et conteneurs */
    .stAlert {
        background-color: #262730 !important;
        border: 1px solid #4a4a4a !important;
    }
    
    /* Dataframes */
    .dataframe {
        background-color: #262730 !important;
        color: #fafafa !important;
    }
    
    /* Formulaires */
    .stTextInput, .stSelectbox, .stNumberInput, .stDateInput, .stTimeInput {
        background-color: #262730 !important;
        color: #fafafa !important;
    }
    
    /* Boutons */
    .stButton > button {
        background-color: #4CAF50 !important;
        color: white !important;
        border: none !important;
    }
    
    .stButton > button:hover {
        background-color: #45a049 !important;
    }
    
    /* Sliders */
    .stSlider {
        background-color: #262730 !important;
    }
    
    /* Checkboxes */
    .stCheckbox {
        background-color: #262730 !important;
        color: #fafafa !important;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background-color: #262730 !important;
        color: #fafafa !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #262730 !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #262730 !important;
        color: #fafafa !important;
    }
    
    /* Progress bars */
    .stProgress > div > div > div > div {
        background-color: #4CAF50 !important;
    }
    
    /* Info boxes */
    .stInfo {
        background-color: #1e3a8a !important;
        border: 1px solid #3b82f6 !important;
    }
    
    .stSuccess {
        background-color: #166534 !important;
        border: 1px solid #22c55e !important;
    }
    
    .stWarning {
        background-color: #92400e !important;
        border: 1px solid #f59e0b !important;
    }
    
    .stError {
        background-color: #991b1b !important;
        border: 1px solid #ef4444 !important;
    }
    
    /* Calendrier personnalisé */
    .calendar-card {
        background-color: #262730 !important;
        border: 2px solid #4CAF50 !important;
        color: #fafafa !important;
    }
    
    .calendar-date {
        color: #4CAF50 !important;
        font-weight: bold !important;
    }
    
    .calendar-city {
        color: #f97316 !important;
        font-weight: bold !important;
    }
    
    .calendar-activities {
        background-color: #1e293b !important;
        border-left: 4px solid #3b82f6 !important;
        color: #fafafa !important;
    }
    
    .calendar-lodging {
        background-color: #1e293b !important;
        border-left: 4px solid #f59e0b !important;
        color: #fafafa !important;
    }
</style>
""", unsafe_allow_html=True)

DATA_FILE = "data.json"

# --- Fonctions utilitaires pour la persistance ---
def get_default_checklist():
    """Retourne la checklist complète par défaut"""
    return {
        # Documents essentiels
        "passeport_valide": False,
        "billet_avion": False,
        "jr_pass": False,
        "permis_conduire": False,
        "assurance": False,
        "carte_credit": False,
        "especes_yen": False,
        
        # Électronique
        "adaptateur": False,
        "chargeur_telephone": False,
        "batterie_externe": False,
        "appareil_photo": False,
        "carte_sd": False,
        
        # Bagages
        "valise": False,
        "vetements": False,
        "chaussures_confortables": False,
        "sous_vetements": False,
        "pyjama": False,
        "serviette": False,
        "produits_hygiene": False,
        "trousse_secours": False,
        "medicaments": False,
        "lunettes_contact": False,
        
        # Préparatifs administratifs
        "banque": False,
        "copie_documents": False,
        "photos_identite": False,
        "adresse_hotel": False,
        "itineraire_imprime": False,
        
        # Applications utiles
        "app_transport": False,
        "app_traduction": False,
        "app_meteo": False,
        "app_maps": False,
        
        # Préparatifs pratiques
        "reservation_hotels": False,
        "reservation_restaurants": False,
        "activites_reservees": False,
        "transport_aeroport": False,
        "guide_phrase": False
    }

def get_default_travel_profile():
    """Retourne le profil de voyage par défaut basé sur le questionnaire"""
    return {
        # Informations de base
        "travelers": "Deux frères, 28 et 30 ans, français",
        "arrival_date": "2026-04-19",
        "departure_date": "2026-05-02",
        "experience": "Première fois",
        "budget_per_day": 150,  # € par personne
        "current_reservations": "Aucune",
        "constraints": "Aucune contrainte particulière",
        
        # Préférences géographiques
        "geographic_orientation": "Route d'Or classique (Tokyo-Kyoto-Osaka) + Alpes Japonaises",
        "priority_1": "Ambiance urbaine, néons et vie nocturne",
        "importance_cliches": 3,  # 1-5 échelle
        
        # Rythme et style
        "travel_rhythm": 4,  # 1-5 échelle
        "planning_preference": 4,  # 1-5 échelle
        "morning_evening": 3,  # 1-5 échelle
        "crowd_tolerance": 3,  # 1-5 échelle
        "golden_week_strategy": "Mix : voir les grands sites avec des stratégies pour éviter les pics",
        "local_interaction": 2,  # 1-5 échelle
        "city_transport": "Prêt à marcher beaucoup pour s'imprégner des quartiers",
        "special_needs": "Non",
        
        # Hébergement
        "accommodation_style": "Mix : Auberges + 1 ou 2 nuits de luxe",
        "ryokan_interest": 1,  # 1-5 échelle
        "onsen_importance": 4,  # 1-5 échelle
        "tattoos": "Non, aucun tatouage",
        "hotel_location": "En plein cœur de l'action (bruyant mais pratique)",
        "jr_pass_strategy": "JSP, conseillez-moi la meilleure stratégie globale",
        "long_distance": "Shinkansen prioritairement, pour l'expérience et le confort",
        "internet_need": "Connexion permanente indispensable",
        
        # Nourriture
        "cuisine_preferences": "Sushi/Sashimi, Ramen/Udon, Street food (Takoyaki...)",
        "restaurant_adventure": 5,  # 1-5 échelle
        "local_drinks": 1,  # 1-5 échelle
        "sweet_breaks": 1,  # 1-5 échelle
        
        # Culture et histoire
        "temples_interest": 2,  # 1-5 échelle
        "castles_interest": 1,  # 1-5 échelle
        "museums_interest": 5,  # 1-5 échelle
        "ww2_history": "Je préfère éviter les visites à forte charge émotionnelle",
        "traditional_workshops": 1,  # 1-5 échelle
        
        # Pop culture et vie urbaine
        "manga_anime": 3,  # 1-5 échelle
        "gaming": 3,  # 1-5 échelle
        "nightlife": "Karaoké entre amis, Petits bars conviviaux (Izakaya), Ruelles typiques",
        "modern_architecture": 5,  # 1-5 échelle
        "unusual_experiences": 3,  # 1-5 échelle
        "contemporary_art": 1,  # 1-5 échelle
        
        # Nature et extérieur
        "nature_importance": 3,  # 1-5 échelle
        "hiking_interest": 5,  # 1-5 échelle
        "japanese_gardens": 4,  # 1-5 échelle
        "coastal_landscapes": 2,  # 1-5 échelle
        
        # Shopping et spécificités
        "shopping": "Pas de shopping prévu",
        "photography": 1,  # 1-5 échelle
        "specific_interests": "Aller voir un combat de Sumo",
        "activities_to_avoid": "Rien",
        
        # Format et attentes
        "detail_level": "Une liste d'activités pour le matin/après-midi/soir",
        "important_advice": "Transport, Budget détaillé, Savoir-vivre, Réservations, Alternatives, Lexique japonais"
    }

def get_default_itinerary():
    """Retourne un itinéraire par défaut basé sur le profil de voyage"""
    return [
        {
            "date": "2026-04-19",
            "city": "Tokyo",
            "activities": "Arrivée à l'aéroport de Narita/Haneda. Transfert vers Tokyo. Installation à l'hôtel. Première découverte : Shibuya Crossing et quartier Shibuya. Dîner dans un Izakaya local.",
            "lodging": "Hôtel à Shibuya ou Shinjuku"
        },
        {
            "date": "2026-04-20",
            "city": "Tokyo",
            "activities": "Matin : Musée national de Tokyo. Après-midi : Asakusa (Senso-ji), Tokyo Skytree. Soirée : Akihabara pour la pop culture et les jeux vidéo.",
            "lodging": "Hôtel à Shibuya ou Shinjuku"
        },
        {
            "date": "2026-04-21",
            "city": "Tokyo",
            "activities": "Matin : Musée Ghibli (réservation obligatoire). Après-midi : Harajuku et Takeshita Street. Soirée : Karaoké dans le quartier.",
            "lodging": "Hôtel à Shibuya ou Shinjuku"
        },
        {
            "date": "2026-04-22",
            "city": "Tokyo",
            "activities": "Matin : TeamLab Planets (art numérique). Après-midi : Odaiba et Rainbow Bridge. Soirée : Shinjuku Golden Gai pour les bars typiques.",
            "lodging": "Hôtel à Shibuya ou Shinjuku"
        },
        {
            "date": "2026-04-23",
            "city": "Hakone",
            "activities": "Départ pour Hakone en train. Randonnée sur le sentier Hakone. Visite des onsen (bains thermaux). Nuit dans un ryokan avec onsen privé.",
            "lodging": "Ryokan avec onsen à Hakone"
        },
        {
            "date": "2026-04-24",
            "city": "Hakone",
            "activities": "Matin : Croisière sur le lac Ashi, vue sur le Mont Fuji. Après-midi : Musée en plein air de Hakone. Retour à Tokyo en soirée.",
            "lodging": "Hôtel à Tokyo"
        },
        {
            "date": "2026-04-25",
            "city": "Tokyo",
            "activities": "Matin : Mont Takao (randonnée facile avec vue sur Tokyo). Après-midi : Roppongi Hills et Mori Art Museum. Soirée : Quartier de Roppongi.",
            "lodging": "Hôtel à Tokyo"
        },
        {
            "date": "2026-04-26",
            "city": "Kyoto",
            "activities": "Départ pour Kyoto en Shinkansen. Installation. Après-midi : Fushimi Inari (moins de monde en fin de journée). Soirée : Gion pour apercevoir des geishas.",
            "lodging": "Hôtel à Kyoto (centre-ville)"
        },
        {
            "date": "2026-04-27",
            "city": "Kyoto",
            "activities": "Matin : Arashiyama (bambouseraie, pont Togetsukyo). Après-midi : Ryoan-ji (jardin zen), Kinkaku-ji (pavillon d'or). Soirée : Pontocho pour dîner.",
            "lodging": "Hôtel à Kyoto (centre-ville)"
        },
        {
            "date": "2026-04-28",
            "city": "Kyoto",
            "activities": "Matin : Sentier du philosophe, temples Ginkaku-ji et Nanzen-ji. Après-midi : Musée national de Kyoto. Soirée : Nijo-jo (château) illuminé.",
            "lodging": "Hôtel à Kyoto (centre-ville)"
        },
        {
            "date": "2026-04-29",
            "city": "Osaka",
            "activities": "Départ pour Osaka. Matin : Château d'Osaka. Après-midi : Dotonbori (quartier animé), street food. Soirée : Umeda Sky Building.",
            "lodging": "Hôtel à Osaka (Namba ou Umeda)"
        },
        {
            "date": "2026-04-30",
            "city": "Osaka",
            "activities": "Matin : Aquarium d'Osaka. Après-midi : Shinsekai, Tsutenkaku. Soirée : Kuromon Market pour les spécialités culinaires.",
            "lodging": "Hôtel à Osaka (Namba ou Umeda)"
        },
        {
            "date": "2026-05-01",
            "city": "Osaka",
            "activities": "Dernière journée à Osaka. Matin : Shopping et dernières courses. Après-midi : Visite du quartier de Tennoji et Abeno Harukas. Soirée : Dernier dîner dans un restaurant local.",
            "lodging": "Hôtel à Osaka (près de l'aéroport KIX)"
        },
        {
            "date": "2026-05-02",
            "city": "Osaka",
            "activities": "Transfert vers l'aéroport Kansai (KIX). Départ pour la France.",
            "lodging": "Vol retour"
        }
    ]

def get_default_flight_info():
    """Retourne les informations de vol par défaut"""
    return {
        "outbound": {
            "airline": "",
            "flight_number": "",
            "departure_airport": "CDG",
            "arrival_airport": "NRT",
            "departure_date": "2026-04-19",
            "departure_time": "10:00",
            "arrival_time": "07:00",
            "terminal_departure": "",
            "terminal_arrival": "",
            "booking_reference": "",
            "checked_in": False,
            "boarding_pass": False
        },
        "return": {
            "airline": "",
            "flight_number": "",
            "departure_airport": "KIX",
            "arrival_airport": "CDG",
            "departure_date": "2026-05-02",
            "departure_time": "11:00",
            "arrival_time": "16:00",
            "terminal_departure": "",
            "terminal_arrival": "",
            "booking_reference": "",
            "checked_in": False,
            "boarding_pass": False
        },
        "notes": "",
        "baggage_allowance": "",
        "seat_selection": False,
        "meal_preference": "",
        "special_assistance": ""
    }

def get_default_budget_planning():
    """Retourne le budget prévisionnel par défaut basé sur le profil de voyage"""
    return {
        "transport": {
            "flights": {"budget": 2000, "description": "Billets d'avion aller-retour"},
            "jr_pass": {"budget": 300, "description": "Japan Rail Pass 7 jours"},
            "local_transport": {"budget": 150, "description": "Métro, bus, taxis locaux"},
            "airport_transfer": {"budget": 80, "description": "Transferts aéroport"}
        },
        "accommodation": {
            "hotels": {"budget": 900, "description": "Hôtels standards (12 nuits)"},
            "ryokan": {"budget": 250, "description": "1 nuit en ryokan avec onsen"},
            "hostels": {"budget": 350, "description": "Auberges de jeunesse"}
        },
        "food": {
            "restaurants": {"budget": 450, "description": "Restaurants midi/soir"},
            "street_food": {"budget": 180, "description": "Street food et snacks"},
            "breakfast": {"budget": 120, "description": "Petits-déjeuners"},
            "drinks": {"budget": 100, "description": "Boissons et cafés"}
        },
        "activities": {
            "museums": {"budget": 80, "description": "Entrées musées et sites"},
            "onsen": {"budget": 60, "description": "Bains thermaux"},
            "guided_tours": {"budget": 120, "description": "Visites guidées"},
            "experiences": {"budget": 150, "description": "Expériences culturelles"}
        },
        "shopping": {
            "souvenirs": {"budget": 120, "description": "Souvenirs et cadeaux"},
            "clothing": {"budget": 80, "description": "Vêtements si nécessaire"},
            "electronics": {"budget": 0, "description": "Électronique"}
        },
        "other": {
            "insurance": {"budget": 100, "description": "Assurance voyage"},
            "sim_card": {"budget": 40, "description": "Carte SIM/data"},
            "emergency": {"budget": 120, "description": "Fonds d'urgence"},
            "tips": {"budget": 30, "description": "Pourboires"}
        }
    }

def migrate_checklist(old_checklist):
    """Migre l'ancienne checklist vers le nouveau format"""
    new_checklist = get_default_checklist()
    
    # Copie les valeurs existantes
    for key in old_checklist:
        if key in new_checklist:
            new_checklist[key] = old_checklist[key]
    
    return new_checklist

def load_data():
    if not os.path.exists(DATA_FILE):
        data = {
            "departure_date": None,
            "itinerary": [],
            "budget": [],
            "checklist": get_default_checklist(),
            "travel_profile": get_default_travel_profile(),
            "flight_info": get_default_flight_info()
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
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
            # Sauvegarde les données migrées
            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        
        # Ajout des informations de vol si absent
        if "flight_info" not in data:
            data["flight_info"] = get_default_flight_info()
            # Sauvegarde les données migrées
            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        
        # Ajout du budget prévisionnel si absent
        if "budget_planning" not in data:
            data["budget_planning"] = get_default_budget_planning()
            # Sauvegarde les données migrées
            with open(DATA_FILE, "w") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
    
    return data

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def export_data():
    """Exporte les données au format JSON pour sauvegarde"""
    data = st.session_state.data
    return json.dumps(data, indent=2, ensure_ascii=False)



# --- Initialisation de session_state ---
if "initialized" not in st.session_state:
    st.session_state.data = load_data()
    st.session_state.initialized = True

def sync_state():
    save_data(st.session_state.data)

# --- Protection par mot de passe ---
def check_password():
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

check_password()

# --- Fonctions d'affichage des sections ---
def display_home():
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
            dep_date_obj = datetime.strptime(dep_date, "%Y-%m-%d").date()
            days_left = (dep_date_obj - date.today()).days
            st.metric("Jours restants avant le départ", f"{days_left} jours" if days_left >= 0 else "Départ passé")
        else:
            st.info("Veuillez renseigner la date de départ dans l'itinéraire.")
    
    with col2:
        # Budget
        total = sum([b["amount"] for b in data.get("budget", [])])
        budget_per_day = profile.get("budget_per_day", 150)
        st.metric("Budget total dépensé", f"{total:.2f} €")
        st.caption(f"Budget cible : {budget_per_day}€/jour")
    
    with col3:
        # Progression checklist
        checklist = data.get("checklist", {})
        total_items = len(checklist)
        completed_items = sum(checklist.values())
        progress_percentage = (completed_items / total_items) * 100 if total_items > 0 else 0
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

def display_itinerary():
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
    japanese_cities = [
        "Tokyo", "Kyoto", "Osaka", "Hiroshima", "Nara", "Sapporo", "Fukuoka", 
        "Nagoya", "Kobe", "Yokohama", "Kamakura", "Hakone", "Nikko", "Takayama", 
        "Kanazawa", "Matsumoto", "Nagano", "Sendai", "Matsuyama", "Kumamoto", 
        "Kagoshima", "Okinawa", "Naha", "Shizuoka", "Okayama", "Kurashiki",
        "Himeji", "Miyajima", "Ishigaki", "Kushiro", "Asahikawa", "Akita",
        "Aomori", "Niigata", "Toyama", "Fukui", "Tottori", "Shimane", "Yamaguchi",
        "Tokushima", "Kochi", "Ehime", "Oita", "Miyazaki", "Saga", "Nagasaki"
    ]
    
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

def display_budget():
    st.header("💴 Suivi de Budget")
    data = st.session_state.data
    
    # Onglets pour budget prévisionnel et suivi des dépenses
    tab1, tab2 = st.tabs(["📊 Budget Prévisionnel", "💰 Suivi des Dépenses"])
    
    with tab1:
        st.subheader("🎯 Planification du Budget")
        
        # Récupérer le budget prévisionnel
        budget_planning = data.get("budget_planning", get_default_budget_planning())
        
        # Calculer le total prévisionnel
        total_planned = 0
        for category in budget_planning.values():
            for item in category.values():
                total_planned += item["budget"]
        
        # Affichage du total prévisionnel
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("💰 Budget Total Prévisionnel", f"{total_planned} €")
        with col2:
            profile = data.get("travel_profile", get_default_travel_profile())
            budget_per_day = profile.get("budget_per_day", 150)
            st.metric("📅 Budget/Jour Cible", f"{budget_per_day} €")
        with col3:
            days = 14  # Durée par défaut
            if data.get("itinerary"):
                days = len(data["itinerary"])
            st.metric("📆 Durée du Voyage", f"{days} jours")
        
        # Sliders pour chaque catégorie
        st.markdown("---")
        
        # Transport
        st.subheader("🚗 Transport")
        col1, col2 = st.columns(2)
        with col1:
            budget_planning["transport"]["flights"]["budget"] = st.slider(
                "✈️ Billets d'avion", 
                min_value=800, max_value=2500, value=budget_planning["transport"]["flights"]["budget"], 
                step=50,
                help="Prix moyen pour un aller-retour France-Japon"
            )
            budget_planning["transport"]["jr_pass"]["budget"] = st.slider(
                "🚄 Japan Rail Pass", 
                min_value=200, max_value=500, value=budget_planning["transport"]["jr_pass"]["budget"], 
                step=25,
                help="Prix du JR Pass selon la durée"
            )
        with col2:
            budget_planning["transport"]["local_transport"]["budget"] = st.slider(
                "🚇 Transport local", 
                min_value=50, max_value=300, value=budget_planning["transport"]["local_transport"]["budget"], 
                step=10,
                help="Métro, bus, taxis dans les villes"
            )
            budget_planning["transport"]["airport_transfer"]["budget"] = st.slider(
                "🚌 Transferts aéroport", 
                min_value=30, max_value=150, value=budget_planning["transport"]["airport_transfer"]["budget"], 
                step=10,
                help="Transferts vers/des aéroports"
            )
        
        # Hébergement
        st.subheader("🏨 Hébergement")
        col1, col2 = st.columns(2)
        with col1:
            budget_planning["accommodation"]["hotels"]["budget"] = st.slider(
                "🏢 Hôtels standards", 
                min_value=400, max_value=1500, value=budget_planning["accommodation"]["hotels"]["budget"], 
                step=50,
                help="Hôtels 3-4 étoiles"
            )
            budget_planning["accommodation"]["ryokan"]["budget"] = st.slider(
                "♨️ Ryokan avec onsen", 
                min_value=100, max_value=400, value=budget_planning["accommodation"]["ryokan"]["budget"], 
                step=25,
                help="Nuit en ryokan traditionnel"
            )
        with col2:
            budget_planning["accommodation"]["hostels"]["budget"] = st.slider(
                "🏠 Auberges", 
                min_value=150, max_value=500, value=budget_planning["accommodation"]["hostels"]["budget"], 
                step=25,
                help="Auberges de jeunesse et guesthouses"
            )
        
        # Nourriture
        st.subheader("🍜 Nourriture")
        col1, col2 = st.columns(2)
        with col1:
            budget_planning["food"]["restaurants"]["budget"] = st.slider(
                "🍽️ Restaurants", 
                min_value=200, max_value=800, value=budget_planning["food"]["restaurants"]["budget"], 
                step=25,
                help="Repas dans les restaurants"
            )
            budget_planning["food"]["street_food"]["budget"] = st.slider(
                "🍡 Street food", 
                min_value=50, max_value=300, value=budget_planning["food"]["street_food"]["budget"], 
                step=10,
                help="Snacks et street food"
            )
        with col2:
            budget_planning["food"]["breakfast"]["budget"] = st.slider(
                "🥐 Petits-déjeuners", 
                min_value=50, max_value=200, value=budget_planning["food"]["breakfast"]["budget"], 
                step=10,
                help="Petits-déjeuners"
            )
            budget_planning["food"]["drinks"]["budget"] = st.slider(
                "🥤 Boissons", 
                min_value=30, max_value=150, value=budget_planning["food"]["drinks"]["budget"], 
                step=10,
                help="Cafés, thés, boissons"
            )
        
        # Activités
        st.subheader("🎯 Activités")
        col1, col2 = st.columns(2)
        with col1:
            budget_planning["activities"]["museums"]["budget"] = st.slider(
                "🏛️ Musées et sites", 
                min_value=20, max_value=150, value=budget_planning["activities"]["museums"]["budget"], 
                step=5,
                help="Entrées musées et sites touristiques"
            )
            budget_planning["activities"]["onsen"]["budget"] = st.slider(
                "♨️ Bains thermaux", 
                min_value=20, max_value=100, value=budget_planning["activities"]["onsen"]["budget"], 
                step=5,
                help="Entrées onsen"
            )
        with col2:
            budget_planning["activities"]["guided_tours"]["budget"] = st.slider(
                "👥 Visites guidées", 
                min_value=50, max_value=200, value=budget_planning["activities"]["guided_tours"]["budget"], 
                step=10,
                help="Visites guidées et tours"
            )
            budget_planning["activities"]["experiences"]["budget"] = st.slider(
                "🎭 Expériences culturelles", 
                min_value=50, max_value=200, value=budget_planning["activities"]["experiences"]["budget"], 
                step=10,
                help="Ateliers, cérémonies, expériences"
            )
        
        # Shopping
        st.subheader("🛍️ Shopping")
        col1, col2 = st.columns(2)
        with col1:
            budget_planning["shopping"]["souvenirs"]["budget"] = st.slider(
                "🎁 Souvenirs", 
                min_value=50, max_value=300, value=budget_planning["shopping"]["souvenirs"]["budget"], 
                step=10,
                help="Souvenirs et cadeaux"
            )
        with col2:
            budget_planning["shopping"]["clothing"]["budget"] = st.slider(
                "👕 Vêtements", 
                min_value=0, max_value=200, value=budget_planning["shopping"]["clothing"]["budget"], 
                step=10,
                help="Vêtements si nécessaire"
            )
        
        # Autres
        st.subheader("📋 Autres")
        col1, col2 = st.columns(2)
        with col1:
            budget_planning["other"]["insurance"]["budget"] = st.slider(
                "🛡️ Assurance voyage", 
                min_value=50, max_value=150, value=budget_planning["other"]["insurance"]["budget"], 
                step=5,
                help="Assurance voyage"
            )
            budget_planning["other"]["sim_card"]["budget"] = st.slider(
                "📱 Carte SIM/Data", 
                min_value=20, max_value=80, value=budget_planning["other"]["sim_card"]["budget"], 
                step=5,
                help="Carte SIM ou data roaming"
            )
        with col2:
            budget_planning["other"]["emergency"]["budget"] = st.slider(
                "🚨 Fonds d'urgence", 
                min_value=50, max_value=200, value=budget_planning["other"]["emergency"]["budget"], 
                step=10,
                help="Fonds de sécurité"
            )
            budget_planning["other"]["tips"]["budget"] = st.slider(
                "💡 Pourboires", 
                min_value=10, max_value=50, value=budget_planning["other"]["tips"]["budget"], 
                step=5,
                help="Pourboires (optionnel au Japon)"
            )
        
        # Recalculer le total
        new_total_planned = 0
        for category in budget_planning.values():
            for item in category.values():
                new_total_planned += item["budget"]
        
        # Affichage du résumé
        st.markdown("---")
        st.subheader("📊 Résumé du Budget Prévisionnel")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("💰 Total Prévisionnel", f"{new_total_planned} €")
            st.metric("📅 Budget/Jour Moyen", f"{new_total_planned/days:.0f} €")
        with col2:
            # Comparaison avec le budget cible
            budget_target = budget_per_day * days
            st.metric("🎯 Budget Cible", f"{budget_target} €")
            difference = new_total_planned - budget_target
            if difference > 0:
                st.error(f"⚠️ Dépassement: +{difference} €")
            else:
                st.success(f"✅ Économies: {abs(difference)} €")
        
        # Répartition par catégorie
        st.subheader("📈 Répartition par Catégorie")
        categories_summary = {
            "Transport": sum(item["budget"] for item in budget_planning["transport"].values()),
            "Hébergement": sum(item["budget"] for item in budget_planning["accommodation"].values()),
            "Nourriture": sum(item["budget"] for item in budget_planning["food"].values()),
            "Activités": sum(item["budget"] for item in budget_planning["activities"].values()),
            "Shopping": sum(item["budget"] for item in budget_planning["shopping"].values()),
            "Autres": sum(item["budget"] for item in budget_planning["other"].values())
        }
        
        # Graphique en barres
        st.bar_chart(categories_summary)
        
        # Bouton de sauvegarde
        if st.button("💾 Sauvegarder le Budget Prévisionnel", type="primary"):
            data["budget_planning"] = budget_planning
            sync_state()
            st.success("Budget prévisionnel sauvegardé !")
    
    with tab2:
        st.subheader("💰 Suivi des Dépenses Réelles")
        
        # Formulaire d'ajout de dépense
        with st.form("add_expense"):
            col1, col2 = st.columns(2)
            with col1:
                description = st.text_input("Description de la dépense")
                category = st.selectbox("Catégorie", ["Transport", "Hébergement", "Nourriture", "Activités", "Shopping", "Autres"])
            with col2:
                amount = st.number_input("Montant (en €)", min_value=0.0, step=0.5)
            submitted = st.form_submit_button("Ajouter la dépense")
            if submitted and description and amount > 0:
                data["budget"].append({
                    "description": description,
                    "amount": float(amount),
                    "category": category
                })
                sync_state()
                st.success("Dépense ajoutée !")
                st.rerun()
        
        # Affichage des dépenses
        if data["budget"]:
            st.subheader("Dépenses enregistrées")
            df = pd.DataFrame(data["budget"])
            st.dataframe(df)
            total_spent = df["amount"].sum()
            st.markdown(f"**Total dépensé : {total_spent:.2f} €**")
            
            # Comparaison avec le budget prévisionnel
            if "budget_planning" in data:
                total_planned = sum(
                    sum(item["budget"] for item in category.values())
                    for category in data["budget_planning"].values()
                )
                remaining = total_planned - total_spent
                if remaining > 0:
                    st.success(f"💰 Budget restant : {remaining:.2f} €")
                else:
                    st.error(f"⚠️ Dépassement : {abs(remaining):.2f} €")
            
            # Dépenses par catégorie
            cat_sum = df.groupby("category")["amount"].sum()
            st.bar_chart(cat_sum)
        else:
            st.info("Aucune dépense enregistrée pour le moment.")

def display_checklist():
    st.header("✅ Checklist de Préparation")
    data = st.session_state.data
    
    # S'assurer que la checklist a toutes les clés nécessaires
    default_checklist = get_default_checklist()
    if "checklist" not in data:
        data["checklist"] = default_checklist
    else:
        # Ajouter les clés manquantes
        for key, default_value in default_checklist.items():
            if key not in data["checklist"]:
                data["checklist"][key] = default_value
    
    checklist = data["checklist"]
    
    # Calcul du pourcentage de progression
    total_items = len(checklist)
    completed_items = sum(checklist.values())
    progress_percentage = (completed_items / total_items) * 100
    
    st.progress(progress_percentage / 100)
    st.write(f"**Progression : {completed_items}/{total_items} ({progress_percentage:.1f}%)**")
    
    # Documents essentiels
    st.subheader("📄 Documents essentiels")
    col1, col2 = st.columns(2)
    with col1:
        checklist["passeport_valide"] = st.checkbox("Passeport valide (6 mois après retour)", value=checklist.get("passeport_valide", False))
        checklist["billet_avion"] = st.checkbox("Billet d'avion imprimé/PDF", value=checklist.get("billet_avion", False))
        checklist["jr_pass"] = st.checkbox("Réservation JR Pass", value=checklist.get("jr_pass", False))
        checklist["permis_conduire"] = st.checkbox("Permis de conduire international", value=checklist.get("permis_conduire", False))
    with col2:
        checklist["assurance"] = st.checkbox("Assurance voyage", value=checklist.get("assurance", False))
        checklist["carte_credit"] = st.checkbox("Carte bancaire internationale", value=checklist.get("carte_credit", False))
        checklist["especes_yen"] = st.checkbox("Prévoir des espèces en yen", value=checklist.get("especes_yen", False))
    
    # Électronique
    st.subheader("📱 Électronique")
    col1, col2 = st.columns(2)
    with col1:
        checklist["adaptateur"] = st.checkbox("Adaptateur secteur Type A/B", value=checklist.get("adaptateur", False))
        checklist["chargeur_telephone"] = st.checkbox("Chargeur téléphone", value=checklist.get("chargeur_telephone", False))
        checklist["batterie_externe"] = st.checkbox("Batterie externe", value=checklist.get("batterie_externe", False))
    with col2:
        checklist["appareil_photo"] = st.checkbox("Appareil photo", value=checklist.get("appareil_photo", False))
        checklist["carte_sd"] = st.checkbox("Carte SD de rechange", value=checklist.get("carte_sd", False))
    
    # Bagages
    st.subheader("🧳 Bagages")
    col1, col2 = st.columns(2)
    with col1:
        checklist["valise"] = st.checkbox("Valise/sac à dos", value=checklist.get("valise", False))
        checklist["vetements"] = st.checkbox("Vêtements adaptés à la saison", value=checklist.get("vetements", False))
        checklist["chaussures_confortables"] = st.checkbox("Chaussures confortables", value=checklist.get("chaussures_confortables", False))
        checklist["sous_vetements"] = st.checkbox("Sous-vêtements", value=checklist.get("sous_vetements", False))
        checklist["pyjama"] = st.checkbox("Pyjama", value=checklist.get("pyjama", False))
    with col2:
        checklist["serviette"] = st.checkbox("Serviette de toilette", value=checklist.get("serviette", False))
        checklist["produits_hygiene"] = st.checkbox("Produits d'hygiène", value=checklist.get("produits_hygiene", False))
        checklist["trousse_secours"] = st.checkbox("Trousse de premiers secours", value=checklist.get("trousse_secours", False))
        checklist["medicaments"] = st.checkbox("Médicaments personnels", value=checklist.get("medicaments", False))
        checklist["lunettes_contact"] = st.checkbox("Lunettes/contacts de rechange", value=checklist.get("lunettes_contact", False))
    
    # Préparatifs administratifs
    st.subheader("📋 Préparatifs administratifs")
    col1, col2 = st.columns(2)
    with col1:
        checklist["banque"] = st.checkbox("Prévenir sa banque", value=checklist.get("banque", False))
        checklist["copie_documents"] = st.checkbox("Copies numériques des documents", value=checklist.get("copie_documents", False))
        checklist["photos_identite"] = st.checkbox("Photos d'identité", value=checklist.get("photos_identite", False))
    with col2:
        checklist["adresse_hotel"] = st.checkbox("Adresses des hôtels notées", value=checklist.get("adresse_hotel", False))
        checklist["itineraire_imprime"] = st.checkbox("Itinéraire imprimé", value=checklist.get("itineraire_imprime", False))
    
    # Applications utiles
    st.subheader("📱 Applications utiles")
    col1, col2 = st.columns(2)
    with col1:
        checklist["app_transport"] = st.checkbox("App transport (Hyperdia, Google Maps)", value=checklist.get("app_transport", False))
        checklist["app_traduction"] = st.checkbox("App traduction (Google Translate)", value=checklist.get("app_traduction", False))
    with col2:
        checklist["app_meteo"] = st.checkbox("App météo", value=checklist.get("app_meteo", False))
        checklist["app_maps"] = st.checkbox("App cartes hors ligne", value=checklist.get("app_maps", False))
    
    # Préparatifs pratiques
    st.subheader("🎯 Préparatifs pratiques")
    col1, col2 = st.columns(2)
    with col1:
        checklist["reservation_hotels"] = st.checkbox("Réservations hôtels confirmées", value=checklist.get("reservation_hotels", False))
        checklist["reservation_restaurants"] = st.checkbox("Réservations restaurants", value=checklist.get("reservation_restaurants", False))
        checklist["activites_reservees"] = st.checkbox("Activités réservées", value=checklist.get("activites_reservees", False))
    with col2:
        checklist["transport_aeroport"] = st.checkbox("Transport aéroport organisé", value=checklist.get("transport_aeroport", False))
        checklist["guide_phrase"] = st.checkbox("Guide de phrases japonaises", value=checklist.get("guide_phrase", False))
    
    # Bouton de sauvegarde
    if st.button("💾 Sauvegarder la checklist"):
        sync_state()
        st.success("Checklist sauvegardée !")
    
    # Conseils selon la progression
    if progress_percentage < 30:
        st.warning("🚨 Il reste encore beaucoup de préparatifs à faire !")
    elif progress_percentage < 70:
        st.info("📝 Continuez vos préparatifs, vous êtes sur la bonne voie !")
    elif progress_percentage < 100:
        st.success("🎉 Presque prêt ! Quelques derniers détails à régler.")
    else:
        st.balloons()
        st.success("🎊 Parfait ! Vous êtes prêt pour votre voyage au Japon !")

def get_city_coords(city):
    # Dictionnaire complet des coordonnées des villes japonaises
    coords = {
        "Tokyo": (35.6895, 139.6917),
        "Kyoto": (35.0116, 135.7681),
        "Osaka": (34.6937, 135.5023),
        "Hiroshima": (34.3853, 132.4553),
        "Nara": (34.6851, 135.8048),
        "Sapporo": (43.0621, 141.3544),
        "Fukuoka": (33.5902, 130.4017),
        "Nagoya": (35.1815, 136.9066),
        "Kobe": (34.6901, 135.1955),
        "Yokohama": (35.4437, 139.6380),
        "Kamakura": (35.3192, 139.5467),
        "Hakone": (35.2323, 139.1067),
        "Nikko": (36.7500, 139.6167),
        "Takayama": (36.1461, 137.2522),
        "Kanazawa": (36.5613, 136.6562),
        "Matsumoto": (36.2380, 137.9720),
        "Nagano": (36.6489, 138.1950),
        "Sendai": (38.2688, 140.8721),
        "Matsuyama": (33.8416, 132.7660),
        "Kumamoto": (32.8031, 130.7079),
        "Kagoshima": (31.5602, 130.5581),
        "Okinawa": (26.2124, 127.6809),
        "Naha": (26.2124, 127.6809),
        "Shizuoka": (34.9769, 138.3831),
        "Okayama": (34.6618, 133.9344),
        "Kurashiki": (34.5854, 133.7722),
        "Himeji": (34.8164, 134.7000),
        "Miyajima": (34.2994, 132.3219),
        "Ishigaki": (24.3448, 124.1570),
        "Kushiro": (42.9750, 144.3747),
        "Asahikawa": (43.7706, 142.3650),
        "Akita": (39.7200, 140.1025),
        "Aomori": (40.8243, 140.7400),
        "Niigata": (37.9022, 139.0232),
        "Toyama": (36.6953, 137.2113),
        "Fukui": (36.0652, 136.2217),
        "Tottori": (35.5011, 134.2351),
        "Shimane": (35.4723, 133.0505),
        "Yamaguchi": (34.1783, 131.4736),
        "Tokushima": (34.0658, 134.5593),
        "Kochi": (33.5588, 133.5311),
        "Ehime": (33.8416, 132.7660),
        "Oita": (33.2381, 131.6126),
        "Miyazaki": (31.9111, 131.4239),
        "Saga": (33.2494, 130.2988),
        "Nagasaki": (32.7503, 129.8779)
    }
    # Recherche insensible à la casse
    city_lower = city.lower().strip()
    for key, value in coords.items():
        if key.lower() == city_lower:
            return value
    return (None, None)

def display_map():
    st.header("🗾 Carte Interactive de l'itinéraire")
    data = st.session_state.data
    itinerary = data.get("itinerary", [])
    if not itinerary:
        st.info("Ajoutez des étapes à l'itinéraire pour voir la carte.")
        return
    
    # Debug: afficher les villes de l'itinéraire
    # st.write("**Villes dans l'itinéraire :**", [step["city"] for step in itinerary])
    
    # Récupérer les villes uniques
    cities = {}
    cities_not_found = []
    
    for step in itinerary:
        city = step["city"]
        if city not in cities:
            lat, lon = get_city_coords(city)
            if lat and lon:
                cities[city] = {"lat": lat, "lon": lon, "steps": []}
            else:
                cities_not_found.append(city)
        if city in cities:
            cities[city]["steps"].append(step)
    
    # Afficher les villes non trouvées
    if cities_not_found:
        st.warning(f"Coordonnées non trouvées pour : {', '.join(set(cities_not_found))}")
    
    if not cities:
        st.error("Aucune coordonnée trouvée pour les villes de l'itinéraire.")
        st.info("Villes supportées : Tokyo, Kyoto, Osaka, Hiroshima, Nara, Sapporo, Fukuoka, Nagoya, Kobe, Yokohama, Kamakura, Hakone, Nikko, Takayama, Kanazawa, Matsumoto, Nagano, Sendai, Matsuyama, Kumamoto, Kagoshima, Okinawa, Naha")
        return
    
    # Centrer la carte sur la première ville
    first_city = next(iter(cities.values()))
    m = folium.Map(location=[first_city["lat"], first_city["lon"]], zoom_start=5)
    
    # Ajouter les marqueurs
    for city, info in cities.items():
        popup = f"<b>{city}</b><br>"
        for step in info["steps"]:
            popup += f"<b>{step['date']}</b> : {step['activities']}<br>"
        
        folium.Marker(
            [info["lat"], info["lon"]],
            popup=folium.Popup(popup, max_width=300),
            tooltip=city,
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
    
    st_folium(m, width=700, height=500)

def display_travel_profile():
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
        profile["contemporary_art"] = st.slider("Art contemporain (1=pas du tout, 5=priorité)", 1, 5, profile["contemporary_art"])
    
    # Nature et extérieur
    st.markdown("**Nature & Extérieur**")
    col1, col2 = st.columns(2)
    with col1:
        profile["nature_importance"] = st.slider("Importance nature (1=focus villes, 5=essentiel)", 1, 5, profile["nature_importance"])
        profile["hiking_interest"] = st.slider("Randonnée (1=non merci, 5=on est sportifs)", 1, 5, profile["hiking_interest"])
    with col2:
        profile["japanese_gardens"] = st.slider("Jardins japonais (1=pas spécialement, 5=j'adore)", 1, 5, profile["japanese_gardens"])
        profile["coastal_landscapes"] = st.slider("Paysages côtiers (1=pas priorité, 5=j'adore la mer)", 1, 5, profile["coastal_landscapes"])
    
    # Shopping et spécificités
    st.subheader("🛍️ Shopping et Spécificités")
    col1, col2 = st.columns(2)
    with col1:
        profile["shopping"] = st.text_input("Shopping", value=profile["shopping"])
        profile["photography"] = st.slider("Photographie (1=souvenirs, 5=passionné)", 1, 5, profile["photography"])
    with col2:
        profile["specific_interests"] = st.text_input("Intérêts spécifiques", value=profile["specific_interests"])
        profile["activities_to_avoid"] = st.text_input("Activités à éviter", value=profile["activities_to_avoid"])
    
    # Format et attentes
    st.subheader("📝 Format et Attentes")
    profile["detail_level"] = st.text_input("Niveau de détail", value=profile["detail_level"])
    profile["important_advice"] = st.text_input("Conseils importants", value=profile["important_advice"])
    
    # Bouton de sauvegarde
    if st.button("💾 Sauvegarder le profil"):
        data["travel_profile"] = profile
        sync_state()
        st.success("Profil sauvegardé !")
    
    # Affichage des recommandations basées sur le profil
    st.subheader("🎯 Recommandations Personnalisées")
    
    # Recommandations basées sur les scores
    recommendations = []
    
    if profile["museums_interest"] >= 4:
        recommendations.append("🏛️ **Musées prioritaires** : Musée national de Tokyo, Musée Ghibli, TeamLab Planets")
    
    if profile["modern_architecture"] >= 4:
        recommendations.append("🏢 **Architecture moderne** : Tokyo Skytree, Tokyo Tower, Shibuya Scramble")
    
    if profile["hiking_interest"] >= 4:
        recommendations.append("🏔️ **Randonnées** : Sentier Nakasendo, Mont Takao, Alpes japonaises")
    
    if profile["japanese_gardens"] >= 4:
        recommendations.append("🌸 **Jardins** : Kenroku-en (Kanazawa), Ryoan-ji (Kyoto), Shinjuku Gyoen")
    
    if profile["restaurant_adventure"] >= 4:
        recommendations.append("🍣 **Restaurants aventure** : Izakaya locaux, restaurants sans menu anglais, street food")
    
    if profile["onsen_importance"] >= 4:
        recommendations.append("♨️ **Onsen** : Hakone, Kusatsu, Beppu")
    
    if "Sumo" in profile["specific_interests"]:
        recommendations.append("🤼 **Sumo** : Réservation obligatoire pour les tournois (Tokyo, Osaka, Nagoya)")
    
    if profile["nightlife"] and "Karaoké" in profile["nightlife"]:
        recommendations.append("🎤 **Karaoké** : Big Echo, Karaoke Kan, ou karaoké privé")
    
    if profile["travel_rhythm"] >= 4:
        recommendations.append("⚡ **Rythme intense** : Planifier 2-3 activités par jour, prévoir des pauses")
    
    if profile["crowd_tolerance"] <= 2:
        recommendations.append("👥 **Éviter la foule** : Visiter tôt le matin ou en soirée, éviter les weekends")
    
    # Affichage des recommandations
    for rec in recommendations:
        st.info(rec)

def display_flight():
    st.header("✈️ Informations de Vol")
    data = st.session_state.data
    flight_info = data.get("flight_info", get_default_flight_info())
    
    # Onglets pour aller et retour
    tab1, tab2, tab3 = st.tabs(["🛫 Vol Aller", "🛬 Vol Retour", "📋 Détails Généraux"])
    
    with tab1:
        st.subheader("Vol Aller")
        col1, col2 = st.columns(2)
        
        with col1:
            flight_info["outbound"]["airline"] = st.text_input("Compagnie aérienne", value=flight_info["outbound"]["airline"], key="outbound_airline")
            flight_info["outbound"]["flight_number"] = st.text_input("Numéro de vol", value=flight_info["outbound"]["flight_number"], key="outbound_flight")
            flight_info["outbound"]["departure_airport"] = st.text_input("Aéroport de départ", value=flight_info["outbound"]["departure_airport"], key="outbound_dep")
            flight_info["outbound"]["arrival_airport"] = st.text_input("Aéroport d'arrivée", value=flight_info["outbound"]["arrival_airport"], key="outbound_arr")
            flight_info["outbound"]["departure_date"] = st.date_input("Date de départ", value=datetime.strptime(flight_info["outbound"]["departure_date"], "%Y-%m-%d").date(), key="outbound_date").strftime("%Y-%m-%d")
        
        with col2:
            flight_info["outbound"]["departure_time"] = st.time_input("Heure de départ", value=datetime.strptime(flight_info["outbound"]["departure_time"], "%H:%M").time(), key="outbound_dep_time").strftime("%H:%M")
            flight_info["outbound"]["arrival_time"] = st.time_input("Heure d'arrivée", value=datetime.strptime(flight_info["outbound"]["arrival_time"], "%H:%M").time(), key="outbound_arr_time").strftime("%H:%M")
            flight_info["outbound"]["terminal_departure"] = st.text_input("Terminal de départ", value=flight_info["outbound"]["terminal_departure"], key="outbound_term_dep")
            flight_info["outbound"]["terminal_arrival"] = st.text_input("Terminal d'arrivée", value=flight_info["outbound"]["terminal_arrival"], key="outbound_term_arr")
            flight_info["outbound"]["booking_reference"] = st.text_input("Référence de réservation", value=flight_info["outbound"]["booking_reference"], key="outbound_ref")
        
        col1, col2 = st.columns(2)
        with col1:
            flight_info["outbound"]["checked_in"] = st.checkbox("Check-in effectué", value=flight_info["outbound"]["checked_in"], key="outbound_checkin")
        with col2:
            flight_info["outbound"]["boarding_pass"] = st.checkbox("Carte d'embarquement", value=flight_info["outbound"]["boarding_pass"], key="outbound_boarding")
    
    with tab2:
        st.subheader("Vol Retour")
        col1, col2 = st.columns(2)
        
        with col1:
            flight_info["return"]["airline"] = st.text_input("Compagnie aérienne", value=flight_info["return"]["airline"], key="return_airline")
            flight_info["return"]["flight_number"] = st.text_input("Numéro de vol", value=flight_info["return"]["flight_number"], key="return_flight")
            flight_info["return"]["departure_airport"] = st.text_input("Aéroport de départ", value=flight_info["return"]["departure_airport"], key="return_dep")
            flight_info["return"]["arrival_airport"] = st.text_input("Aéroport d'arrivée", value=flight_info["return"]["arrival_airport"], key="return_arr")
            flight_info["return"]["departure_date"] = st.date_input("Date de départ", value=datetime.strptime(flight_info["return"]["departure_date"], "%Y-%m-%d").date(), key="return_date").strftime("%Y-%m-%d")
        
        with col2:
            flight_info["return"]["departure_time"] = st.time_input("Heure de départ", value=datetime.strptime(flight_info["return"]["departure_time"], "%H:%M").time(), key="return_dep_time").strftime("%H:%M")
            flight_info["return"]["arrival_time"] = st.time_input("Heure d'arrivée", value=datetime.strptime(flight_info["return"]["arrival_time"], "%H:%M").time(), key="return_arr_time").strftime("%H:%M")
            flight_info["return"]["terminal_departure"] = st.text_input("Terminal de départ", value=flight_info["return"]["terminal_departure"], key="return_term_dep")
            flight_info["return"]["terminal_arrival"] = st.text_input("Terminal d'arrivée", value=flight_info["return"]["terminal_arrival"], key="return_term_arr")
            flight_info["return"]["booking_reference"] = st.text_input("Référence de réservation", value=flight_info["return"]["booking_reference"], key="return_ref")
        
        col1, col2 = st.columns(2)
        with col1:
            flight_info["return"]["checked_in"] = st.checkbox("Check-in effectué", value=flight_info["return"]["checked_in"], key="return_checkin")
        with col2:
            flight_info["return"]["boarding_pass"] = st.checkbox("Carte d'embarquement", value=flight_info["return"]["boarding_pass"], key="return_boarding")
    
    with tab3:
        st.subheader("Détails Généraux")
        col1, col2 = st.columns(2)
        
        with col1:
            flight_info["baggage_allowance"] = st.text_input("Franchise bagages", value=flight_info["baggage_allowance"], placeholder="ex: 23kg + bagage à main")
            flight_info["meal_preference"] = st.selectbox("Préférence repas", ["", "Standard", "Végétarien", "Halal", "Kosher", "Sans gluten"], index=0 if not flight_info["meal_preference"] else ["Standard", "Végétarien", "Halal", "Kosher", "Sans gluten"].index(flight_info["meal_preference"]) + 1)
        
        with col2:
            flight_info["seat_selection"] = st.checkbox("Sélection de siège effectuée", value=flight_info["seat_selection"])
            flight_info["special_assistance"] = st.text_input("Assistance spéciale", value=flight_info["special_assistance"], placeholder="ex: Chaise roulante, assistance visuelle")
        
        flight_info["notes"] = st.text_area("Notes importantes", value=flight_info["notes"], placeholder="Informations importantes sur les vols, contacts d'urgence, etc.")
    
    # Bouton de sauvegarde
    if st.button("💾 Sauvegarder les informations de vol"):
        data["flight_info"] = flight_info
        sync_state()
        st.success("Informations de vol sauvegardées !")
    
    # Affichage du résumé
    st.subheader("📋 Résumé des Vols")
    
    if flight_info["outbound"]["airline"] or flight_info["return"]["airline"]:
        col1, col2 = st.columns(2)
        
        with col1:
            if flight_info["outbound"]["airline"]:
                st.info(f"**🛫 Aller :** {flight_info['outbound']['airline']} {flight_info['outbound']['flight_number']}")
                st.caption(f"📅 {flight_info['outbound']['departure_date']} à {flight_info['outbound']['departure_time']}")
                st.caption(f"🛬 {flight_info['outbound']['arrival_airport']} à {flight_info['outbound']['arrival_time']}")
                if flight_info["outbound"]["checked_in"]:
                    st.success("✅ Check-in effectué")
                if flight_info["outbound"]["boarding_pass"]:
                    st.success("✅ Carte d'embarquement")
        
        with col2:
            if flight_info["return"]["airline"]:
                st.info(f"**🛬 Retour :** {flight_info['return']['airline']} {flight_info['return']['flight_number']}")
                st.caption(f"📅 {flight_info['return']['departure_date']} à {flight_info['return']['departure_time']}")
                st.caption(f"🛬 {flight_info['return']['arrival_airport']} à {flight_info['return']['arrival_time']}")
                if flight_info["return"]["checked_in"]:
                    st.success("✅ Check-in effectué")
                if flight_info["return"]["boarding_pass"]:
                    st.success("✅ Carte d'embarquement")
    else:
        st.info("Aucune information de vol renseignée pour le moment.")
    
    # Conseils utiles
    st.subheader("💡 Conseils Utiles")
    st.markdown("""
    - **Check-in en ligne** : Généralement disponible 24-48h avant le vol
    - **Bagages** : Vérifiez les dimensions et poids autorisés
    - **Documents** : Passeport valide + visa si nécessaire
    - **Arrivée à l'aéroport** : 2-3h avant le vol international
    - **Transfert aéroport** : Prévoyez le transport vers Tokyo (Narita Express, Limousine Bus)
    """)

def display_calendar():
    st.header("📅 Calendrier de Voyage")
    data = st.session_state.data
    itinerary = data.get("itinerary", [])
    
    if not itinerary:
        st.info("💡 Vous n'avez pas encore d'itinéraire. Ajoutez des étapes dans l'onglet 'Itinéraire' pour voir le calendrier !")
        return
    
    # Trier l'itinéraire par date
    sorted_itinerary = sorted(itinerary, key=lambda x: x["date"])
    
    # Créer un DataFrame pour l'affichage
    df = pd.DataFrame(sorted_itinerary)
    df["date"] = pd.to_datetime(df["date"])
    df["jour_semaine"] = df["date"].dt.strftime("%A")
    df["jour_semaine_fr"] = df["date"].dt.strftime("%A").map({
        "Monday": "Lundi", "Tuesday": "Mardi", "Wednesday": "Mercredi",
        "Thursday": "Jeudi", "Friday": "Vendredi", "Saturday": "Samedi", "Sunday": "Dimanche"
    })
    df["date_formatted"] = df["date"].dt.strftime("%d/%m/%Y")
    
    # Affichage en colonnes
    st.subheader("🗓️ Vue Calendrier")
    
    # Calculer le nombre de colonnes (max 3 pour la lisibilité)
    num_columns = min(3, len(sorted_itinerary))
    
    if num_columns == 1:
        cols = [st.container()]
    elif num_columns == 2:
        col1, col2 = st.columns(2)
        cols = [col1, col2]
    else:
        col1, col2, col3 = st.columns(3)
        cols = [col1, col2, col3]
    
    # Répartir les jours dans les colonnes
    for i, (idx, row) in enumerate(df.iterrows()):
        col_idx = i % num_columns
        with cols[col_idx]:
            # Carte pour chaque jour
            with st.container():
                st.markdown(f"""
                <div class="calendar-card" style="
                    border: 2px solid #4CAF50;
                    border-radius: 10px;
                    padding: 15px;
                    margin: 10px 0;
                    background-color: #262730;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
                ">
                    <h4 class="calendar-date" style="color: #4CAF50; margin: 0; font-weight: bold;">{row['date_formatted']}</h4>
                    <p style="color: #9CA3AF; margin: 5px 0; font-size: 0.9em; font-weight: 500;">{row['jour_semaine_fr']}</p>
                    <h5 class="calendar-city" style="color: #F97316; margin: 10px 0; font-weight: bold;">🏙️ {row['city']}</h5>
                    <div class="calendar-activities" style="background-color: #1E293B; padding: 10px; border-radius: 5px; margin: 10px 0; border-left: 4px solid #3B82F6;">
                        <strong style="color: #60A5FA;">📋 Activités :</strong><br>
                        <span style="color: #E5E7EB;">{row['activities'] if row['activities'] else 'Aucune activité prévue'}</span>
                    </div>
                    <div class="calendar-lodging" style="background-color: #1E293B; padding: 10px; border-radius: 5px; border-left: 4px solid #F59E0B;">
                        <strong style="color: #FBBF24;">🏨 Hébergement :</strong><br>
                        <span style="color: #E5E7EB;">{row['lodging'] if row['lodging'] else 'Non défini'}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # Affichage en tableau pour une vue plus compacte
    st.subheader("📊 Vue Tableau")
    
    # Créer un tableau stylisé
    table_data = []
    for idx, row in df.iterrows():
        table_data.append({
            "📅 Date": row["date_formatted"],
            "📆 Jour": row["jour_semaine_fr"],
            "🏙️ Ville": row["city"],
            "📋 Activités": row["activities"][:100] + "..." if len(row["activities"]) > 100 else row["activities"],
            "🏨 Hébergement": row["lodging"][:50] + "..." if len(row["lodging"]) > 50 else row["lodging"]
        })
    
    table_df = pd.DataFrame(table_data)
    st.dataframe(table_df, use_container_width=True, hide_index=True)
    
    # Statistiques du voyage
    st.subheader("📈 Statistiques du Voyage")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📅 Durée", f"{len(sorted_itinerary)} jours")
    
    with col2:
        unique_cities = len(set(step["city"] for step in sorted_itinerary))
        st.metric("🏙️ Villes visitées", unique_cities)
    
    with col3:
        start_date = sorted_itinerary[0]["date"]
        end_date = sorted_itinerary[-1]["date"]
        st.metric("🗓️ Période", f"{start_date} → {end_date}")
    
    with col4:
        # Compter les types d'hébergement
        accommodations = [step["lodging"] for step in sorted_itinerary if step["lodging"]]
        hotel_count = sum(1 for acc in accommodations if "hôtel" in acc.lower() or "hotel" in acc.lower())
        ryokan_count = sum(1 for acc in accommodations if "ryokan" in acc.lower())
        st.metric("🏨 Types d'hébergement", f"{hotel_count} hôtels, {ryokan_count} ryokan")

def display_resources():
    st.header("🔗 Ressources Utiles")
    
    st.subheader("Convertisseur EUR → JPY")
    taux = 165  # Taux fixe, à ajuster ou automatiser
    eur = st.number_input("Montant en EUR", min_value=0.0, step=1.0, key="eur_input")
    jpy = eur * taux
    st.write(f"≈ {jpy:.0f} ¥ (taux : 1€ = {taux}¥)")
    st.subheader("Phrases utiles 🇯🇵")
    st.markdown("""
- Bonjour : こんにちは (Konnichiwa)
- Merci : ありがとう (Arigatou)
- Excusez-moi : すみません (Sumimasen)
- Oui : はい (Hai)
- Non : いいえ (Iie)
- Où sont les toilettes ? : トイREはどこですか？ (Toire wa doko desu ka?)
    """)
    st.subheader("Liens importants")
    st.markdown("""
- [Ambassade du Japon en France](https://www.fr.emb-japan.go.jp/)
- [Japan Rail Pass](https://www.japan-rail-pass.fr/)
- [Hyperdia (trains)](https://www.hyperdia.com/)
- [JR East](https://www.jreast.co.jp/e/)
    """)

def display_settings():
    st.header("⚙️ Réglages")
    
    # Onglets pour les réglages
    tab1, tab2 = st.tabs(["💾 Sauvegarde", "🔄 Reset"])
    
    with tab1:
        st.subheader("💾 Sauvegarde des données")
        st.info("⚠️ Exportez régulièrement vos données pour éviter toute perte !")
        
        if st.button("📥 Exporter les données (JSON)", type="primary"):
            data_json = export_data()
            st.download_button(
                label="💾 Télécharger data.json",
                data=data_json,
                file_name=f"data_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )
        
        # Section d'import (optionnel pour le futur)
        st.subheader("📤 Import de données")
        st.info("Fonctionnalité d'import à venir...")
    
    with tab2:
        st.subheader("🔄 Reset de l'application")
        st.warning("⚠️ Cette action supprimera définitivement toutes vos données !")
        
        # Formulaire de confirmation avec mot de passe
        with st.form("reset_confirmation"):
            reset_password = st.text_input(
                "Mot de passe de confirmation", 
                type="password",
                help="Entrez le mot de passe pour confirmer le reset"
            )
            reset_confirmed = st.checkbox(
                "Je confirme vouloir supprimer toutes mes données",
                help="Cochez cette case pour confirmer"
            )
            
            submitted = st.form_submit_button("🗑️ Reset Application", type="secondary")
            
            if submitted:
                if reset_password == st.secrets["PASSWORD"] and reset_confirmed:
                    # Supprimer le fichier de données
                    if os.path.exists(DATA_FILE):
                        os.remove(DATA_FILE)
                    # Réinitialiser la session
                    st.session_state.clear()
                    st.session_state.data = load_data()
                    st.session_state.initialized = True
                    st.success("✅ Application remise à zéro avec succès !")
                    st.rerun()
                elif reset_password != st.secrets["PASSWORD"]:
                    st.error("❌ Mot de passe incorrect")
                elif not reset_confirmed:
                    st.error("❌ Veuillez confirmer la suppression")
                else:
                    st.error("❌ Erreur lors du reset")
        
        # Informations sur le reset
        st.info("""
        **Ce que fait le reset :**
        - Supprime toutes vos données sauvegardées
        - Remet l'application à son état initial
        - Génère un nouveau profil de voyage par défaut
        - Efface l'itinéraire, le budget et la checklist
        
        **Ce qui n'est PAS affecté :**
        - Vos fichiers locaux
        - Vos exports précédents
        """)

# --- Navigation principale ---
menu = [
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
choix = st.sidebar.radio("Navigation", menu, format_func=lambda x: x)

st.sidebar.markdown("---")
st.sidebar.info("🇯🇵 Application de préparation de voyage au Japon — par votre assistant IA")

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