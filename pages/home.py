# Page d'accueil
import streamlit as st
import pandas as pd
from datetime import datetime, date
from data.models import get_default_travel_profile
from utils.helpers import calculate_days_until_departure, get_progress_percentage, format_currency

def display_home():
    """Affiche la page d'accueil avec le tableau de bord moderne"""
    
    # En-tête avec gradient
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="margin: 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
            🗾 Tableau de Bord Japon
        </h1>
        <p style="color: #94a3b8; font-size: 1.1rem; margin-top: 0.5rem;">
            Votre compagnon de voyage intelligent
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    data = st.session_state.data
    
    # Affichage du profil de voyage
    profile = data.get("travel_profile", get_default_travel_profile())
    
    # Métriques principales avec style moderne
    st.markdown("### 📊 Vue d'ensemble")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Date de départ
        dep_date = data.get("departure_date") or profile.get("arrival_date")
        if dep_date:
            days_left = calculate_days_until_departure(dep_date)
            if days_left is not None:
                if days_left >= 0:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 1.5rem; border-radius: 16px; text-align: center; color: white; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
                        <div style="font-size: 2rem; font-weight: bold;">{days_left}</div>
                        <div style="font-size: 0.9rem; opacity: 0.9;">jours restants</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 1.5rem; border-radius: 16px; text-align: center; color: white; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
                        <div style="font-size: 1.5rem; font-weight: bold;">🎉 Voyage en cours !</div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("📅 Veuillez renseigner la date de départ dans l'itinéraire.")
        else:
            st.info("📅 Veuillez renseigner la date de départ dans l'itinéraire.")
    
    with col2:
        # Budget
        total = sum([b["amount"] for b in data.get("budget", [])])
        budget_per_day = profile.get("budget_per_day", 150)
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 16px; text-align: center; color: white; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
            <div style="font-size: 1.5rem; font-weight: bold;">{format_currency(total)}</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">budget dépensé</div>
            <div style="font-size: 0.8rem; margin-top: 0.5rem; opacity: 0.8;">Objectif: {budget_per_day}€/jour</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        # Progression checklist
        checklist = data.get("checklist", {})
        total_items = len(checklist)
        completed_items = sum(checklist.values())
        progress_percentage = get_progress_percentage(completed_items, total_items)
        
        # Couleur basée sur la progression
        if progress_percentage >= 80:
            gradient = "linear-gradient(135deg, #10b981 0%, #059669 100%)"
        elif progress_percentage >= 50:
            gradient = "linear-gradient(135deg, #f59e0b 0%, #d97706 100%)"
        else:
            gradient = "linear-gradient(135deg, #ef4444 0%, #dc2626 100%)"
        
        st.markdown(f"""
        <div style="background: {gradient}; padding: 1.5rem; border-radius: 16px; text-align: center; color: white; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
            <div style="font-size: 1.5rem; font-weight: bold;">{completed_items}/{total_items}</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">tâches complétées</div>
            <div style="font-size: 0.8rem; margin-top: 0.5rem; opacity: 0.8;">{progress_percentage:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Profil de voyage avec cartes modernes
    st.markdown("### 👥 Votre Profil de Voyage")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div style="background: #334155; padding: 1.25rem; border-radius: 16px; border: 1px solid #475569; margin: 0.5rem 0;">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <span style="font-size: 1.5rem; margin-right: 0.5rem;">👥</span>
                <strong>Voyageurs</strong>
            </div>
            <div style="color: #cbd5e1; font-size: 1.1rem;">{profile.get('travelers', 'Non défini')}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="background: #334155; padding: 1.25rem; border-radius: 16px; border: 1px solid #475569; margin: 0.5rem 0;">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <span style="font-size: 1.5rem; margin-right: 0.5rem;">⭐</span>
                <strong>Expérience</strong>
            </div>
            <div style="color: #cbd5e1; font-size: 1.1rem;">{profile.get('experience', 'Non défini')}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="background: #334155; padding: 1.25rem; border-radius: 16px; border: 1px solid #475569; margin: 0.5rem 0;">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <span style="font-size: 1.5rem; margin-right: 0.5rem;">🎯</span>
                <strong>Priorité N°1</strong>
            </div>
            <div style="color: #cbd5e1; font-size: 1.1rem;">{profile.get('priority_1', 'Non définie')}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        rhythm = profile.get('travel_rhythm', 3)
        rhythm_emoji = "🐌" if rhythm <= 2 else "🚶" if rhythm <= 3 else "🏃" if rhythm <= 4 else "⚡"
        
        st.markdown(f"""
        <div style="background: #334155; padding: 1.25rem; border-radius: 16px; border: 1px solid #475569; margin: 0.5rem 0;">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <span style="font-size: 1.5rem; margin-right: 0.5rem;">{rhythm_emoji}</span>
                <strong>Rythme</strong>
            </div>
            <div style="color: #cbd5e1; font-size: 1.1rem;">{rhythm}/5 (1=très cool, 5=très intense)</div>
        </div>
        """, unsafe_allow_html=True)
        
        crowd = profile.get('crowd_tolerance', 3)
        crowd_emoji = "🏃" if crowd <= 2 else "🚶" if crowd <= 3 else "👥" if crowd <= 4 else "🎉"
        
        st.markdown(f"""
        <div style="background: #334155; padding: 1.25rem; border-radius: 16px; border: 1px solid #475569; margin: 0.5rem 0;">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <span style="font-size: 1.5rem; margin-right: 0.5rem;">{crowd_emoji}</span>
                <strong>Tolérance foule</strong>
            </div>
            <div style="color: #cbd5e1; font-size: 1.1rem;">{crowd}/5 (1=je fuis, 5=ça me stimule)</div>
        </div>
        """, unsafe_allow_html=True)
        
        museums = profile.get('museums_interest', 3)
        museums_emoji = "😴" if museums <= 2 else "🤔" if museums <= 3 else "🤓" if museums <= 4 else "🏛️"
        
        st.markdown(f"""
        <div style="background: #334155; padding: 1.25rem; border-radius: 16px; border: 1px solid #475569; margin: 0.5rem 0;">
            <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                <span style="font-size: 1.5rem; margin-right: 0.5rem;">{museums_emoji}</span>
                <strong>Intérêt musées</strong>
            </div>
            <div style="color: #cbd5e1; font-size: 1.1rem;">{museums}/5</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Recommandations rapides avec style moderne
    st.markdown("### 🎯 Recommandations Personnalisées")
    
    recommendations = []
    
    if profile.get("museums_interest", 3) >= 4:
        recommendations.append(("🏛️", "Musées prioritaires", "Musée national de Tokyo, Musée Ghibli"))
    
    if profile.get("modern_architecture", 3) >= 4:
        recommendations.append(("🏢", "Architecture moderne", "Tokyo Skytree, Shibuya Scramble"))
    
    if profile.get("hiking_interest", 3) >= 4:
        recommendations.append(("🏔️", "Randonnées", "Mont Takao, Alpes japonaises"))
    
    if profile.get("onsen_importance", 3) >= 4:
        recommendations.append(("♨️", "Onsen", "Hakone, Kusatsu"))
    
    if "Sumo" in profile.get("specific_interests", ""):
        recommendations.append(("🤼", "Sumo", "Réservation obligatoire pour les tournois"))
    
    if profile.get("travel_rhythm", 3) >= 4:
        recommendations.append(("⚡", "Rythme intense", "Planifier 2-3 activités par jour"))
    
    # Affichage des recommandations
    if recommendations:
        for i, (emoji, title, desc) in enumerate(recommendations[:3]):
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(99, 102, 241, 0.05) 100%); border: 1px solid rgba(99, 102, 241, 0.2); border-left: 4px solid #6366f1; padding: 1.25rem; border-radius: 16px; margin: 0.5rem 0;">
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <span style="font-size: 1.5rem; margin-right: 0.5rem;">{emoji}</span>
                    <strong style="color: #f8fafc;">{title}</strong>
                </div>
                <div style="color: #cbd5e1;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("💡 Complétez votre profil de voyage pour recevoir des recommandations personnalisées !")
    
    # Prochaine tâche prioritaire avec style moderne
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
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(249, 115, 22, 0.1) 0%, rgba(249, 115, 22, 0.05) 100%); border: 1px solid rgba(249, 115, 22, 0.2); border-left: 4px solid #f97316; padding: 1.25rem; border-radius: 16px; margin: 0.5rem 0;">
            <div style="display: flex; align-items: center;">
                <span style="font-size: 1.5rem; margin-right: 0.5rem;">🎯</span>
                <div>
                    <strong style="color: #f8fafc;">Prochaine tâche à faire :</strong>
                    <div style="color: #cbd5e1; margin-top: 0.25rem;">{next_task}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    elif completed_items == total_items and total_items > 0:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%); border: 1px solid rgba(16, 185, 129, 0.2); border-left: 4px solid #10b981; padding: 1.25rem; border-radius: 16px; margin: 0.5rem 0;">
            <div style="display: flex; align-items: center;">
                <span style="font-size: 1.5rem; margin-right: 0.5rem;">🎊</span>
                <div>
                    <strong style="color: #f8fafc;">Félicitations !</strong>
                    <div style="color: #cbd5e1; margin-top: 0.25rem;">Toutes les tâches de la checklist sont complétées !</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True) 