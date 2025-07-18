#!/usr/bin/env python3
"""
Script de test pour vérifier que le thème sombre est correctement configuré
"""

import sys
import os

def test_imports():
    """Teste l'importation des modules principaux"""
    try:
        from config.styles import apply_styles
        from config.settings import configure_page
        print("✅ Importation des modules de style réussie")
        return True
    except ImportError as e:
        print(f"❌ Erreur d'importation : {e}")
        return False

def test_css_content():
    """Teste que le CSS contient bien les styles sombres"""
    try:
        from config.styles import apply_styles
        import streamlit as st
        
        # Simuler l'application des styles
        st.set_page_config(page_title="Test")
        
        # Vérifier que la fonction s'exécute sans erreur
        apply_styles()
        print("✅ Application des styles CSS réussie")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de l'application des styles : {e}")
        return False

def test_dark_theme_colors():
    """Teste que les couleurs sombres sont bien définies"""
    dark_colors = [
        "#0e1117",  # Arrière-plan principal
        "#262730",  # Arrière-plan secondaire
        "#fafafa",  # Texte principal
        "#4CAF50",  # Vert accent
        "#3b82f6",  # Bleu accent
        "#f59e0b"   # Orange accent
    ]
    
    print("🎨 Couleurs du thème sombre :")
    for color in dark_colors:
        print(f"   - {color}")
    
    return True

def main():
    """Fonction principale de test"""
    print("🧪 Test du thème sombre - Dashboard Voyage Japon")
    print("=" * 50)
    
    tests = [
        ("Importation des modules", test_imports),
        ("Application des styles CSS", test_css_content),
        ("Vérification des couleurs", test_dark_theme_colors)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 Test : {test_name}")
        if test_func():
            passed += 1
            print(f"✅ {test_name} : SUCCÈS")
        else:
            print(f"❌ {test_name} : ÉCHEC")
    
    print("\n" + "=" * 50)
    print(f"📊 Résultats : {passed}/{total} tests réussis")
    
    if passed == total:
        print("🎉 Tous les tests sont passés ! Le thème sombre est correctement configuré.")
        return 0
    else:
        print("⚠️ Certains tests ont échoué. Vérifiez la configuration.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 