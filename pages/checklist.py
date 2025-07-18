# Page de la checklist
import streamlit as st
import pandas as pd
from data.models import get_default_checklist
from data.storage import sync_state
from utils.helpers import get_progress_percentage

def display_checklist():
    """Affiche la page de la checklist moderne"""
    
    # En-tête stylisé
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="margin: 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
            ✅ Checklist de Préparation
        </h1>
        <p style="color: #94a3b8; font-size: 1.1rem; margin-top: 0.5rem;">
            Organisez votre voyage étape par étape
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    data = st.session_state.data
    checklist = data.get("checklist", get_default_checklist())
    
    # Calcul de la progression
    total_items = len(checklist)
    completed_items = sum(checklist.values())
    progress_percentage = get_progress_percentage(completed_items, total_items)
    
    # Affichage de la progression avec style moderne
    st.markdown("### 📊 Progression Globale")
    
    # Couleur basée sur la progression
    if progress_percentage >= 80:
        progress_color = "#10b981"
        progress_gradient = "linear-gradient(135deg, #10b981 0%, #059669 100%)"
    elif progress_percentage >= 50:
        progress_color = "#f59e0b"
        progress_gradient = "linear-gradient(135deg, #f59e0b 0%, #d97706 100%)"
    else:
        progress_color = "#ef4444"
        progress_gradient = "linear-gradient(135deg, #ef4444 0%, #dc2626 100%)"
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.markdown(f"""
        <div style="background: {progress_gradient}; padding: 1.5rem; border-radius: 16px; text-align: center; color: white; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
            <div style="font-size: 2rem; font-weight: bold;">{completed_items}/{total_items}</div>
            <div style="font-size: 1rem; opacity: 0.9;">tâches complétées</div>
            <div style="font-size: 0.9rem; margin-top: 0.5rem; opacity: 0.8;">{progress_percentage:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: #334155; padding: 1.5rem; border-radius: 16px; border: 1px solid #475569; text-align: center; color: white;">
            <div style="font-size: 1.5rem; font-weight: bold; color: {progress_color};">{progress_percentage:.0f}%</div>
            <div style="font-size: 0.9rem; color: #cbd5e1;">complété</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        remaining = total_items - completed_items
        st.markdown(f"""
        <div style="background: #334155; padding: 1.5rem; border-radius: 16px; border: 1px solid #475569; text-align: center; color: white;">
            <div style="font-size: 1.5rem; font-weight: bold; color: #f59e0b;">{remaining}</div>
            <div style="font-size: 0.9rem; color: #cbd5e1;">restantes</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Barre de progression stylisée
    st.markdown(f"""
    <div style="background: #1e293b; border-radius: 12px; padding: 0.5rem; margin: 1rem 0;">
        <div style="background: {progress_gradient}; height: 8px; border-radius: 6px; width: {progress_percentage}%; transition: width 0.5s ease;"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Groupes de la checklist avec icônes
    groups = {
        "📋 Documents Essentiels": {
            "icon": "📋",
            "color": "#3b82f6",
            "gradient": "linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%)",
            "items": ["passeport_valide", "billet_avion", "jr_pass", "permis_conduire", "assurance", "carte_credit", "especes_yen"]
        },
        "📱 Électronique": {
            "icon": "📱",
            "color": "#8b5cf6",
            "gradient": "linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%)",
            "items": ["adaptateur", "chargeur_telephone", "batterie_externe", "appareil_photo", "carte_sd"]
        },
        "🧳 Bagages": {
            "icon": "🧳",
            "color": "#f59e0b",
            "gradient": "linear-gradient(135deg, #f59e0b 0%, #d97706 100%)",
            "items": ["valise", "vetements", "chaussures_confortables", "sous_vetements", "pyjama", "serviette", "produits_hygiene", "trousse_secours", "medicaments", "lunettes_contact"]
        },
        "📄 Préparatifs Administratifs": {
            "icon": "📄",
            "color": "#10b981",
            "gradient": "linear-gradient(135deg, #10b981 0%, #059669 100%)",
            "items": ["banque", "copie_documents", "photos_identite", "adresse_hotel", "itineraire_imprime"]
        },
        "📱 Applications Utiles": {
            "icon": "📱",
            "color": "#06b6d4",
            "gradient": "linear-gradient(135deg, #06b6d4 0%, #0891b2 100%)",
            "items": ["app_transport", "app_traduction", "app_meteo", "app_maps"]
        },
        "🎯 Préparatifs Pratiques": {
            "icon": "🎯",
            "color": "#ef4444",
            "gradient": "linear-gradient(135deg, #ef4444 0%, #dc2626 100%)",
            "items": ["reservation_hotels", "reservation_restaurants", "activites_reservees", "transport_aeroport", "guide_phrase"]
        }
    }
    
    # Labels pour l'affichage avec icônes
    labels = {
        "passeport_valide": ("🛂", "Passeport valide (6 mois après retour)"),
        "billet_avion": ("✈️", "Billet d'avion imprimé/PDF"),
        "jr_pass": ("🚄", "Réservation JR Pass"),
        "permis_conduire": ("🚗", "Permis de conduire international"),
        "assurance": ("🛡️", "Assurance voyage"),
        "carte_credit": ("💳", "Carte bancaire internationale"),
        "especes_yen": ("💴", "Prévoir des espèces en yen"),
        "adaptateur": ("🔌", "Adaptateur secteur Type A/B"),
        "chargeur_telephone": ("📱", "Chargeur téléphone"),
        "batterie_externe": ("🔋", "Batterie externe"),
        "appareil_photo": ("📸", "Appareil photo"),
        "carte_sd": ("💾", "Carte SD de rechange"),
        "valise": ("🧳", "Valise/sac à dos"),
        "vetements": ("👕", "Vêtements adaptés à la saison"),
        "chaussures_confortables": ("👟", "Chaussures confortables"),
        "sous_vetements": ("🩲", "Sous-vêtements"),
        "pyjama": ("🛏️", "Pyjama"),
        "serviette": ("🛁", "Serviette de toilette"),
        "produits_hygiene": ("🧴", "Produits d'hygiène"),
        "trousse_secours": ("🏥", "Trousse de premiers secours"),
        "medicaments": ("💊", "Médicaments personnels"),
        "lunettes_contact": ("👓", "Lunettes/contacts de rechange"),
        "banque": ("🏦", "Prévenir sa banque"),
        "copie_documents": ("📋", "Copies numériques des documents"),
        "photos_identite": ("🆔", "Photos d'identité"),
        "adresse_hotel": ("🏨", "Adresses des hôtels notées"),
        "itineraire_imprime": ("🗺️", "Itinéraire imprimé"),
        "app_transport": ("🚇", "App transport (Hyperdia, Google Maps)"),
        "app_traduction": ("🗣️", "App traduction (Google Translate)"),
        "app_meteo": ("🌤️", "App météo"),
        "app_maps": ("🗺️", "App cartes hors ligne"),
        "reservation_hotels": ("🏨", "Réservations hôtels confirmées"),
        "reservation_restaurants": ("🍜", "Réservations restaurants"),
        "activites_reservees": ("🎫", "Activités réservées"),
        "transport_aeroport": ("🚌", "Transport aéroport organisé"),
        "guide_phrase": ("📖", "Guide de phrases japonaises")
    }
    
    # Affichage par groupes avec design moderne
    for group_name, group_data in groups.items():
        items = group_data["items"]
        group_color = group_data["color"]
        group_gradient = group_data["gradient"]
        group_icon = group_data["icon"]
        
        # Calcul de la progression du groupe
        group_completed = sum(checklist[item] for item in items)
        group_total = len(items)
        group_progress = get_progress_percentage(group_completed, group_total)
        
        # En-tête du groupe
        st.markdown(f"""
        <div style="background: {group_gradient}; padding: 1rem 1.5rem; border-radius: 16px; margin: 2rem 0 1rem 0; color: white; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
            <div style="display: flex; align-items: center;">
                <span style="font-size: 1.5rem; margin-right: 0.5rem;">{group_icon}</span>
                <h3 style="margin: 0; color: white;">{group_name.split(' ', 1)[1]}</h3>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 1.2rem; font-weight: bold;">{group_completed}/{group_total}</div>
                <div style="font-size: 0.8rem; opacity: 0.9;">{group_progress:.0f}%</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Barre de progression du groupe
        st.markdown(f"""
        <div style="background: #1e293b; border-radius: 8px; padding: 0.25rem; margin: 0 0 1rem 0;">
            <div style="background: {group_gradient}; height: 6px; border-radius: 4px; width: {group_progress}%; transition: width 0.5s ease;"></div>
        </div>
        """, unsafe_allow_html=True)
        
        # Affichage des items en grille
        cols = st.columns(2)
        for i, item in enumerate(items):
            col_idx = i % 2
            item_icon, item_label = labels.get(item, ("📝", item))
            is_completed = checklist[item]
            
            with cols[col_idx]:
                # Bouton stylisé pour chaque tâche
                if st.button(
                    f"{item_icon} {item_label}",
                    key=f"btn_{item}",
                    use_container_width=True,
                    type="primary" if is_completed else "secondary"
                ):
                    # Inverser l'état
                    checklist[item] = not is_completed
                    sync_state()
                    st.rerun()
                
                # Affichage de l'état actuel
                if is_completed:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 0.5rem; margin: 0.25rem 0; text-align: center;">
                        <span style="color: #10b981; font-weight: bold;">✅ Complété</span>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="background: rgba(148, 163, 184, 0.1); border: 1px solid rgba(148, 163, 184, 0.3); border-radius: 8px; padding: 0.5rem; margin: 0.25rem 0; text-align: center;">
                        <span style="color: #94a3b8;">⭕ En attente</span>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Espacement entre les groupes
        st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)
    
    # Boutons d'action avec style moderne
    st.markdown("### 🔧 Actions")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("🔄 Réinitialiser", type="secondary", use_container_width=True):
            data["checklist"] = get_default_checklist()
            sync_state()
            st.success("Checklist réinitialisée !")
            st.rerun()
    
    with col2:
        if st.button("💾 Sauvegarder", type="primary", use_container_width=True):
            sync_state()
            st.success("Checklist sauvegardée !")
    
    with col3:
        if st.button("📊 Statistiques", type="secondary", use_container_width=True):
            st.info(f"📈 Statistiques détaillées : {completed_items}/{total_items} tâches complétées ({progress_percentage:.1f}%)")
    
    # Message de félicitations stylisé
    if completed_items == total_items and total_items > 0:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%); border: 1px solid rgba(16, 185, 129, 0.2); border-left: 4px solid #10b981; padding: 1.5rem; border-radius: 16px; margin: 2rem 0; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🎊</div>
            <h3 style="color: #f8fafc; margin: 0 0 0.5rem 0;">Félicitations !</h3>
            <p style="color: #cbd5e1; margin: 0; font-size: 1.1rem;">Toutes les tâches de la checklist sont complétées !</p>
            <p style="color: #94a3b8; margin: 0.5rem 0 0 0; font-size: 0.9rem;">Vous êtes prêt(e) pour votre voyage au Japon ! 🇯🇵</p>
        </div>
        """, unsafe_allow_html=True) 