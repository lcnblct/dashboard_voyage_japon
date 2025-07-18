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
            "city": "Tokyo",
            "activities": "Retour à Tokyo en Shinkansen. Dernières courses, souvenirs. Soirée : Tournoi de Sumo (si disponible) ou quartier de Ginza.",
            "lodging": "Hôtel près de l'aéroport"
        },
        {
            "date": "2026-05-02",
            "city": "Tokyo",
            "activities": "Transfert vers l'aéroport. Départ pour la France.",
            "lodging": "Vol retour"
        }
    ]

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
            "travel_profile": get_default_travel_profile()
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
    with st.form("add_expense"):
        col1, col2 = st.columns(2)
        with col1:
            description = st.text_input("Description")
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
        total = df["amount"].sum()
        st.markdown(f"**Total : {total:.2f} €**")
        # Dépenses par catégorie
        cat_sum = df.groupby("category")["amount"].sum()
        st.bar_chart(cat_sum)
    else:
        st.info("Aucune dépense enregistrée.")

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

def display_resources():
    st.header("🔗 Ressources Utiles")
    
    # Section de sauvegarde
    st.subheader("💾 Sauvegarde des données")
    st.info("⚠️ Exportez régulièrement vos données pour éviter toute perte !")
    
    if st.button("📥 Exporter les données (JSON)"):
        data_json = export_data()
        st.download_button(
            label="💾 Télécharger data.json",
            data=data_json,
            file_name=f"data_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json"
        )
    
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

# --- Navigation principale ---
menu = [
    "Accueil",
    "Profil de Voyage",
    "Itinéraire",
    "Budget",
    "Checklist",
    "Carte",
    "Ressources"
]
choix = st.sidebar.radio("Navigation", menu, format_func=lambda x: x)

if choix == "Accueil":
    display_home()
elif choix == "Profil de Voyage":
    display_travel_profile()
elif choix == "Itinéraire":
    display_itinerary()
elif choix == "Budget":
    display_budget()
elif choix == "Checklist":
    display_checklist()
elif choix == "Carte":
    display_map()
elif choix == "Ressources":
    display_resources()

st.sidebar.markdown("---")
st.sidebar.info("🇯🇵 Application de préparation de voyage au Japon — par votre assistant IA") 