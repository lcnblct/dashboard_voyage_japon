# Page du générateur de prompt ultime
import streamlit as st
from datetime import datetime
from data.models import get_default_travel_profile
from data.storage import sync_state

def display_prompt_generator():
    """Affiche la page du générateur de prompt ultime"""
    
    # Initialisation de l'état
    if 'prompt_state' not in st.session_state:
        st.session_state.prompt_state = 'intro'
    
    data = st.session_state.data
    profile = data.get("travel_profile", get_default_travel_profile())
    
    # CSS personnalisé
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    .prompt-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .prompt-text {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 0.5rem;
        padding: 1rem;
        font-family: 'Courier New', monospace;
        white-space: pre-wrap;
        max-height: 400px;
        overflow-y: auto;
    }
    .stButton > button {
        border-radius: 0.5rem;
        font-weight: 600;
        padding: 0.5rem 1.5rem;
    }
    .info-box {
        background-color: #eff6ff;
        border: 1px solid #dbeafe;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .warning-box {
        background-color: #fef3c7;
        border: 1px solid #f59e0b;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # En-tête principal
    st.markdown("""
    <div class="main-header">
        <h1>🎯 Générateur de Prompt Ultime</h1>
        <p style="font-size: 1.2rem; color: #6b7280;">Créez le prompt parfait pour votre guide de voyage personnalisé</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation entre les étapes
    if st.session_state.prompt_state == 'intro':
        display_prompt_intro()
    elif st.session_state.prompt_state == 'customize':
        display_prompt_customize(profile)
    elif st.session_state.prompt_state == 'result':
        display_prompt_result()

def display_prompt_intro():
    """Affiche l'introduction du générateur de prompt"""
    
    st.markdown("""
    <div class="prompt-card">
        <h3>🚀 Bienvenue dans le Générateur de Prompt Ultime</h3>
        <p>Ce générateur va créer un prompt détaillé et structuré basé sur votre profil de voyage. 
        Ce prompt pourra ensuite être utilisé avec ChatGPT, Claude ou tout autre IA pour générer un guide de voyage personnalisé.</p>
        
        <div class="info-box">
            <h4>📋 Ce que fait ce générateur :</h4>
            <ul>
                <li>Analyse votre profil de voyage complet</li>
                <li>Structure toutes vos préférences et contraintes</li>
                <li>Crée un prompt détaillé pour l'IA</li>
                <li>Permet la personnalisation du niveau de détail</li>
                <li>Génère un fichier téléchargeable</li>
            </ul>
        </div>
        
        <div class="warning-box">
            <h4>⚠️ Important :</h4>
            <p>Assurez-vous d'avoir complété votre profil de voyage avant de générer le prompt. 
            Plus votre profil est détaillé, plus le guide généré sera personnalisé.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col2:
        if st.button("🎯 Commencer la génération", type="primary"):
            st.session_state.prompt_state = 'customize'
            st.rerun()

def display_prompt_customize(profile):
    """Affiche l'étape de personnalisation du prompt"""
    
    st.markdown("""
    <div class="prompt-card">
        <h3>⚙️ Personnalisation du Prompt</h3>
        <p>Vérifiez et ajustez les informations de votre profil qui seront utilisées dans le prompt :</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Informations de base
    st.subheader("👥 Informations de base")
    col1, col2 = st.columns(2)
    
    with col1:
        travelers = st.text_input("Voyageurs", value=profile.get('travelers', ''))
        arrival_date = st.date_input("Date d'arrivée", value=profile.get('arrival_date'))
        departure_date = st.date_input("Date de départ", value=profile.get('departure_date'))
        budget = st.text_input("Budget", value=profile.get('budget', ''))
    
    with col2:
        experience = st.selectbox("Expérience", 
            ["Premier voyage", "Déjà visité", "Expert"], 
            index=["Premier voyage", "Déjà visité", "Expert"].index(profile.get('experience', 'Premier voyage')))
        arrival_airport = st.text_input("Aéroport d'arrivée", value=profile.get('arrival_airport', ''))
        departure_airport = st.text_input("Aéroport de départ", value=profile.get('departure_airport', ''))
    
    # Préférences géographiques
    st.subheader("🗺️ Préférences géographiques")
    col1, col2 = st.columns(2)
    
    with col1:
        geographic_orientation = st.text_area("Orientation géographique", 
            value=profile.get('geographic_orientation', ''), height=100)
        priority_1 = st.text_input("Priorité N°1", value=profile.get('priority_1', ''))
        travel_rhythm = st.slider("Rythme du voyage", 1, 5, profile.get('travel_rhythm', 3))
    
    with col2:
        crowd_tolerance = st.slider("Tolérance à la foule", 1, 5, profile.get('crowd_tolerance', 3))
        accommodation_style = st.text_input("Style d'hébergement", value=profile.get('accommodation_style', ''))
        cuisine_preferences = st.text_input("Préférences culinaires", value=profile.get('cuisine_preferences', ''))
    
    # Centres d'intérêt
    st.subheader("🎯 Centres d'intérêt")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        temples_interest = st.slider("Temples et sanctuaires", 1, 5, profile.get('temples_interest', 3))
        manga_anime = st.slider("Manga/Anime", 1, 5, profile.get('manga_anime', 3))
        gaming = st.slider("Jeux vidéo", 1, 5, profile.get('gaming', 3))
    
    with col2:
        nature_importance = st.slider("Nature", 1, 5, profile.get('nature_importance', 3))
        museums_interest = st.slider("Musées", 1, 5, profile.get('museums_interest', 3))
        photography = st.slider("Photographie", 1, 5, profile.get('photography', 3))
    
    with col3:
        onsen_interest = st.slider("Onsen", 1, 5, profile.get('onsen_interest', 3))
        shopping_interest = st.slider("Shopping", 1, 5, profile.get('shopping_interest', 3))
        nightlife_interest = st.slider("Vie nocturne", 1, 5, profile.get('nightlife_interest', 3))
    
    # Autres informations
    st.subheader("📝 Autres informations")
    current_reservations = st.text_area("Réservations actuelles", 
        value=profile.get('current_reservations', ''), height=80)
    constraints = st.text_area("Contraintes", 
        value=profile.get('constraints', ''), height=80)
    specific_interests = st.text_area("Intérêts spécifiques", 
        value=profile.get('specific_interests', ''), height=80)
    
    # Options de personnalisation du prompt
    st.subheader("🎨 Options du prompt")
    col1, col2 = st.columns(2)
    
    with col1:
        detail_level = st.selectbox("Niveau de détail", 
            ["Basique", "Standard", "Détaillé", "Très détaillé"], 
            index=2)
        prompt_tone = st.selectbox("Ton du prompt", 
            ["Professionnel", "Amical", "Enthousiaste", "Formel"], 
            index=1)
    
    with col2:
        include_alternatives = st.checkbox("Inclure des alternatives", value=True)
        include_budget_tips = st.checkbox("Inclure des conseils budget", value=True)
        important_advice = st.text_area("Conseils importants à ajouter", 
            value="", height=80, 
            placeholder="Ex: Privilégier les transports en commun, éviter les périodes de fêtes...")
    
    # Boutons d'action
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔙 Retour"):
            st.session_state.prompt_state = 'intro'
            st.rerun()
    
    with col2:
        if st.button("🎲 Générer avec données aléatoires"):
            generate_random_prompt()
            st.session_state.prompt_state = 'result'
            st.rerun()
    
    with col3:
        if st.button("🚀 Générer le prompt", type="primary"):
            # Mise à jour du profil avec les nouvelles valeurs
            updated_profile = {
                'travelers': travelers,
                'arrival_date': arrival_date,
                'departure_date': departure_date,
                'budget': budget,
                'experience': experience,
                'arrival_airport': arrival_airport,
                'departure_airport': departure_airport,
                'geographic_orientation': geographic_orientation,
                'priority_1': priority_1,
                'travel_rhythm': travel_rhythm,
                'crowd_tolerance': crowd_tolerance,
                'accommodation_style': accommodation_style,
                'cuisine_preferences': cuisine_preferences,
                'temples_interest': temples_interest,
                'manga_anime': manga_anime,
                'gaming': gaming,
                'nature_importance': nature_importance,
                'museums_interest': museums_interest,
                'photography': photography,
                'onsen_interest': onsen_interest,
                'shopping_interest': shopping_interest,
                'nightlife_interest': nightlife_interest,
                'current_reservations': current_reservations,
                'constraints': constraints,
                'specific_interests': specific_interests
            }
            
            # Sauvegarde du profil mis à jour
            data = st.session_state.data
            data["travel_profile"] = updated_profile
            sync_state()
            
            # Génération du prompt
            st.session_state.generated_prompt = generate_custom_prompt(
                updated_profile, detail_level, prompt_tone, 
                include_alternatives, include_budget_tips, important_advice
            )
            st.session_state.prompt_state = 'result'
            st.rerun()

def display_prompt_result():
    """Affiche le résultat du prompt généré"""
    
    if 'generated_prompt' not in st.session_state:
        st.error("Aucun prompt généré. Veuillez retourner à l'étape précédente.")
        if st.button("🔙 Retour"):
            st.session_state.prompt_state = 'customize'
            st.rerun()
        return
    
    st.markdown("""
    <div class="prompt-card">
        <h3>✅ Prompt Ultime Généré</h3>
        <p>Voici votre prompt personnalisé. Vous pouvez le copier et l'utiliser avec ChatGPT, Claude ou tout autre IA pour générer votre guide de voyage.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Affichage du prompt
    st.subheader("📝 Votre Prompt")
    st.markdown(f"""
    <div class="prompt-text">
{st.session_state.generated_prompt}
    </div>
    """, unsafe_allow_html=True)
    
    # Boutons d'action
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🔙 Modifier"):
            st.session_state.prompt_state = 'customize'
            st.rerun()
    
    with col2:
        if st.button("📋 Copier dans le presse-papiers"):
            st.write("✅ Prompt copié !")
            st.code(st.session_state.generated_prompt)
    
    with col3:
        download_prompt()

def generate_custom_prompt(profile, detail_level, prompt_tone, include_alternatives, include_budget_tips, important_advice):
    """Génère un prompt personnalisé basé sur le profil"""
    
    # Récupération du profil complet depuis session_state
    data = st.session_state.data
    full_profile = data.get("travel_profile", profile)
    
    # Descriptions basées sur les scores
    rhythm_desc = get_rhythm_description(profile.get('travel_rhythm', 3))
    crowd_desc = get_crowd_description(profile.get('crowd_tolerance', 3))
    
    # Construction du prompt
    prompt = f"""# RÔLE ET OBJECTIF
Tu es un expert du voyage au Japon, spécialisé dans la création de guides de voyage personnalisés. Ta mission est de créer un guide de voyage COMPLET et DÉTAILLÉ en te basant EXCLUSIVEMENT sur le profil voyageur fourni ci-dessous. 

IMPORTANT : Ce prompt contient toutes les informations nécessaires pour créer un guide sur-mesure. Tu dois respecter scrupuleusement les préférences, contraintes et centres d'intérêt spécifiés.

---

# PROFIL VOYAGEUR COMPLET

## INFORMATIONS DE BASE
- **Voyageurs :** {profile.get('travelers', 'Non spécifié')}
- **Dates :** {profile.get('arrival_date', 'Non spécifié')} → {profile.get('departure_date', 'Non spécifié')}
- **Budget :** {profile.get('budget', 'Non spécifié')}
- **Expérience :** {profile.get('experience', 'Non spécifié')}
- **Aéroports :** {profile.get('arrival_airport', 'Non spécifié')} → {profile.get('departure_airport', 'Non spécifié')}

## PRÉFÉRENCES GÉOGRAPHIQUES
- **Orientation :** {profile.get('geographic_orientation', 'Non spécifié')}
- **Priorité N°1 :** {profile.get('priority_1', 'Non spécifié')}

## RYTHME ET STYLE
- **Rythme du voyage :** {profile.get('travel_rhythm', 'Non spécifié')}/5 ({rhythm_desc})
- **Tolérance à la foule :** {profile.get('crowd_tolerance', 'Non spécifié')}/5 ({crowd_desc})
- **Style d'hébergement :** {profile.get('accommodation_style', 'Non spécifié')}
- **Préférences culinaires :** {profile.get('cuisine_preferences', 'Non spécifié')}

## CENTRES D'INTÉRÊT (Scores 1-5)
- **Temples et sanctuaires :** {profile.get('temples_interest', 'Non spécifié')}/5
- **Manga/Anime :** {profile.get('manga_anime', 'Non spécifié')}/5
- **Jeux vidéo :** {profile.get('gaming', 'Non spécifié')}/5
- **Nature :** {profile.get('nature_importance', 'Non spécifié')}/5
- **Musées :** {profile.get('museums_interest', 'Non spécifié')}/5
- **Photographie :** {profile.get('photography', 'Non spécifié')}/5
- **Onsen :** {profile.get('onsen_interest', 'Non spécifié')}/5
- **Shopping :** {profile.get('shopping_interest', 'Non spécifié')}/5
- **Vie nocturne :** {profile.get('nightlife_interest', 'Non spécifié')}/5

## AUTRES INFORMATIONS
- **Réservations actuelles :** {profile.get('current_reservations', 'Aucune')}
- **Contraintes :** {profile.get('constraints', 'Aucune')}
- **Intérêts spécifiques :** {profile.get('specific_interests', 'Aucun')}

## RÉPONSES AU QUESTIONNAIRE DÉTAILLÉ
{get_questionnaire_answers(full_profile)}

---

# MISSION : CRÉER UN GUIDE DE VOYAGE COMPLET

En te basant EXCLUSIVEMENT sur ce profil, crée un guide de voyage détaillé et pratique. Voici la structure attendue :

## 1. TITRE ET SYNTHÈSE
- Donne un titre accrocheur qui reflète l'esprit du voyage
- Rédige une synthèse de 2-3 paragraphes qui justifie les choix d'itinéraire

## 2. ITINÉRAIRE GLOBAL
- Présente les grandes étapes avec le nombre de nuits
- Justifie chaque choix par rapport au profil

## 3. PLANNING JOUR PAR JOUR
Pour CHAQUE jour, fournis :
- **Thème de la journée**
- **Matin** : Activités détaillées avec horaires
- **Midi** : Suggestions de restaurants adaptées aux goûts
- **Après-midi** : Activités et visites
- **Soir** : Dîner et activités nocturnes
- **Conseils pratiques** : Horaires, réservations, alternatives

## 4. CONSEILS PRATIQUES PERSONNALISÉS
- Transport : Pass recommandés, cartes, applications
- Budget : Estimations détaillées par activité
- Savoir-vivre : Coutumes locales importantes
- Réservations : Liens et conseils
- Alternatives : Plans B en cas de problème
- Lexique : Mots utiles en japonais

## 5. RECOMMANDATIONS SPÉCIALES
- Activités "coup de cœur" selon le profil
- Lieux moins connus qui correspondent aux goûts
- Conseils pour optimiser l'expérience

**TON :** {prompt_tone.lower()}, enthousiaste, pratique et encourageant.

**DÉTAIL :** {detail_level}

**CONSEILS IMPORTANTS :** {important_advice if important_advice else "Aucun conseil spécifique ajouté."}

Maintenant, crée ce guide de voyage personnalisé en respectant scrupuleusement ce profil.
"""
    
    return prompt

def generate_random_prompt():
    """Génère un prompt avec des données aléatoires pour démonstration"""
    
    import random
    
    # Données aléatoires cohérentes
    random_data = {
        'travelers': 'Couple de 30 ans',
        'arrival_date': '2024-05-15',
        'departure_date': '2024-05-25',
        'budget': '4000€ pour 2 personnes',
        'experience': 'Premier voyage',
        'arrival_airport': 'Narita',
        'departure_airport': 'Haneda',
        'geographic_orientation': 'Route d\'Or classique (Tokyo-Kyoto-Osaka)',
        'priority_1': 'La gastronomie sous toutes ses formes',
        'travel_rhythm': 4,
        'crowd_tolerance': 3,
        'accommodation_style': 'Mélange ryokan et hôtels modernes',
        'cuisine_preferences': 'Aventure culinaire totale, street food et restaurants traditionnels',
        'temples_interest': 4,
        'manga_anime': 3,
        'gaming': 2,
        'nature_importance': 3,
        'museums_interest': 4,
        'photography': 5,
        'onsen_interest': 4,
        'shopping_interest': 3,
        'nightlife_interest': 4,
        'current_reservations': 'Aucune',
        'constraints': 'Pas de voiture, privilégier les transports en commun',
        'specific_interests': 'Photographie urbaine, onsen, street food'
    }
    
    st.session_state.generated_prompt = generate_custom_prompt(
        random_data, "Détaillé", "Enthousiaste", True, True, 
        "Privilégier les transports en commun, réserver les restaurants populaires à l'avance"
    )

def get_rhythm_description(score):
    """Retourne une description du rythme basée sur le score"""
    descriptions = {
        1: "Très lent, beaucoup de temps libre",
        2: "Lent, quelques activités par jour",
        3: "Modéré, équilibré",
        4: "Rapide, bien rempli",
        5: "Très rapide, intensif"
    }
    return descriptions.get(score, "Modéré")

def get_crowd_description(score):
    """Retourne une description de la tolérance à la foule basée sur le score"""
    descriptions = {
        1: "Éviter les foules",
        2: "Préférer les lieux calmes",
        3: "Équilibré",
        4: "Pas de problème avec les foules",
        5: "Rechercher l'ambiance"
    }
    return descriptions.get(score, "Équilibré")

def get_questionnaire_answers(profile):
    """Récupère les réponses du questionnaire détaillé"""
    # Cette fonction pourrait être étendue pour inclure toutes les réponses du questionnaire
    # Pour l'instant, on retourne les informations principales
    return f"""
Réponses principales du questionnaire :
- Orientation géographique : {profile.get('geographic_orientation', 'Non spécifié')}
- Priorité principale : {profile.get('priority_1', 'Non spécifié')}
- Rythme de voyage : {profile.get('travel_rhythm', 'Non spécifié')}/5
- Style d'hébergement : {profile.get('accommodation_style', 'Non spécifié')}
- Préférences culinaires : {profile.get('cuisine_preferences', 'Non spécifié')}
"""

def download_prompt():
    """Permet de télécharger le prompt généré"""
    
    if 'generated_prompt' not in st.session_state:
        st.warning("Aucun prompt à télécharger.")
        return
    
    # Nom du fichier avec timestamp
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"prompt-voyage-japon-{timestamp}.txt"
    
    # Téléchargement
    st.download_button(
        label="📥 Télécharger le prompt",
        data=st.session_state.generated_prompt,
        file_name=filename,
        mime="text/plain"
    ) 