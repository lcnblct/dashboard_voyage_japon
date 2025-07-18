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
                "passeport_valide": False,
                "billet_avion": False,
                "jr_pass": False,
                "permis_conduire": False,
                "adaptateur": False,
                "vetements": False,
                "trousse_secours": False,
                "banque": False,
                "assurance": False
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
        ("passeport_valide", "Passeport valide"),
        ("billet_avion", "Billet d'avion imprimé/PDF"),
        ("jr_pass", "Réservation JR Pass"),
        ("permis_conduire", "Permis de conduire international"),
        ("adaptateur", "Adaptateur secteur Type A/B"),
        ("vetements", "Vêtements adaptés à la saison"),
        ("trousse_secours", "Trousse de premiers secours"),
        ("banque", "Prévenir sa banque"),
        ("assurance", "Souscrire à une assurance voyage")
    ]
    next_task = next((label for key, label in checklist_labels if not checklist.get(key)), None)
    if next_task:
        st.warning(f"Prochaine tâche à faire : {next_task}")
    else:
        st.success("Toutes les tâches de la checklist sont complétées !")

def display_itinerary():
    st.header("🗺️ Gestion de l'itinéraire")
    data = st.session_state.data
    with st.form("add_step"):
        col1, col2 = st.columns(2)
        with col1:
            date_step = st.date_input("Date", value=date(2026, 4, 18))
        with col2:
            city = st.text_input("Ville / Lieu")
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
            st.experimental_rerun()
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
                    st.experimental_rerun()
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
            st.experimental_rerun()
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
    st.subheader("Documents")
    checklist["passeport_valide"] = st.checkbox("Passeport valide", value=checklist["passeport_valide"])
    checklist["billet_avion"] = st.checkbox("Billet d'avion imprimé/PDF", value=checklist["billet_avion"])
    checklist["jr_pass"] = st.checkbox("Réservation JR Pass", value=checklist["jr_pass"])
    checklist["permis_conduire"] = st.checkbox("Permis de conduire international", value=checklist["permis_conduire"])
    st.subheader("Bagages")
    checklist["adaptateur"] = st.checkbox("Adaptateur secteur Type A/B", value=checklist["adaptateur"])
    checklist["vetements"] = st.checkbox("Vêtements adaptés à la saison", value=checklist["vetements"])
    checklist["trousse_secours"] = st.checkbox("Trousse de premiers secours", value=checklist["trousse_secours"])
    st.subheader("Administratif")
    checklist["banque"] = st.checkbox("Prévenir sa banque", value=checklist["banque"])
    checklist["assurance"] = st.checkbox("Souscrire à une assurance voyage", value=checklist["assurance"])
    if st.button("Sauvegarder la checklist"):
        sync_state()
        st.success("Checklist sauvegardée !")

def get_city_coords(city):
    # Dictionnaire minimal, à étendre selon les besoins
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
        "Yokohama": (35.4437, 139.6380)
    }
    return coords.get(city, (None, None))

def display_map():
    st.header("🗾 Carte Interactive de l'itinéraire")
    data = st.session_state.data
    itinerary = data.get("itinerary", [])
    if not itinerary:
        st.info("Ajoutez des étapes à l'itinéraire pour voir la carte.")
        return
    # Récupérer les villes uniques
    cities = {}
    for step in itinerary:
        city = step["city"]
        if city not in cities:
            lat, lon = get_city_coords(city)
            if lat and lon:
                cities[city] = {"lat": lat, "lon": lon, "steps": []}
        if city in cities:
            cities[city]["steps"].append(step)
    if not cities:
        st.warning("Aucune coordonnée trouvée pour les villes de l'itinéraire.")
        return
    # Centrer la carte sur la première ville
    first_city = next(iter(cities.values()))
    m = folium.Map(location=[first_city["lat"], first_city["lon"]], zoom_start=5)
    for city, info in cities.items():
        popup = ""
        for step in info["steps"]:
            popup += f"<b>{step['date']}</b> : {step['activities']}<br>"
        folium.Marker(
            [info["lat"], info["lon"]],
            popup=folium.Popup(popup, max_width=300),
            tooltip=city
        ).add_to(m)
    st_folium(m, width=700, height=500)

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