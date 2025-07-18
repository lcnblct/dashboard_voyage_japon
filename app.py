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
def load_data():
    if not os.path.exists(DATA_FILE):
        data = {
            "departure_date": None,
            "itinerary": [],
            "budget": [],
            "checklist": {
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
        }
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
    else:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
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
    # Date de départ
    dep_date = data.get("departure_date")
    if dep_date:
        dep_date_obj = datetime.strptime(dep_date, "%Y-%m-%d").date()
        days_left = (dep_date_obj - date.today()).days
        st.metric("Jours restants avant le départ", f"{days_left} jours" if days_left >= 0 else "Départ passé")
    else:
        st.info("Veuillez renseigner la date de départ dans l'itinéraire.")
    # Budget
    total = sum([b["amount"] for b in data.get("budget", [])])
    st.metric("Budget total dépensé", f"{total:.2f} €")
    # Prochaine tâche
    checklist = data.get("checklist", {})
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
    
    # Calcul du pourcentage de progression
    total_items = len(checklist)
    completed_items = sum(checklist.values())
    progress_percentage = (completed_items / total_items) * 100 if total_items > 0 else 0
    
    # Affichage de la progression
    st.metric("Progression checklist", f"{completed_items}/{total_items} ({progress_percentage:.1f}%)")
    
    # Prochaine tâche prioritaire
    next_task = next((label for key, label in checklist_labels if not checklist.get(key)), None)
    if next_task:
        st.warning(f"🎯 Prochaine tâche à faire : {next_task}")
    else:
        st.success("🎊 Toutes les tâches de la checklist sont complétées !")

def display_itinerary():
    st.header("🗺️ Gestion de l'itinéraire")
    data = st.session_state.data
    
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
        checklist["passeport_valide"] = st.checkbox("Passeport valide (6 mois après retour)", value=checklist["passeport_valide"])
        checklist["billet_avion"] = st.checkbox("Billet d'avion imprimé/PDF", value=checklist["billet_avion"])
        checklist["jr_pass"] = st.checkbox("Réservation JR Pass", value=checklist["jr_pass"])
        checklist["permis_conduire"] = st.checkbox("Permis de conduire international", value=checklist["permis_conduire"])
    with col2:
        checklist["assurance"] = st.checkbox("Assurance voyage", value=checklist["assurance"])
        checklist["carte_credit"] = st.checkbox("Carte bancaire internationale", value=checklist["carte_credit"])
        checklist["especes_yen"] = st.checkbox("Prévoir des espèces en yen", value=checklist["especes_yen"])
    
    # Électronique
    st.subheader("📱 Électronique")
    col1, col2 = st.columns(2)
    with col1:
        checklist["adaptateur"] = st.checkbox("Adaptateur secteur Type A/B", value=checklist["adaptateur"])
        checklist["chargeur_telephone"] = st.checkbox("Chargeur téléphone", value=checklist["chargeur_telephone"])
        checklist["batterie_externe"] = st.checkbox("Batterie externe", value=checklist["batterie_externe"])
    with col2:
        checklist["appareil_photo"] = st.checkbox("Appareil photo", value=checklist["appareil_photo"])
        checklist["carte_sd"] = st.checkbox("Carte SD de rechange", value=checklist["carte_sd"])
    
    # Bagages
    st.subheader("🧳 Bagages")
    col1, col2 = st.columns(2)
    with col1:
        checklist["valise"] = st.checkbox("Valise/sac à dos", value=checklist["valise"])
        checklist["vetements"] = st.checkbox("Vêtements adaptés à la saison", value=checklist["vetements"])
        checklist["chaussures_confortables"] = st.checkbox("Chaussures confortables", value=checklist["chaussures_confortables"])
        checklist["sous_vetements"] = st.checkbox("Sous-vêtements", value=checklist["sous_vetements"])
        checklist["pyjama"] = st.checkbox("Pyjama", value=checklist["pyjama"])
    with col2:
        checklist["serviette"] = st.checkbox("Serviette de toilette", value=checklist["serviette"])
        checklist["produits_hygiene"] = st.checkbox("Produits d'hygiène", value=checklist["produits_hygiene"])
        checklist["trousse_secours"] = st.checkbox("Trousse de premiers secours", value=checklist["trousse_secours"])
        checklist["medicaments"] = st.checkbox("Médicaments personnels", value=checklist["medicaments"])
        checklist["lunettes_contact"] = st.checkbox("Lunettes/contacts de rechange", value=checklist["lunettes_contact"])
    
    # Préparatifs administratifs
    st.subheader("📋 Préparatifs administratifs")
    col1, col2 = st.columns(2)
    with col1:
        checklist["banque"] = st.checkbox("Prévenir sa banque", value=checklist["banque"])
        checklist["copie_documents"] = st.checkbox("Copies numériques des documents", value=checklist["copie_documents"])
        checklist["photos_identite"] = st.checkbox("Photos d'identité", value=checklist["photos_identite"])
    with col2:
        checklist["adresse_hotel"] = st.checkbox("Adresses des hôtels notées", value=checklist["adresse_hotel"])
        checklist["itineraire_imprime"] = st.checkbox("Itinéraire imprimé", value=checklist["itineraire_imprime"])
    
    # Applications utiles
    st.subheader("📱 Applications utiles")
    col1, col2 = st.columns(2)
    with col1:
        checklist["app_transport"] = st.checkbox("App transport (Hyperdia, Google Maps)", value=checklist["app_transport"])
        checklist["app_traduction"] = st.checkbox("App traduction (Google Translate)", value=checklist["app_traduction"])
    with col2:
        checklist["app_meteo"] = st.checkbox("App météo", value=checklist["app_meteo"])
        checklist["app_maps"] = st.checkbox("App cartes hors ligne", value=checklist["app_maps"])
    
    # Préparatifs pratiques
    st.subheader("🎯 Préparatifs pratiques")
    col1, col2 = st.columns(2)
    with col1:
        checklist["reservation_hotels"] = st.checkbox("Réservations hôtels confirmées", value=checklist["reservation_hotels"])
        checklist["reservation_restaurants"] = st.checkbox("Réservations restaurants", value=checklist["reservation_restaurants"])
        checklist["activites_reservees"] = st.checkbox("Activités réservées", value=checklist["activites_reservees"])
    with col2:
        checklist["transport_aeroport"] = st.checkbox("Transport aéroport organisé", value=checklist["transport_aeroport"])
        checklist["guide_phrase"] = st.checkbox("Guide de phrases japonaises", value=checklist["guide_phrase"])
    
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
- Où sont les toilettes ? : トイレはどこですか？ (Toire wa doko desu ka?)
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
    "Itinéraire",
    "Budget",
    "Checklist",
    "Carte",
    "Ressources"
]
choix = st.sidebar.radio("Navigation", menu, format_func=lambda x: x)

if choix == "Accueil":
    display_home()
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