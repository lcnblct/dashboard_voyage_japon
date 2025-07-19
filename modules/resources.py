# Page des ressources utiles - Version ultra développée
import streamlit as st
import json
import requests
from datetime import datetime
import pandas as pd

def get_exchange_rate():
    """Récupère le taux de change EUR/JPY en temps réel"""
    try:
        # API gratuite pour les taux de change
        response = requests.get("https://api.exchangerate-api.com/v4/latest/EUR", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data['rates']['JPY']
    except:
        pass
    return 165  # Taux de fallback

def display_resources():
    """Affiche la page des ressources utiles ultra développée"""
    
    # Titre principal avec emoji
    st.title("🔗 Centre de Ressources Japon")
    st.markdown("---")
    
    # Informations contextuelles basées sur le profil utilisateur
    if 'data' in st.session_state and 'travel_profile' in st.session_state.data:
        profile = st.session_state.data['travel_profile']
        
        # Affichage du contexte utilisateur
        with st.expander("📋 Contexte de votre voyage", expanded=False):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Voyageurs", profile.get('travelers', 'Non défini'))
                st.metric("Budget/jour", f"{profile.get('budget_per_day', 0)}€")
            with col2:
                st.metric("Arrivée", profile.get('arrival_date', 'Non défini'))
                st.metric("Expérience", profile.get('experience', 'Non défini'))
            with col3:
                st.metric("Rythme", f"{profile.get('travel_rhythm', 0)}/5")
                st.metric("Planification", f"{profile.get('planning_preference', 0)}/5")
    
    # === SECTION 1: OUTILS PRATIQUES ===
    st.header("🛠️ Outils Pratiques")
    
    # Convertisseur de devises avancé
    with st.container():
        st.subheader("💱 Convertisseur de Devises")
        col1, col2, col3 = st.columns([2, 1, 2])
        
        with col1:
            amount = st.number_input("Montant", min_value=0.0, step=1.0, key="currency_amount")
            currency_from = st.selectbox("De", ["EUR", "USD", "GBP", "CAD", "AUD"], key="currency_from")
        
        with col2:
            st.markdown("### →")
            if st.button("🔄 Actualiser", key="refresh_rate"):
                st.rerun()
        
        with col3:
            # Récupération du taux en temps réel
            if currency_from == "EUR":
                rate = get_exchange_rate()
                jpy_amount = amount * rate
                st.metric("En JPY", f"¥{jpy_amount:,.0f}")
                st.caption(f"Taux: 1€ = ¥{rate:.2f}")
            else:
                st.info("Taux EUR/JPY uniquement disponible")
    
    # Calculateur de budget
    with st.container():
        st.subheader("💰 Calculateur de Budget")
        if 'data' in st.session_state and 'budget_planning' in st.session_state.data:
            budget_data = st.session_state.data['budget_planning']
            
            # Calcul du budget total
            total_budget = 0
            budget_details = {}
            
            for category, items in budget_data.items():
                category_total = 0
                for item_name, item_data in items.items():
                    if isinstance(item_data, dict) and 'budget' in item_data:
                        category_total += item_data['budget']
                budget_details[category] = category_total
                total_budget += category_total
            
            # Affichage du budget
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Budget Total", f"{total_budget}€")
                st.metric("Budget/jour", f"{total_budget/14:.0f}€")
            with col2:
                st.metric("Budget restant", f"{total_budget - sum(budget_details.values()):.0f}€")
                
            # Graphique du budget par catégorie
            if budget_details:
                budget_df = pd.DataFrame(list(budget_details.items()), columns=['Catégorie', 'Budget'])
                st.bar_chart(budget_df.set_index('Catégorie'))
    
    # === SECTION 2: TRANSPORT ===
    st.header("🚄 Transport")
    
    # Applications de transport
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📱 Applications Essentielles")
        st.markdown("""
        **🚇 Hyperdia**
        - Horaires trains Japon
        - [hyperdia.com](https://www.hyperdia.com/)
        
        **🗺️ Google Maps**
        - Navigation complète
        - Transport en commun
        
        **🚌 Japan Transit Planner**
        - Itinéraires détaillés
        - Prix des trajets
        
        **🚕 Japan Taxi**
        - Réservation taxis
        - Traduction automatique
        """)
    
    with col2:
        st.subheader("🎫 Pass et Cartes")
        st.markdown("""
        **🚄 Japan Rail Pass**
        - [japan-rail-pass.fr](https://www.japan-rail-pass.fr/)
        - Réservation obligatoire
        
        **💳 Pasmo/Suica**
        - Rechargeable
        - Métro, bus, magasins
        
        **🎫 Tokyo Subway Ticket**
        - 24h/48h/72h
        - Illimité métro Tokyo
        """)
    
    with col3:
        st.subheader("✈️ Aéroports")
        st.markdown("""
        **🛬 Narita (NRT)**
        - Tokyo principal
        - Train JR Narita Express
        
        **🛬 Haneda (HND)**
        - Tokyo centre
        - Monorail Tokyo
        
        **🛬 Kansai (KIX)**
        - Osaka/Kyoto
        - Haruka Express
        """)
    
    # === SECTION 3: COMMUNICATION ===
    st.header("💬 Communication")
    
    # Applications de traduction
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌐 Traduction")
        st.markdown("""
        **📱 Google Translate**
        - Traduction photo
        - Conversation temps réel
        - Hors ligne disponible
        
        **📱 DeepL**
        - Traduction précise
        - Interface élégante
        
        **📱 Microsoft Translator**
        - Conversation multi-langues
        - Traduction vocale
        """)
    
    with col2:
        st.subheader("📞 Communication")
        st.markdown("""
        **📱 LINE**
        - Messagerie populaire
        - Appels vidéo gratuits
        
        **📱 WhatsApp**
        - International
        - Appels WiFi
        
        **📱 Discord**
        - Communauté voyageurs
        - Partage d'expériences
        """)
    
    # Phrases essentielles japonaises
    st.subheader("🗣️ Phrases Essentielles")
    
    phrases_data = {
        "Salutations": {
            "Bonjour": "こんにちは (Konnichiwa)",
            "Bonsoir": "こんばんは (Konbanwa)",
            "Au revoir": "さようなら (Sayounara)",
            "Merci": "ありがとう (Arigatou)",
            "S'il vous plaît": "お願いします (Onegaishimasu)"
        },
        "Transport": {
            "Où est la station ?": "駅はどこですか？ (Eki wa doko desu ka?)",
            "Combien coûte le billet ?": "切符はいくらですか？ (Kippu wa ikura desu ka?)",
            "Je vais à...": "...に行きます (... ni ikimasu)",
            "Où sont les toilettes ?": "トイレはどこですか？ (Toire wa doko desu ka?)"
        },
        "Restaurant": {
            "Menu s'il vous plaît": "メニューをお願いします (Menyuu wo onegaishimasu)",
            "C'est délicieux": "おいしいです (Oishii desu)",
            "L'addition s'il vous plaît": "お会計をお願いします (Okaikei wo onegaishimasu)",
            "Je ne mange pas...": "...は食べません (... wa tabemasen)"
        },
        "Urgences": {
            "Aidez-moi": "助けてください (Tasukete kudasai)",
            "Je suis malade": "病気です (Byouki desu)",
            "Police": "警察 (Keisatsu)",
            "Hôpital": "病院 (Byouin)"
        }
    }
    
    # Affichage des phrases par catégorie
    for category, phrases in phrases_data.items():
        with st.expander(f"📝 {category}", expanded=False):
            for french, japanese in phrases.items():
                st.markdown(f"**{french}** : {japanese}")
    
    # === SECTION 4: HÉBERGEMENT ===
    st.header("🏨 Hébergement")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🏨 Hôtels")
        st.markdown("""
        **📱 Booking.com**
        - Réservations internationales
        - Avis vérifiés
        
        **📱 Hotels.com**
        - Programme fidélité
        - Prix garantis
        
        **📱 Agoda**
        - Spécialisé Asie
        - Prix compétitifs
        """)
    
    with col2:
        st.subheader("🏮 Ryokan & Onsen")
        st.markdown("""
        **♨️ Japanican**
        - Ryokan traditionnels
        - [japanican.com](https://www.japanican.com/)
        
        **♨️ Rakuten Travel**
        - Onsen authentiques
        - Réservations locales
        
        **♨️ Jalan**
        - Site japonais
        - Prix locaux
        """)
    
    with col3:
        st.subheader("🏠 Auberges")
        st.markdown("""
        **🏠 Hostelworld**
        - Auberges de jeunesse
        - Communauté voyageurs
        
        **🏠 Airbnb**
        - Appartements locaux
        - Expérience authentique
        
        **🏠 Couchsurfing**
        - Hébergement gratuit
        - Rencontres locales
        """)
    
    # === SECTION 5: NOURRITURE ===
    st.header("🍜 Nourriture")
    
    # Applications de restauration
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🍽️ Applications Restaurants")
        st.markdown("""
        **🍜 Tabelog**
        - Guide restaurants japonais
        - Avis locaux authentiques
        
        **🍜 Gurunavi**
        - Restaurants par région
        - Réservations en ligne
        
        **🍜 HotPepper**
        - Offres et promotions
        - Restaurants populaires
        
        **🍜 OpenTable**
        - Réservations internationales
        - Interface en anglais
        """)
    
    with col2:
        st.subheader("🥡 Livraison")
        st.markdown("""
        **🚚 Uber Eats**
        - Livraison internationale
        - Interface familière
        
        **🚚 Demaekan**
        - Livraison japonaise
        - Restaurants locaux
        
        **🚚 FoodPanda**
        - Alternative Uber Eats
        - Couverture étendue
        """)
    
    # Guide culinaire
    st.subheader("📖 Guide Culinaire")
    
    cuisine_categories = {
        "🍣 Sushi & Sashimi": ["Nigiri", "Maki", "Sashimi", "Chirashi", "Temaki"],
        "🍜 Ramen & Udon": ["Tonkotsu", "Shoyu", "Miso", "Shio", "Tsukemen"],
        "🍱 Bento & Donburi": ["Katsudon", "Gyudon", "Oyakodon", "Unadon", "Tempura"],
        "🍢 Street Food": ["Takoyaki", "Okonomiyaki", "Yakitori", "Taiyaki", "Dango"],
        "🍰 Pâtisseries": ["Mochi", "Dorayaki", "Castella", "Anmitsu", "Kakigori"]
    }
    
    for category, items in cuisine_categories.items():
        with st.expander(category, expanded=False):
            for item in items:
                st.markdown(f"• {item}")
    
    # === SECTION 6: ACTIVITÉS & CULTURE ===
    st.header("🎭 Activités & Culture")
    
    # Basé sur le profil utilisateur
    if 'data' in st.session_state and 'travel_profile' in st.session_state.data:
        profile = st.session_state.data['travel_profile']
        
        # Recommandations personnalisées
        st.subheader("🎯 Recommandations Personnalisées")
        
        recommendations = []
        
        # Musées (score 5)
        if profile.get('museums_interest', 0) >= 4:
            recommendations.extend([
                "🏛️ Musée National de Tokyo",
                "🎨 Musée Ghibli",
                "🎭 TeamLab Borderless",
                "🏛️ Musée Edo-Tokyo",
                "🎨 Mori Art Museum"
            ])
        
        # Architecture moderne (score 5)
        if profile.get('modern_architecture', 0) >= 4:
            recommendations.extend([
                "🗼 Tokyo Skytree",
                "🏢 Tokyo Tower",
                "🌉 Rainbow Bridge",
                "🏢 Shibuya Scramble",
                "🏢 Umeda Sky Building (Osaka)"
            ])
        
        # Randonnée (score 5)
        if profile.get('hiking_interest', 0) >= 4:
            recommendations.extend([
                "⛰️ Mont Takao",
                "🏔️ Alpes Japonaises",
                "🌲 Sentier Nakasendo",
                "⛰️ Mont Fuji (saison)",
                "🌿 Parc national de Nikko"
            ])
        
        # Onsen (score 4)
        if profile.get('onsen_importance', 0) >= 4:
            recommendations.extend([
                "♨️ Hakone",
                "♨️ Kusatsu",
                "♨️ Beppu",
                "♨️ Ginzan Onsen",
                "♨️ Yufuin"
            ])
        
        # Sumo (intérêt spécifique)
        if "sumo" in profile.get('specific_interests', '').lower():
            recommendations.extend([
                "🤼 Ryogoku Kokugikan (Tokyo)",
                "🤼 Osaka Prefectural Gymnasium",
                "🤼 Aichi Prefectural Gymnasium"
            ])
        
        # Affichage des recommandations
        if recommendations:
            for rec in recommendations:
                st.markdown(f"• {rec}")
        else:
            st.info("Complétez votre profil de voyage pour recevoir des recommandations personnalisées")
    
    # Applications culturelles
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎭 Culture & Événements")
        st.markdown("""
        **🎫 Viator**
        - Visites guidées
        - Expériences culturelles
        
        **🎫 Klook**
        - Activités populaires
        - Billets attractions
        
        **🎫 GetYourGuide**
        - Tours organisés
        - Skip-the-line tickets
        
        **🎫 Japan Experience**
        - Spécialisé Japon
        - Expériences authentiques
        """)
    
    with col2:
        st.subheader("🎪 Événements")
        st.markdown("""
        **🌸 Hanami (Avril)**
        - Cerisiers en fleur
        - Parcs populaires
        
        **🎆 Matsuri (Été)**
        - Festivals locaux
        - Feux d'artifice
        
        **🍁 Momiji (Novembre)**
        - Érables rouges
        - Jardins traditionnels
        
        **❄️ Yuki Matsuri (Février)**
        - Festival de neige
        - Sapporo
        """)
    
    # === SECTION 7: MÉTÉO & SANTÉ ===
    st.header("🌤️ Météo & Santé")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌤️ Météo")
        st.markdown("""
        **🌤️ Tenki.jp**
        - Météo japonaise officielle
        - Prévisions précises
        
        **🌤️ Weather.com**
        - Interface internationale
        - Alertes météo
        
        **🌤️ AccuWeather**
        - Prévisions détaillées
        - Radar météo
        
        **🌤️ Yahoo Weather**
        - Interface simple
        - Données locales
        """)
    
    with col2:
        st.subheader("🏥 Santé")
        st.markdown("""
        **🏥 Japan Health Info**
        - Info santé voyage
        - Hôpitaux anglophones
        
        **🏥 Tokyo Medical Info**
        - Cliniques Tokyo
        - Services d'urgence
        
        **🏥 Osaka Medical Info**
        - Soins Osaka
        - Pharmacies 24h
        
        **🏥 Kyoto Medical Info**
        - Services Kyoto
        - Traduction médicale
        """)
    
    # === SECTION 8: LIENS OFFICIELS ===
    st.header("🏛️ Liens Officiels")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🇯🇵 Gouvernement")
        st.markdown("""
        **🏛️ Ambassade du Japon**
        - [fr.emb-japan.go.jp](https://www.fr.emb-japan.go.jp/)
        - Visa et documents
        
        **🏛️ JNTO**
        - [japan.travel](https://www.japan.travel/)
        - Office tourisme officiel
        
        **🏛️ Ministère Affaires Étrangères**
        - Conseils voyage
        - Sécurité
        """)
    
    with col2:
        st.subheader("🚄 Transport Officiel")
        st.markdown("""
        **🚄 JR East**
        - [jreast.co.jp](https://www.jreast.co.jp/e/)
        - Trains région Tokyo
        
        **🚄 JR West**
        - [jrwest.co.jp](https://www.jrwest.co.jp/)
        - Trains région Osaka
        
        **🚄 JR Central**
        - [jr-central.co.jp](https://www.jr-central.co.jp/)
        - Shinkansen Tokaido
        
        **🚄 Japan Rail Pass**
        - [japan-rail-pass.fr](https://www.japan-rail-pass.fr/)
        - Réservations officielles
        """)
    
    with col3:
        st.subheader("🏛️ Services Publics")
        st.markdown("""
        **🏛️ Police Japon**
        - Services d'urgence
        - 110 (police)
        
        **🏛️ Pompiers**
        - Services d'urgence
        - 119 (pompiers)
        
        **🏛️ Immigration**
        - Services visa
        - Prolongation séjour
        """)
    
    # === SECTION 9: RESSOURCES SPÉCIALISÉES ===
    st.header("🎯 Ressources Spécialisées")
    
    # Basé sur les intérêts du profil
    if 'data' in st.session_state and 'travel_profile' in st.session_state.data:
        profile = st.session_state.data['travel_profile']
        
        # Ressources par intérêt
        interests_resources = {
            "manga_anime": {
                "title": "📚 Manga & Anime",
                "resources": [
                    "🏪 Akihabara (Tokyo) - Quartier otaku",
                    "🏪 Nakano Broadway (Tokyo) - Manga vintage",
                    "🏪 Denden Town (Osaka) - Électronique & manga",
                    "🎭 Ghibli Museum (Tokyo) - Réservation obligatoire",
                    "🎭 Universal Studios Japan (Osaka) - Attractions anime"
                ]
            },
            "gaming": {
                "title": "🎮 Gaming",
                "resources": [
                    "🏪 Super Potato (Akihabara) - Rétro gaming",
                    "🏪 BicCamera - Consoles modernes",
                    "🎮 SEGA Arcades - Arcades classiques",
                    "🎮 Taito Station - Jeux d'arcade",
                    "🎮 Round1 - Bowling & jeux"
                ]
            },
            "hiking_interest": {
                "title": "⛰️ Randonnée",
                "resources": [
                    "🗺️ Yamap - Application randonnée",
                    "🗺️ AllTrails - Sentiers internationaux",
                    "⛰️ Japan Hiking - Guide spécialisé",
                    "🏔️ Alpes Japonaises - Parcs nationaux",
                    "🌲 Nakasendo Trail - Chemin historique"
                ]
            },
            "japanese_gardens": {
                "title": "🌿 Jardins Japonais",
                "resources": [
                    "🌿 Kenroku-en (Kanazawa) - Un des 3 grands jardins",
                    "🌿 Ryoan-ji (Kyoto) - Jardin zen",
                    "🌿 Kinkaku-ji (Kyoto) - Pavillon d'or",
                    "🌿 Ginkaku-ji (Kyoto) - Pavillon d'argent",
                    "🌿 Koraku-en (Okayama) - Jardin paysager"
                ]
            }
        }
        
        # Affichage des ressources spécialisées
        for interest_key, interest_data in interests_resources.items():
            if profile.get(interest_key, 0) >= 3:  # Intérêt moyen ou plus
                with st.expander(interest_data["title"], expanded=False):
                    for resource in interest_data["resources"]:
                        st.markdown(f"• {resource}")
    
    # === SECTION 10: APPLICATIONS MOBILES ===
    st.header("📱 Applications Mobiles Essentielles")
    
    # Applications par catégorie
    apps_categories = {
        "🚄 Transport": [
            "Hyperdia - Horaires trains",
            "Google Maps - Navigation",
            "Japan Transit Planner - Itinéraires",
            "Japan Taxi - Réservation taxis",
            "Tokyo Subway Navigation"
        ],
        "🌐 Communication": [
            "Google Translate - Traduction",
            "DeepL - Traduction précise",
            "LINE - Messagerie locale",
            "WhatsApp - Communication internationale",
            "Discord - Communauté voyageurs"
        ],
        "🍽️ Nourriture": [
            "Tabelog - Restaurants japonais",
            "Gurunavi - Guide restaurants",
            "Uber Eats - Livraison",
            "HotPepper - Offres restaurants",
            "OpenTable - Réservations"
        ],
        "🏨 Hébergement": [
            "Booking.com - Réservations hôtels",
            "Airbnb - Appartements locaux",
            "Japanican - Ryokan traditionnels",
            "Hostelworld - Auberges",
            "Rakuten Travel - Onsen"
        ],
        "🎭 Culture": [
            "Viator - Visites guidées",
            "Klook - Activités populaires",
            "GetYourGuide - Tours organisés",
            "Japan Experience - Expériences",
            "Tokyo Art Beat - Événements culturels"
        ],
        "🌤️ Utilitaires": [
            "Tenki.jp - Météo japonaise",
            "Google Lens - Traduction photo",
            "Pocket WiFi - Connexion internet",
            "Japan Official Travel App",
            "Tokyo Metro - Plan métro"
        ]
    }
    
    # Affichage des applications
    for category, apps in apps_categories.items():
        with st.expander(category, expanded=False):
            for app in apps:
                st.markdown(f"• {app}")
    
    # === SECTION 11: CONSEILS PRATIQUES ===
    st.header("💡 Conseils Pratiques")
    
    # Conseils par thème
    tips_categories = {
        "💰 Argent": [
            "Préférez les cartes de crédit sans frais à l'étranger",
            "Retirez de l'argent dans les konbini (7-Eleven, Lawson)",
            "Gardez toujours des espèces pour les petits commerces",
            "Évitez les bureaux de change à l'aéroport (taux défavorables)",
            "Utilisez des cartes prépayées comme Pasmo/Suica"
        ],
        "🚄 Transport": [
            "Réservez votre JR Pass avant le départ",
            "Téléchargez les cartes hors ligne de Google Maps",
            "Préférez les trains aux bus pour les longues distances",
            "Évitez les taxis sauf en cas d'urgence (très chers)",
            "Utilisez les pass de transport journaliers en ville"
        ],
        "🍽️ Nourriture": [
            "Les restaurants affichent souvent des modèles en vitrine",
            "Pointage du doigt fonctionne bien pour commander",
            "Les ramen se mangent bruyamment (c'est normal !)",
            "Grattez les bols de riz (c'est poli)",
            "Évitez de marcher en mangeant"
        ],
        "🏨 Hébergement": [
            "Réservez tôt pour les périodes de pointe (Golden Week, Hanami)",
            "Les chambres sont souvent plus petites qu'en Europe",
            "Préférez les hôtels près des gares pour la praticité",
            "Les ryokan ont des règles strictes (respectez-les)",
            "Vérifiez les horaires de check-in/check-out"
        ],
        "📱 Internet": [
            "Louez un Pocket WiFi à l'aéroport",
            "Ou achetez une carte SIM data",
            "Téléchargez les cartes hors ligne",
            "Utilisez les WiFi gratuits des konbini",
            "Préparez une liste de mots-clés en japonais"
        ],
        "🎭 Culture": [
            "Retirez vos chaussures dans les temples/ryokan",
            "Évitez de manger dans le métro",
            "Faites la queue proprement",
            "Soyez silencieux dans les transports",
            "Respectez les règles de photographie"
        ]
    }
    
    # Affichage des conseils
    for category, tips in tips_categories.items():
        with st.expander(category, expanded=False):
            for tip in tips:
                st.markdown(f"• {tip}")
    
    # === SECTION 12: CONTACTS D'URGENCE ===
    st.header("🚨 Contacts d'Urgence")
    
    emergency_contacts = {
        "🚔 Police": "110",
        "🚒 Pompiers/Ambulance": "119",
        "🏥 Services d'urgence": "119",
        "📞 Ambassade de France (Tokyo)": "+81-3-5798-6000",
        "📞 Consulat de France (Osaka)": "+81-6-4790-1500",
        "📞 Consulat de France (Kyoto)": "+81-75-761-8105"
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        for service, number in list(emergency_contacts.items())[:3]:
            st.markdown(f"**{service}** : `{number}`")
    
    with col2:
        for service, number in list(emergency_contacts.items())[3:]:
            st.markdown(f"**{service}** : `{number}`")
    
    # === FOOTER ===
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #888;'>
        <p>🔗 Centre de Ressources Japon - Mise à jour : {}</p>
        <p>💡 Ces ressources sont basées sur votre profil de voyage personnalisé</p>
    </div>
    """.format(datetime.now().strftime("%d/%m/%Y")), unsafe_allow_html=True) 