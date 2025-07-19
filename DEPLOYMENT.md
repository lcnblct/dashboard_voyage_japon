# Déploiement sur Streamlit Cloud

## Prérequis

1. **Compte GitHub** avec votre code
2. **Compte Streamlit Cloud** (gratuit sur [share.streamlit.io](https://share.streamlit.io))

## Étapes de déploiement

### 1. Préparer le repository GitHub

Assurez-vous que votre repository contient :
- ✅ `app.py` (fichier principal)
- ✅ `requirements.txt` (dépendances)
- ✅ `.streamlit/config.toml` (configuration)
- ✅ `.gitignore` (exclut les secrets)

### 2. Configurer les secrets sur Streamlit Cloud

1. Allez sur [share.streamlit.io](https://share.streamlit.io)
2. Connectez-vous avec GitHub
3. Sélectionnez votre repository
4. Dans "Advanced settings" → "Secrets", ajoutez :

```toml
PASSWORD = "votre_mot_de_passe_securise"
GROQ_API_KEY = "votre_clé_api_groq"
```

### 3. Déployer

1. Cliquez sur "Deploy!"
2. Attendez que le déploiement se termine
3. Votre app sera disponible sur `https://votre-app.streamlit.app`

## Configuration des secrets

**IMPORTANT :** Ne jamais commiter les vrais secrets dans Git !

- ❌ `.streamlit/secrets.toml` (local seulement)
- ✅ Secrets configurés sur Streamlit Cloud

## Structure recommandée

```
votre-projet/
├── app.py                 # Application principale
├── requirements.txt       # Dépendances Python
├── .streamlit/
│   ├── config.toml       # Configuration Streamlit
│   └── secrets.example.toml  # Exemple de secrets
├── modules/              # Modules de l'application
├── config/              # Configuration
├── data/                # Données
├── utils/               # Utilitaires
└── .gitignore          # Fichiers à ignorer
```

## Dépannage

### Erreur de déploiement
- Vérifiez que `app.py` existe et fonctionne
- Vérifiez que `requirements.txt` est correct
- Vérifiez les logs de déploiement

### Erreur de secrets
- Vérifiez que les secrets sont configurés sur Streamlit Cloud
- Vérifiez que les noms correspondent à ceux dans le code

### Erreur de modules
- Vérifiez que tous les modules sont présents
- Vérifiez les imports dans `app.py`