#!/bin/bash

# Script de lancement pour le Dashboard Voyage Japon
echo "🚀 Lancement du Dashboard Voyage Japon..."

# Vérifier si l'environnement virtuel existe
if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv venv
fi

# Activer l'environnement virtuel
echo "🔧 Activation de l'environnement virtuel..."
source venv/bin/activate

# Installer les dépendances si nécessaire
echo "📚 Vérification des dépendances..."
pip install -r requirements.txt

# Lancer l'application
echo "🌐 Lancement de l'application Streamlit..."
echo "📍 L'application sera accessible à l'adresse : http://localhost:8501"
echo "🛑 Pour arrêter l'application, appuyez sur Ctrl+C"
echo ""

streamlit run app.py 