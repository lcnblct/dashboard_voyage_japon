#!/usr/bin/env python3
"""
Script de test pour vérifier la fonctionnalité de l'application refactorisée
"""

import sys
import os

def test_imports():
    """Teste tous les imports de l'application"""
    print("🔍 Test des imports...")
    
    try:
        # Test des modules de configuration
        from config.settings import configure_page, NAVIGATION_MENU
        print("✅ config.settings - OK")
        
        from config.styles import apply_styles
        print("✅ config.styles - OK")
        
        # Test des modules de données
        from data.models import get_default_checklist, get_default_travel_profile
        print("✅ data.models - OK")
        
        from data.storage import load_data, save_data, sync_state
        print("✅ data.storage - OK")
        
        from data.cities import get_city_coords, get_supported_cities
        print("✅ data.cities - OK")
        
        # Test des utilitaires
        from utils.helpers import check_password, format_currency, calculate_days_until_departure
        print("✅ utils.helpers - OK")
        
        # Test des pages
        from pages.home import display_home
        print("✅ pages.home - OK")
        
        from pages.travel_profile import display_travel_profile
        print("✅ pages.travel_profile - OK")
        
        from pages.itinerary import display_itinerary
        print("✅ pages.itinerary - OK")
        
        from pages.calendar import display_calendar
        print("✅ pages.calendar - OK")
        
        from pages.flight import display_flight
        print("✅ pages.flight - OK")
        
        from pages.budget import display_budget
        print("✅ pages.budget - OK")
        
        from pages.checklist import display_checklist
        print("✅ pages.checklist - OK")
        
        from pages.map import display_map
        print("✅ pages.map - OK")
        
        from pages.resources import display_resources
        print("✅ pages.resources - OK")
        
        from pages.settings import display_settings
        print("✅ pages.settings - OK")
        
        # Test de l'application complète
        import app
        print("✅ Application complète - OK")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur d'import: {e}")
        return False

def test_data_functions():
    """Teste les fonctions de données"""
    print("\n🔍 Test des fonctions de données...")
    
    try:
        from data.models import get_default_checklist, get_default_travel_profile
        from data.cities import get_city_coords, get_supported_cities
        from utils.helpers import format_currency, calculate_days_until_departure
        
        # Test des modèles par défaut
        checklist = get_default_checklist()
        assert isinstance(checklist, dict)
        assert len(checklist) > 0
        print("✅ Modèles par défaut - OK")
        
        # Test des coordonnées des villes
        coords = get_city_coords("Tokyo")
        assert coords == (35.6895, 139.6917)
        print("✅ Coordonnées des villes - OK")
        
        # Test des villes supportées
        cities = get_supported_cities()
        assert "Tokyo" in cities
        assert "Kyoto" in cities
        print("✅ Villes supportées - OK")
        
        # Test des fonctions utilitaires
        formatted = format_currency(123.45)
        assert formatted == "123.45 €"
        print("✅ Fonctions utilitaires - OK")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur de données: {e}")
        return False

def test_file_structure():
    """Teste la structure des fichiers"""
    print("\n🔍 Test de la structure des fichiers...")
    
    required_files = [
        "app.py",
        "config/settings.py",
        "config/styles.py",
        "data/models.py",
        "data/storage.py",
        "data/cities.py",
        "utils/helpers.py",
        "pages/home.py",
        "pages/travel_profile.py",
        "pages/itinerary.py",
        "pages/calendar.py",
        "pages/flight.py",
        "pages/budget.py",
        "pages/checklist.py",
        "pages/map.py",
        "pages/resources.py",
        "pages/settings.py",
        "data.json"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
        else:
            print(f"✅ {file_path} - OK")
    
    if missing_files:
        print(f"❌ Fichiers manquants: {missing_files}")
        return False
    
    return True

def test_data_json():
    """Teste le fichier de données JSON"""
    print("\n🔍 Test du fichier data.json...")
    
    try:
        import json
        with open("data.json", "r") as f:
            data = json.load(f)
        
        # Vérifie la structure de base
        assert "checklist" in data
        assert isinstance(data["checklist"], dict)
        print("✅ Structure JSON - OK")
        
        # Vérifie que la checklist contient des éléments
        assert len(data["checklist"]) > 0
        print("✅ Contenu checklist - OK")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur JSON: {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🚀 Test de fonctionnalité de l'application refactorisée")
    print("=" * 60)
    
    tests = [
        test_file_structure,
        test_data_json,
        test_imports,
        test_data_functions
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 60)
    print(f"📊 Résultats: {passed}/{total} tests réussis")
    
    if passed == total:
        print("🎉 Tous les tests sont passés ! L'application est fonctionnelle.")
        return 0
    else:
        print("❌ Certains tests ont échoué.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 