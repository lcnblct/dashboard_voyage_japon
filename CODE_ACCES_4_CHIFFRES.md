# 🔐 Système d'Authentification par Code à 4 Chiffres

## 📋 Vue d'ensemble

L'application utilise maintenant un **système d'authentification par code à 4 chiffres** au lieu d'un mot de passe traditionnel. Cette approche offre une expérience utilisateur plus simple et plus rapide.

## ✨ Avantages du Code à 4 Chiffres

### 🚀 **Simplicité d'utilisation**
- Saisie rapide (4 chiffres seulement)
- Pas de caractères spéciaux à retenir
- Interface claire et intuitive

### 🔒 **Sécurité adaptée**
- Protection suffisante pour une application personnelle
- Code facile à partager avec des proches
- Moins de risque d'oubli

### 📱 **Expérience mobile optimisée**
- Saisie rapide sur mobile
- Interface adaptée aux petits écrans
- Validation en temps réel

## ⚙️ Configuration

### 1. **Fichier de configuration local**
Créez ou modifiez le fichier `.streamlit/secrets.toml` :

```toml
ACCESS_CODE = "1234"
GROQ_API_KEY = "votre_clé_api_groq_ici"
```

### 2. **Déploiement sur Streamlit Cloud**
Dans les paramètres de votre application sur Streamlit Cloud :

```toml
ACCESS_CODE = "1234"
GROQ_API_KEY = "votre_clé_api_groq"
```

## 🔧 Fonctionnalités

### ✅ **Validation en temps réel**
- Vérification du format (exactement 4 chiffres)
- Messages d'erreur clairs
- Feedback immédiat

### 🔄 **Réinitialisation sécurisée**
- Code requis pour le reset de l'application
- Confirmation obligatoire
- Protection contre les suppressions accidentelles

### 🎨 **Interface moderne**
- Design cohérent avec le thème sombre
- Messages d'aide contextuels
- Animations et transitions fluides

## 📝 Utilisation

### **Première connexion**
1. Lancez l'application
2. Entrez votre code à 4 chiffres
3. L'application se souvient de votre authentification

### **Reset de l'application**
1. Allez dans "Réglages" → "Reset"
2. Entrez votre code à 4 chiffres
3. Confirmez la suppression
4. L'application se remet à zéro

## 🔒 Recommandations de sécurité

### **Choix du code**
- Évitez les codes trop évidents (1234, 0000, 1111)
- Utilisez un code personnel significatif
- Changez le code si nécessaire

### **Partage du code**
- Partagez uniquement avec des personnes de confiance
- Le code donne accès à toutes vos données de voyage
- Considérez changer le code après partage

## 🛠️ Migration depuis l'ancien système

### **Pour les utilisateurs existants**
1. Mettez à jour votre fichier `.streamlit/secrets.toml`
2. Remplacez `PASSWORD = "ancien_mot_de_passe"` par `ACCESS_CODE = "1234"`
3. Redémarrez l'application
4. Utilisez le nouveau code à 4 chiffres

### **Pour les nouveaux utilisateurs**
1. Configurez `ACCESS_CODE = "1234"` dans vos secrets
2. Lancez l'application
3. Entrez le code 1234 pour accéder

## 🔍 Dépannage

### **Code non reconnu**
- Vérifiez que le code contient exactement 4 chiffres
- Assurez-vous que `ACCESS_CODE` est correctement configuré
- Redémarrez l'application si nécessaire

### **Problèmes de configuration**
- Vérifiez le fichier `.streamlit/secrets.toml`
- Assurez-vous que la syntaxe TOML est correcte
- Consultez les logs de l'application

## 📚 Code par défaut

**Code d'accès par défaut :** `1234`

⚠️ **Important :** Changez ce code pour un code personnel dans votre configuration !

---

*Ce système d'authentification offre un bon équilibre entre simplicité d'utilisation et sécurité pour une application de planification de voyage personnelle.* 