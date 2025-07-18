# Modèles de données par défaut pour l'application

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