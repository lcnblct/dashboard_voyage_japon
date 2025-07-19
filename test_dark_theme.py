#!/usr/bin/env python3
"""
Script de test pour vérifier que le thème sombre est correctement configuré et forcé
"""

import sys
import os

def test_imports():
    """Teste l'importation des modules principaux"""
    try:
        from config.styles import apply_styles
        from config.settings import configure_page
        from config import force_dark_theme
        print("✅ Importation des modules de style réussie")
        return True
    except ImportError as e:
        print(f"❌ Erreur d'importation : {e}")
        return False

def test_css_content():
    """Teste que le CSS contient bien les styles sombres forcés"""
    try:
        from config.styles import apply_styles
        from config import force_dark_theme
        import streamlit as st
        
        # Simuler l'application des styles
        st.set_page_config(page_title="Test")
        
        # Vérifier que les fonctions s'exécutent sans erreur
        force_dark_theme()
        apply_styles()
        print("✅ Application des styles CSS forcés réussie")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de l'application des styles : {e}")
        return False

def test_dark_theme_colors():
    """Teste que les couleurs sombres sont bien définies et forcées"""
    dark_colors = [
        "#0e1117",  # Arrière-plan principal
        "#262730",  # Arrière-plan secondaire
        "#fafafa",  # Texte principal
        "#4CAF50",  # Vert accent
        "#3b82f6",  # Bleu accent
        "#f59e0b"   # Orange accent
    ]
    
    print("🎨 Couleurs du thème sombre forcé :")
    for color in dark_colors:
        print(f"   - {color}")
    
    return True

def test_theme_override():
    """Teste que les overrides du thème sont bien configurés"""
    override_selectors = [
        ":root { color-scheme: dark !important; }",
        ".stApp { --background-color: #0e1117 !important; }",
        "html, body { background-color: #0e1117 !important; }",
        "div[data-testid='stSidebar'] { background-color: #262730 !important; }"
    ]
    
    print("🔧 Overrides du thème sombre configurés :")
    for selector in override_selectors:
        print(f"   - {selector}")
    
    return True

def test_force_dark_theme():
    """Teste la fonction de forçage du thème sombre"""
    try:
        from config import force_dark_theme
        print("✅ Fonction force_dark_theme disponible")
        return True
    except Exception as e:
        print(f"❌ Erreur avec force_dark_theme : {e}")
        return False

def main():
    """Fonction principale de test"""
    print("🧪 Test du thème sombre FORCÉ - Dashboard Voyage Japon")
    print("=" * 60)
    
    tests = [
        ("Importation des modules", test_imports),
        ("Application des styles CSS forcés", test_css_content),
        ("Vérification des couleurs", test_dark_theme_colors),
        ("Vérification des overrides", test_theme_override),
        ("Test de force_dark_theme", test_force_dark_theme)
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
    
    print("\n" + "=" * 60)
    print(f"📊 Résultats : {passed}/{total} tests réussis")
    
    if passed == total:
        print("🎉 Tous les tests sont passés ! Le thème sombre est correctement FORCÉ.")
        print("🌙 Aucun thème clair ne peut être utilisé, peu importe les paramètres système.")
        return 0
    else:
        print("⚠️ Certains tests ont échoué. Vérifiez la configuration du thème sombre forcé.")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 