# 🗾 Dashboard Voyage Japon

Un tableau de bord interactif et complet pour organiser et suivre votre voyage au Japon. Cette application Streamlit vous permet de gérer votre itinéraire, votre budget, votre checklist de préparation et bien plus encore !

## ✨ Fonctionnalités

### 🏠 **Page d'accueil**
- Compteur de jours avant le départ
- Vue d'ensemble du budget total
- Prochaine tâche à accomplir dans la checklist
- Statut global de préparation

### 🗺️ **Gestion de l'itinéraire**
- Ajout d'étapes avec date, ville, activités et hébergement
- Affichage chronologique de l'itinéraire
- Suppression d'étapes
- Définition automatique de la date de départ

### 💴 **Suivi de budget**
- Enregistrement des dépenses par catégorie
- Visualisation des dépenses totales
- Graphiques par catégorie (Transport, Hébergement, Nourriture, etc.)
- Calcul automatique du total

### ✅ **Checklist de préparation**
- Documents essentiels (passeport, billets, JR Pass, permis)
- Bagages (adaptateur, vêtements, trousse de secours)
- Administratif (banque, assurance)
- Sauvegarde automatique des progrès

### 🗾 **Carte interactive**
- Visualisation de l'itinéraire sur une carte du Japon
- Marqueurs pour chaque ville visitée
- Popups avec détails des activités par date
- Support pour les principales villes japonaises

### 🔗 **Ressources utiles**
- Convertisseur EUR → JPY
- Phrases japonaises essentielles
- Liens vers sites officiels (ambassade, JR Pass, etc.)

## 🚀 Installation et démarrage

### Prérequis
- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/votre-username/dashboard_voyage_japon.git
   cd dashboard_voyage_japon
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration du mot de passe**
   
   Créez un fichier `.streamlit/secrets.toml` à la racine du projet :
   ```toml
   PASSWORD = "votre_mot_de_passe_ici"
   ```

4. **Lancer l'application**
   ```bash
   streamlit run app.py
   ```

5. **Accéder à l'application**
   
   Ouvrez votre navigateur et allez sur `http://localhost:8501`

## 📁 Structure du projet

```
dashboard_voyage_japon/
├── app.py              # Application principale Streamlit
├── data.json           # Données persistantes (créé automatiquement)
├── requirements.txt    # Dépendances Python
├── README.md          # Ce fichier
└── .streamlit/
    └── secrets.toml   # Configuration du mot de passe
```

## 🔧 Configuration

### Variables d'environnement

L'application utilise Streamlit Secrets pour la sécurité. Créez le fichier `.streamlit/secrets.toml` :

```toml
PASSWORD = "votre_mot_de_passe_secret"
```

### Personnalisation

Vous pouvez facilement personnaliser l'application en modifiant :

- **Villes supportées** : Ajoutez des coordonnées dans la fonction `get_city_coords()`
- **Taux de change** : Modifiez la valeur dans `display_resources()`
- **Checklist** : Ajoutez ou supprimez des éléments dans `load_data()`

## 💾 Persistance des données

Toutes les données sont automatiquement sauvegardées dans le fichier `data.json` :
- Itinéraire complet
- Dépenses et budget
- État de la checklist
- Date de départ

## 🛡️ Sécurité

- **Protection par mot de passe** : L'application nécessite un mot de passe pour y accéder
- **Données locales** : Toutes les données restent sur votre machine
- **Aucune connexion externe** : L'application fonctionne entièrement en local

## 🎯 Utilisation

### Première utilisation
1. Lancez l'application avec `streamlit run app.py`
2. Entrez le mot de passe configuré
3. Commencez par ajouter votre date de départ dans la section "Itinéraire"
4. Remplissez progressivement votre checklist de préparation

### Gestion quotidienne
- **Itinéraire** : Ajoutez vos étapes au fur et à mesure de votre planification
- **Budget** : Enregistrez vos dépenses pour suivre vos finances
- **Checklist** : Cochez les éléments au fur et à mesure de votre préparation
- **Carte** : Visualisez votre parcours sur une carte interactive

## 🔧 Dépendances

- **streamlit** : Interface utilisateur web
- **pandas** : Manipulation et analyse des données
- **folium** : Création de cartes interactives
- **streamlit-folium** : Intégration de Folium dans Streamlit

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🆘 Support

Si vous rencontrez des problèmes ou avez des questions :

1. Vérifiez que toutes les dépendances sont installées
2. Assurez-vous que le fichier `secrets.toml` est correctement configuré
3. Consultez les logs de Streamlit pour les erreurs
4. Ouvrez une issue sur GitHub

## 🎉 Remerciements

- [Streamlit](https://streamlit.io/) pour l'interface utilisateur
- [Folium](https://python-visualization.github.io/folium/) pour les cartes interactives
- [Pandas](https://pandas.pydata.org/) pour la manipulation des données

---

**Bon voyage au Japon ! 🇯🇵✨**
