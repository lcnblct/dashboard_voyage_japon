#!/usr/bin/env python3
"""
Test de l'assistant IA dans le contexte Streamlit
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from modules.ai_assistant import send_message_to_ai, build_ai_context
from data.models import get_default_travel_profile

def test_ai_assistant():
    """Test de l'assistant IA"""
    
    print("🧪 Test de l'assistant IA")
    print("=" * 40)
    
    # Simulation de l'environnement Streamlit
    if 'ai_messages' not in st.session_state:
        st.session_state.ai_messages = []
        st.session_state.ai_client = None
    
    # Récupération du profil de voyage
    profile = get_default_travel_profile()
    print(f"📋 Profil de voyage chargé : {profile.get('travelers', 'Non spécifié')} voyageurs")
    
    # Test de construction du contexte
    context = build_ai_context(profile)
    print(f"📝 Contexte construit ({len(context)} caractères)")
    
    # Test d'envoi de message
    test_message = "Bonjour, peux-tu me donner quelques conseils pour visiter Tokyo ?"
    print(f"💬 Envoi du message de test : {test_message}")
    
    try:
        send_message_to_ai(test_message, profile)
        print("✅ Message envoyé avec succès")
        
        # Affichage de l'historique
        if st.session_state.ai_messages:
            print(f"📝 {len(st.session_state.ai_messages)} messages dans l'historique")
            for i, msg in enumerate(st.session_state.ai_messages):
                role = "👤 Utilisateur" if msg["role"] == "user" else "🤖 Assistant"
                print(f"   {i+1}. {role} ({msg['timestamp']}): {msg['content'][:100]}...")
        else:
            print("❌ Aucun message dans l'historique")
            
    except Exception as e:
        print(f"❌ Erreur lors de l'envoi du message : {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_ai_assistant() 