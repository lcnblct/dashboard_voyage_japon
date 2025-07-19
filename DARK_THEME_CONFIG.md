# Configuration du Thème Sombre Forcé

## Vue d'ensemble

Cette application utilise un thème sombre **forcé** qui ne peut pas être modifié par les paramètres du système. Peu importe les préférences de thème de l'utilisateur ou du système d'exploitation, l'application restera toujours en mode sombre.

## Implémentation

### 1. Configuration principale (`config/settings.py`)

La fonction `configure_page()` applique un CSS global qui force le thème sombre :

```css
/* Configuration globale pour forcer le mode sombre partout */
:root {
    --background-color: #0e1117 !important;
    --text-color: #fafafa !important;
    --secondary-background-color: #262730 !important;
}

/* Override complet des variables CSS de Streamlit */
.stApp {
    --background-color: #0e1117 !important;
    --text-color: #fafafa !important;
    --secondary-background-color: #262730 !important;
}
```

### 2. Styles détaillés (`config/styles.py`)

Le fichier `apply_styles()` contient des overrides spécifiques pour tous les éléments :

- **Sélecteurs globaux** : `html`, `body`, `.stApp`
- **Widgets Streamlit** : inputs, boutons, onglets, etc.
- **Éléments de navigation** : sidebar, header
- **Composants personnalisés** : métriques, cartes, alertes

### 3. Forçage global (`config/__init__.py`)

La fonction `force_dark_theme()` applique un override ultime :

```python
def force_dark_theme():
    """Force le thème sombre de manière globale"""
    st.markdown("""
    <style>
        /* FORÇAGE GLOBAL DU THÈME SOMBRE */
        :root {
            color-scheme: dark !important;
        }
        /* ... autres overrides ... */
    </style>
    """, unsafe_allow_html=True)
```

### 4. Application principale (`app.py`)

L'application appelle les trois niveaux de configuration :

```python
# Configuration de la page
configure_page()

# Forçage global du thème sombre
force_dark_theme()

# Application des styles
apply_styles()
```

## Couleurs utilisées

| Élément | Couleur | Description |
|---------|---------|-------------|
| Arrière-plan principal | `#0e1117` | Fond sombre principal |
| Arrière-plan secondaire | `#262730` | Fond des cartes et sidebar |
| Texte principal | `#fafafa` | Texte blanc |
| Texte secondaire | `#cbd5e1` | Texte gris clair |
| Bordure | `#475569` | Bordures grises |
| Accent primaire | `#6366f1` | Bleu/violet |
| Accent secondaire | `#10b981` | Vert |

## Overrides spécifiques

### Éléments de base
```css
html, body, .stApp, .stApp > div, .stApp > div > div {
    background-color: #0e1117 !important;
    color: #fafafa !important;
}
```

### Sidebar
```css
div[data-testid="stSidebar"] {
    background-color: #262730 !important;
}
```

### Widgets
```css
.stTextInput > div > div > input,
.stSelectbox > div > div > div,
.stNumberInput > div > div > input {
    background-color: #262730 !important;
    color: #fafafa !important;
    border-color: #4a5568 !important;
}
```

### Navigation
```css
.css-1d391kg, .css-1v0mbdj, .css-1lcbmhc {
    background-color: #262730 !important;
}
```

## Test de la configuration

Le script `test_dark_theme.py` vérifie que :

1. ✅ Tous les modules s'importent correctement
2. ✅ Les styles CSS s'appliquent sans erreur
3. ✅ Les couleurs sombres sont définies
4. ✅ Les overrides sont configurés
5. ✅ La fonction `force_dark_theme()` est disponible

## Garanties

- **Aucun thème clair** : L'application ne peut jamais passer en mode clair
- **Indépendance système** : Les paramètres du système n'affectent pas l'apparence
- **Cohérence** : Tous les éléments utilisent le même thème sombre
- **Performance** : Les overrides CSS sont optimisés pour les performances

## Maintenance

Pour modifier le thème sombre :

1. Modifier les variables CSS dans `config/styles.py`
2. Ajuster les overrides dans `config/settings.py`
3. Tester avec `python test_dark_theme.py`
4. Vérifier l'apparence dans l'application

## Notes techniques

- Utilisation de `!important` pour forcer les overrides
- Sélecteurs CSS spécifiques pour cibler les éléments Streamlit
- Configuration en cascade (global → spécifique → ultime)
- Compatible avec toutes les versions de Streamlit 