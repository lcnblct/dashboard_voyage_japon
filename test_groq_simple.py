#!/usr/bin/env python3
"""
Test simple de l'API Groq sans clé hardcodée
"""

import groq
import os

def test_groq_connection():
    """Teste la connexion à l'API Groq"""
    
    # Récupération de la clé API depuis les secrets Streamlit
    try:
        import streamlit as st
        api_key = st.secrets.get("GROQ_API_KEY", "")
    except:
        # Fallback pour les tests en ligne de commande
        api_key = os.getenv("GROQ_API_KEY", "")
    
    if not api_key:
        print("❌ Aucune clé API trouvée")
        print("   Configurez GROQ_API_KEY dans .streamlit/secrets.toml ou comme variable d'environnement")
        return False
    
    print(f"🔑 Clé API trouvée : {api_key[:10]}...")
    
    try:
        # Initialisation du client
        client = groq.Groq(api_key=api_key)
        print("✅ Client Groq initialisé avec succès")
        
        # Test simple
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": "Bonjour, test simple"}],
            max_tokens=50,
            temperature=0.1
        )
        
        print(f"✅ Test réussi")
        print(f"   Réponse : {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ Erreur : {str(e)}")
        return False

if __name__ == "__main__":
    print("🔍 Test simple de l'API Groq")
    print("=" * 40)
    
    success = test_groq_connection()
    
    if success:
        print("\n✅ L'API Groq fonctionne correctement")
    else:
        print("\n❌ Problème détecté avec l'API Groq") 