# 🗾 Dashboard de Voyage au Japon

Un tableau de bord interactif et personnalisé pour organiser votre voyage au Japon, avec un profil de voyage détaillé basé sur vos préférences.

## ✨ Fonctionnalités

### 📊 Tableau de Bord Principal
- **Compteur de jours** avant le départ
- **Suivi du budget** avec objectif quotidien
- **Progression de la checklist** de préparation
- **Recommandations personnalisées** basées sur votre profil

### 👥 Profil de Voyage Personnalisé
- **Questionnaire complet** avec 50+ questions sur vos préférences
- **Scores personnalisés** (1-5) pour chaque centre d'intérêt
- **Recommandations adaptées** selon votre profil
- **Sauvegarde automatique** de vos préférences

### 🗺️ Gestion de l'Itinéraire
- **Ajout d'étapes** avec dates, villes et activités
- **Carte interactive** avec marqueurs géolocalisés
- **Liste des villes japonaises** populaires
- **Suppression et modification** des étapes

### 💰 Suivi de Budget
- **Ajout de dépenses** par catégorie
- **Visualisation graphique** des dépenses
- **Calcul automatique** du total
- **Comparaison** avec le budget cible

### ✅ Checklist de Préparation
- **40+ éléments** organisés par catégories
- **Progression visuelle** avec pourcentage
- **Sauvegarde automatique** des coches
- **Migration automatique** des anciennes données

### 🗾 Carte Interactive
- **Visualisation** de votre itinéraire
- **Marqueurs** pour chaque ville visitée
- **Popups informatifs** avec détails des étapes
- **Support** de 45+ villes japonaises



## 🚀 Installation et Utilisation

### Prérequis
```bash
pip install -r requirements.txt
```

### Lancement
```bash
streamlit run app.py
```

### Configuration
1. **Mot de passe** : Configurez `st.secrets["PASSWORD"]` dans votre fichier `.streamlit/secrets.toml`
2. **Première utilisation** : Complétez votre profil de voyage dans la section "Profil de Voyage"
3. **Données** : Toutes vos informations sont sauvegardées dans `data.json`

## 📋 Structure des Données

### Profil de Voyage
Le profil contient 50+ champs organisés en catégories :
- **Informations de base** : voyageurs, dates, budget
- **Préférences géographiques** : orientation, priorités
- **Rythme et style** : intensité, planification, tolérance foule
- **Hébergement** : style, onsen, emplacement
- **Nourriture** : préférences, niveau d'aventure
- **Centres d'intérêt** : culture, pop culture, nature
- **Spécificités** : intérêts particuliers, activités à éviter

### Recommandations Personnalisées
Le système génère automatiquement des recommandations basées sur vos scores :
- **Musées** (score ≥ 4) : Musée national de Tokyo, Musée Ghibli
- **Architecture moderne** (score ≥ 4) : Tokyo Skytree, Shibuya Scramble
- **Randonnée** (score ≥ 4) : Mont Takao, Alpes japonaises
- **Jardins** (score ≥ 4) : Kenroku-en, Ryoan-ji
- **Onsen** (score ≥ 4) : Hakone, Kusatsu
- **Sumo** : Réservations pour les tournois
- **Karaoké** : Bars et salles privées



## 🎯 Profil Type : Deux Frères Urbains

Basé sur votre questionnaire, voici votre profil type :

### Points Forts
- **Musées** : Passion absolue (5/5)
- **Architecture moderne** : Intérêt maximal (5/5)
- **Randonnée** : Sportifs et motivés (5/5)
- **Cuisine aventureuse** : Prêts pour l'aventure totale (5/5)
- **Onsen** : Critère essentiel (4/5)
- **Vie nocturne** : Priorité N°1

### Itinéraire Recommandé
- **Tokyo** (5 nuits) : Découverte urbaine et vie nocturne
- **Hakone** (2 nuits) : Onsen et vue sur le Mont Fuji
- **Kyoto** (4 nuits) : Culture traditionnelle et jardins
- **Osaka** (3 nuits) : Street food et ambiance locale

### Activités Prioritaires
- **Musées** : Musée national de Tokyo, Musée Ghibli, TeamLab
- **Architecture** : Tokyo Skytree, Shibuya Scramble, Umeda Sky Building
- **Randonnées** : Mont Takao, Sentier Nakasendo, Alpes japonaises
- **Onsen** : Hakone, Kusatsu, Beppu
- **Sumo** : Réservation obligatoire pour les tournois
- **Karaoké** : Soirées entre frères

## 🔧 Personnalisation

### Ajout de Nouvelles Villes
Modifiez la fonction `get_city_coords()` dans `app.py` pour ajouter de nouvelles villes avec leurs coordonnées.

### Modification du Profil
Ajoutez de nouveaux champs dans `get_default_travel_profile()` et mettez à jour la fonction `display_travel_profile()`.



## 📱 Applications Recommandées

### Transport
- **Hyperdia** : Horaires des trains
- **Google Maps** : Navigation
- **Japan Transit Planner** : Itinéraires détaillés

### Communication
- **Google Translate** : Traduction
- **DeepL** : Traduction avancée

### Météo
- **Tenki.jp** : Météo japonaise
- **Weather.com** : Prévisions internationales

## 💡 Conseils d'Utilisation

1. **Complétez d'abord votre profil** pour recevoir des recommandations personnalisées
2. **Sauvegardez régulièrement** vos données via l'export JSON
3. **Utilisez la carte interactive** pour visualiser votre itinéraire
4. **Générez le guide LaTeX** une fois votre profil finalisé
5. **Consultez les recommandations** sur la page d'accueil

## 🤝 Contribution

Ce projet est conçu pour être facilement personnalisable. N'hésitez pas à :
- Ajouter de nouvelles fonctionnalités
- Améliorer les recommandations
- Étendre la liste des villes
- Personnaliser le guide LaTeX

## 📄 Licence

Ce projet est open source et disponible sous licence MIT.

---

**Bon voyage au Japon ! 🇯🇵**

*Votre assistant IA personnel pour un voyage parfaitement personnalisé.*
