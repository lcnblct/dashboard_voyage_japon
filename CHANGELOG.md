# Changelog - Dashboard Voyage Japon

## [1.1.0] - 2024-12-19

### 🎨 Ajouté
- **Thème sombre forcé** : L'application utilise maintenant un thème sombre uniforme, peu importe les préférences système
- **Styles CSS améliorés** : Suppression des media queries adaptatives pour une expérience visuelle cohérente
- **Configuration globale** : Variables CSS personnalisées pour forcer le mode sombre
- **Script de lancement** : `run.sh` pour faciliter l'installation et le lancement
- **Environnement virtuel** : Configuration automatique avec `venv/`
- **Fichier .gitignore** : Exclusion des fichiers temporaires et de l'environnement virtuel

### 🔧 Modifié
- **config/styles.py** : Refactorisation complète pour supprimer les media queries `@media (prefers-color-scheme)`
- **config/settings.py** : Ajout de la configuration CSS globale pour forcer le thème sombre
- **README.md** : Documentation mise à jour avec les nouvelles instructions d'installation
- **requirements.txt** : Dépendances vérifiées et compatibles

### 🗑️ Supprimé
- **app_old.py** : Ancien fichier avec la logique adaptative obsolète
- **Media queries adaptatives** : Suppression de la logique `@media (prefers-color-scheme: light)`

### 🎯 Couleurs du Thème Sombre
- **Arrière-plan principal** : `#0e1117`
- **Arrière-plan secondaire** : `#262730`
- **Texte principal** : `#fafafa`
- **Accents** : `#4CAF50` (vert), `#3b82f6` (bleu), `#f59e0b` (orange)

### 🚀 Installation
```bash
# Installation rapide
./run.sh

# Ou installation manuelle
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

---

## [1.0.0] - Version Initiale

### ✨ Fonctionnalités
- Dashboard complet pour la préparation de voyage au Japon
- Profil de voyage personnalisé avec 50+ questions
- Gestion d'itinéraire avec carte interactive
- Suivi de budget et checklist de préparation
- Thème adaptatif (clair/sombre selon les préférences système) 