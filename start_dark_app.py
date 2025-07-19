#!/usr/bin/env python3
"""
Script de démarrage pour l'application avec thème sombre forcé
"""

import os
import sys
import subprocess
import time

def check_dark_theme_config():
    """Vérifie que la configuration du thème sombre est correcte"""
    print("🔍 Vérification de la configuration du thème sombre...")
    
    try:
        # Test d'importation
        from config import force_dark_theme
        from config.styles import apply_styles
        from config.settings import configure_page
        print("✅ Modules de thème sombre importés avec succès")
        
        # Test de la fonction force_dark_theme
        force_dark_theme()
        print("✅ Fonction force_dark_theme exécutée avec succès")
        
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la vérification : {e}")
        return False

def start_application():
    """Démarre l'application avec le thème sombre forcé"""
    print("🚀 Démarrage de l'application avec thème sombre forcé...")
    
    try:
        # Démarrage de l'application
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors du démarrage : {e}")
        return False
    except KeyboardInterrupt:
        print("\n🛑 Application arrêtée par l'utilisateur")
        return True

def main():
    """Fonction principale"""
    print("🌙 Dashboard Voyage Japon - Thème Sombre Forcé")
    print("=" * 50)
    
    # Vérification de la configuration
    if not check_dark_theme_config():
        print("❌ Configuration du thème sombre incorrecte")
        print("💡 Vérifiez les fichiers de configuration")
        return 1
    
    print("✅ Configuration du thème sombre validée")
    print("🌙 L'application utilisera UNIQUEMENT le thème sombre")
    print("💡 Peu importe les paramètres du système")
    print()
    
    # Démarrage de l'application
    return start_application()

if __name__ == "__main__":
    sys.exit(main()) 