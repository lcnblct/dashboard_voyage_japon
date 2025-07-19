#!/usr/bin/env python3
import requests
import time

def test_app():
    """Test si l'application Streamlit fonctionne"""
    url = "http://localhost:8501"
    
    print("Test de l'application Streamlit...")
    print(f"URL: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        print(f"Statut: {response.status_code}")
        print(f"Contenu (premiers 200 caractères): {response.text[:200]}")
        return True
    except requests.exceptions.ConnectionError:
        print("Erreur: Impossible de se connecter à l'application")
        return False
    except Exception as e:
        print(f"Erreur: {e}")
        return False

if __name__ == "__main__":
    # Attendre que l'application démarre
    print("Attente du démarrage de l'application...")
    time.sleep(15)
    
    success = test_app()
    if success:
        print("✅ L'application fonctionne correctement!")
        print("Vous pouvez maintenant accéder à l'application via votre navigateur.")
        print("Mot de passe: japon2024")
    else:
        print("❌ L'application ne répond pas.")