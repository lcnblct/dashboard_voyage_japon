# Page des réglages
import streamlit as st
import os
from datetime import datetime
from data.storage import export_data, sync_state, load_data
from config.settings import DATA_FILE

def display_settings():
    """Affiche la page des réglages"""
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