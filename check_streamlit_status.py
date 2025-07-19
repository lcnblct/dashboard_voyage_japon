#!/usr/bin/env python3
"""
Vérification de l'état de l'application Streamlit
"""

import requests
import time
import subprocess
import sys
import os

def check_streamlit_app():
    """Vérifie si l'application Streamlit fonctionne"""
    
    print("🔍 Vérification de l'application Streamlit")
    print("=" * 50)
    
    # URL de l'application
    url = "http://localhost:8502"
    
    try:
        # Test de connexion
        print(f"🌐 Test de connexion à {url}")
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print("✅ Application accessible")
            print(f"   Status code: {response.status_code}")
            print(f"   Taille de la réponse: {len(response.content)} caractères")
            
            # Vérification du contenu
            if "Assistant IA" in response.text:
                print("✅ Page de l'assistant IA détectée")
            else:
                print("⚠️  Page de l'assistant IA non détectée")
                
            return True
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Impossible de se connecter à l'application")
        print("   L'application Streamlit n'est peut-être pas démarrée")
        return False
    except requests.exceptions.Timeout:
        print("❌ Timeout lors de la connexion")
        return False
    except Exception as e:
        print(f"❌ Erreur inattendue: {str(e)}")
        return False

def check_streamlit_process():
    """Vérifie si le processus Streamlit est en cours d'exécution"""
    
    print("\n🔍 Vérification du processus Streamlit")
    print("=" * 50)
    
    try:
        # Recherche des processus Streamlit
        result = subprocess.run(
            ["ps", "aux"], 
            capture_output=True, 
            text=True
        )
        
        if "streamlit" in result.stdout.lower():
            print("✅ Processus Streamlit détecté")
            lines = result.stdout.split('\n')
            for line in lines:
                if "streamlit" in line.lower() and "app.py" in line:
                    print(f"   Processus: {line.strip()}")
        else:
            print("❌ Aucun processus Streamlit détecté")
            
    except Exception as e:
        print(f"❌ Erreur lors de la vérification des processus: {str(e)}")

def start_streamlit_if_needed():
    """Démarre Streamlit si nécessaire"""
    
    print("\n🚀 Démarrage de Streamlit")
    print("=" * 50)
    
    if not check_streamlit_app():
        print("🔄 Démarrage de l'application Streamlit...")
        
        try:
            # Démarrage en arrière-plan
            process = subprocess.Popen(
                ["streamlit", "run", "app.py", "--server.port", "8502"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            print("⏳ Attente du démarrage...")
            time.sleep(5)
            
            # Vérification après démarrage
            if check_streamlit_app():
                print("✅ Application démarrée avec succès")
                return True
            else:
                print("❌ Échec du démarrage")
                return False
                
        except Exception as e:
            print(f"❌ Erreur lors du démarrage: {str(e)}")
            return False
    else:
        print("✅ L'application est déjà en cours d'exécution")
        return True

def main():
    """Fonction principale"""
    
    print("🔧 Diagnostic complet de l'application Streamlit")
    print("=" * 60)
    
    # Vérification de l'environnement
    print("📋 Environnement:")
    print(f"   Python: {sys.version}")
    print(f"   Répertoire: {os.getcwd()}")
    
    # Vérification des processus
    check_streamlit_process()
    
    # Vérification de l'application
    if check_streamlit_app():
        print("\n✅ L'application fonctionne correctement")
        print("\n🔧 Si l'assistant IA ne fonctionne pas dans l'interface:")
        print("1. Vérifiez que vous êtes sur la page 'Assistant IA'")
        print("2. Vérifiez que la clé API est correctement configurée")
        print("3. Essayez de rafraîchir la page")
        print("4. Vérifiez les logs de l'application")
    else:
        print("\n❌ L'application n'est pas accessible")
        print("\n🔧 Solutions:")
        print("1. Démarrez l'application avec: streamlit run app.py")
        print("2. Vérifiez que le port 8502 n'est pas utilisé")
        print("3. Vérifiez les logs d'erreur")
        
        # Tentative de démarrage automatique
        start_streamlit_if_needed()

if __name__ == "__main__":
    main() 