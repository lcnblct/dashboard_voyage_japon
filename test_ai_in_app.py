#!/usr/bin/env python3
"""
Test de l'assistant IA dans l'application Streamlit
"""

import requests
import json
import time

def test_ai_assistant_in_app():
    """Test de l'assistant IA via l'interface web"""
    
    print("🧪 Test de l'assistant IA dans l'application")
    print("=" * 50)
    
    # URL de l'application
    base_url = "http://localhost:8502"
    
    try:
        # Test de connexion à la page principale
        print("🌐 Test de connexion à l'application...")
        response = requests.get(base_url, timeout=10)
        
        if response.status_code == 200:
            print("✅ Application accessible")
            
            # Vérification du contenu
            content = response.text
            if "Assistant IA" in content:
                print("✅ Page de l'assistant IA détectée")
            else:
                print("⚠️  Page de l'assistant IA non détectée dans la page principale")
                
            # Test de navigation vers la page assistant IA
            print("\n🔍 Test de navigation vers l'assistant IA...")
            
            # Note: Streamlit ne supporte pas directement les requêtes POST pour les interactions
            # Nous allons vérifier que la page est accessible
            ai_page_url = f"{base_url}/Assistant_IA"
            try:
                ai_response = requests.get(ai_page_url, timeout=10)
                if ai_response.status_code == 200:
                    print("✅ Page de l'assistant IA accessible")
                else:
                    print(f"⚠️  Page de l'assistant IA non accessible (status: {ai_response.status_code})")
            except:
                print("⚠️  Impossible d'accéder directement à la page de l'assistant IA")
                print("   Cela est normal, Streamlit gère les pages différemment")
            
            return True
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Impossible de se connecter à l'application")
        return False
    except Exception as e:
        print(f"❌ Erreur inattendue: {str(e)}")
        return False

def check_streamlit_logs():
    """Vérifie les logs de Streamlit pour des erreurs"""
    
    print("\n📋 Vérification des logs Streamlit")
    print("=" * 50)
    
    print("🔍 Pour voir les logs en temps réel, utilisez:")
    print("   streamlit run app.py --logger.level debug")
    print("\n🔍 Ou vérifiez les logs dans le terminal où Streamlit est lancé")

def provide_troubleshooting_guide():
    """Fournit un guide de dépannage"""
    
    print("\n🔧 Guide de dépannage de l'assistant IA")
    print("=" * 50)
    
    print("Si l'assistant IA ne fonctionne pas :")
    print("\n1. ✅ Vérifications de base :")
    print("   - L'application Streamlit est-elle démarrée ?")
    print("   - Êtes-vous sur la page 'Assistant IA' ?")
    print("   - Votre clé API Groq est-elle configurée ?")
    
    print("\n2. 🔑 Vérification de la clé API :")
    print("   - Vérifiez le fichier .streamlit/secrets.toml")
    print("   - La clé doit commencer par 'gsk_'")
    print("   - Testez la clé avec le script test_groq_debug.py")
    
    print("\n3. 🌐 Vérification de la connexion :")
    print("   - Vérifiez votre connexion internet")
    print("   - Testez l'accès à https://console.groq.com/")
    print("   - Vérifiez votre quota d'utilisation Groq")
    
    print("\n4. 🔄 Solutions de redémarrage :")
    print("   - Redémarrez l'application Streamlit")
    print("   - Effacez le cache du navigateur")
    print("   - Redémarrez votre navigateur")
    
    print("\n5. 📝 Logs et débogage :")
    print("   - Vérifiez les logs dans le terminal")
    print("   - Utilisez le mode debug de Streamlit")
    print("   - Testez avec un message simple")

def main():
    """Fonction principale"""
    
    print("🔍 Diagnostic complet de l'assistant IA")
    print("=" * 60)
    
    # Test de l'application
    if test_ai_assistant_in_app():
        print("\n✅ L'application fonctionne correctement")
        print("\n🎯 Prochaines étapes :")
        print("1. Ouvrez http://localhost:8502 dans votre navigateur")
        print("2. Naviguez vers la page 'Assistant IA'")
        print("3. Testez l'envoi d'un message simple")
        print("4. Vérifiez que la réponse s'affiche correctement")
        
        # Guide de dépannage
        provide_troubleshooting_guide()
        
    else:
        print("\n❌ L'application n'est pas accessible")
        print("\n🔧 Solutions :")
        print("1. Démarrez l'application : streamlit run app.py")
        print("2. Vérifiez que le port 8502 n'est pas utilisé")
        print("3. Vérifiez les logs d'erreur")
    
    # Vérification des logs
    check_streamlit_logs()

if __name__ == "__main__":
    main() 