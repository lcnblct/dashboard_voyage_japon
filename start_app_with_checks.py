#!/usr/bin/env python3
"""
Script de démarrage amélioré avec vérifications complètes
"""

import subprocess
import sys
import os
import time
import requests
from pathlib import Path

def check_environment():
    """Vérifie l'environnement de développement"""
    
    print("🔍 Vérification de l'environnement")
    print("=" * 40)
    
    # Vérification de Python
    print(f"🐍 Python: {sys.version}")
    
    # Vérification du répertoire
    print(f"📁 Répertoire: {os.getcwd()}")
    
    # Vérification de l'environnement virtuel
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Environnement virtuel activé")
    else:
        print("⚠️  Environnement virtuel non détecté")
        print("   Recommandé: source venv/bin/activate")
    
    # Vérification des fichiers requis
    required_files = ['app.py', 'requirements.txt', '.streamlit/secrets.toml']
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} trouvé")
        else:
            print(f"❌ {file} manquant")
            return False
    
    return True

def check_dependencies():
    """Vérifie les dépendances"""
    
    print("\n📦 Vérification des dépendances")
    print("=" * 40)
    
    required_packages = ['streamlit', 'groq', 'pandas', 'folium']
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} installé")
        except ImportError:
            print(f"❌ {package} non installé")
            print(f"   Installez avec: pip install {package}")
            return False
    
    return True

def check_api_key():
    """Vérifie la clé API Groq"""
    
    print("\n🔑 Vérification de la clé API")
    print("=" * 40)
    
    try:
        import streamlit as st
        from pathlib import Path
        
        # Lecture du fichier secrets.toml
        secrets_file = Path('.streamlit/secrets.toml')
        if secrets_file.exists():
            with open(secrets_file, 'r') as f:
                content = f.read()
                if 'GROQ_API_KEY' in content and 'gsk_' in content:
                    print("✅ Clé API Groq configurée")
                    return True
                else:
                    print("❌ Clé API Groq manquante ou invalide")
                    return False
        else:
            print("❌ Fichier .streamlit/secrets.toml manquant")
            return False
            
    except Exception as e:
        print(f"❌ Erreur lors de la vérification de la clé API: {str(e)}")
        return False

def test_groq_connection():
    """Teste la connexion à l'API Groq"""
    
    print("\n🌐 Test de connexion à l'API Groq")
    print("=" * 40)
    
    try:
        import groq
        
        # Lecture de la clé API
        with open('.streamlit/secrets.toml', 'r') as f:
            content = f.read()
            lines = content.split('\n')
            api_key = None
            for line in lines:
                if 'GROQ_API_KEY' in line:
                    api_key = line.split('=')[1].strip().strip('"')
                    break
        
        if not api_key:
            print("❌ Clé API non trouvée")
            return False
        
        # Test de connexion
        client = groq.Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": "Test"}],
            max_tokens=10
        )
        
        print("✅ Connexion à l'API Groq réussie")
        return True
        
    except Exception as e:
        print(f"❌ Erreur de connexion à l'API Groq: {str(e)}")
        return False

def check_port_availability():
    """Vérifie si le port 8502 est disponible"""
    
    print("\n🔌 Vérification du port 8502")
    print("=" * 40)
    
    try:
        response = requests.get("http://localhost:8502", timeout=5)
        print("⚠️  Port 8502 déjà utilisé")
        return False
    except requests.exceptions.ConnectionError:
        print("✅ Port 8502 disponible")
        return True
    except Exception:
        print("✅ Port 8502 disponible")
        return True

def start_streamlit():
    """Démarre l'application Streamlit"""
    
    print("\n🚀 Démarrage de l'application Streamlit")
    print("=" * 40)
    
    try:
        # Démarrage de Streamlit
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8502",
            "--server.headless", "true"
        ])
        
        print("⏳ Attente du démarrage...")
        time.sleep(5)
        
        # Vérification que l'application est accessible
        try:
            response = requests.get("http://localhost:8502", timeout=10)
            if response.status_code == 200:
                print("✅ Application démarrée avec succès")
                print(f"🌐 URL: http://localhost:8502")
                return process
            else:
                print(f"❌ Erreur HTTP: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Impossible d'accéder à l'application: {str(e)}")
            return None
            
    except Exception as e:
        print(f"❌ Erreur lors du démarrage: {str(e)}")
        return None

def main():
    """Fonction principale"""
    
    print("🔧 Démarrage amélioré de l'application")
    print("=" * 60)
    
    # Vérifications préalables
    checks = [
        ("Environnement", check_environment),
        ("Dépendances", check_dependencies),
        ("Clé API", check_api_key),
        ("Connexion API", test_groq_connection),
        ("Port", check_port_availability)
    ]
    
    for check_name, check_func in checks:
        if not check_func():
            print(f"\n❌ Échec de la vérification: {check_name}")
            print("\n🔧 Solutions:")
            print("1. Vérifiez que vous êtes dans le bon répertoire")
            print("2. Activez l'environnement virtuel: source venv/bin/activate")
            print("3. Installez les dépendances: pip install -r requirements.txt")
            print("4. Configurez votre clé API dans .streamlit/secrets.toml")
            print("5. Vérifiez votre connexion internet")
            return False
    
    print("\n✅ Toutes les vérifications sont passées")
    
    # Démarrage de l'application
    process = start_streamlit()
    
    if process:
        print("\n🎉 Application prête !")
        print("\n📋 Instructions:")
        print("1. Ouvrez http://localhost:8502 dans votre navigateur")
        print("2. Naviguez vers la page 'Assistant IA'")
        print("3. Testez l'assistant avec un message simple")
        print("4. Pour arrêter l'application, appuyez sur Ctrl+C")
        
        try:
            # Attendre que l'utilisateur arrête l'application
            process.wait()
        except KeyboardInterrupt:
            print("\n🛑 Arrêt de l'application...")
            process.terminate()
            process.wait()
            print("✅ Application arrêtée")
    else:
        print("\n❌ Échec du démarrage de l'application")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 