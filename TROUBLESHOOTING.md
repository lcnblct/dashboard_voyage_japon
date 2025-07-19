# 🔧 Guide de Dépannage - Assistant IA

## Problème : L'assistant IA ne fonctionne pas

### 🔍 Diagnostic Rapide

1. **Vérifiez que l'application est démarrée :**
   ```bash
   source venv/bin/activate
   python check_streamlit_status.py
   ```

2. **Testez l'API Groq :**
   ```bash
   source venv/bin/activate
   python test_groq_debug.py
   ```

3. **Démarrage avec vérifications complètes :**
   ```bash
   source venv/bin/activate
   python start_app_with_checks.py
   ```

### 🚨 Problèmes Courants et Solutions

#### 1. ❌ "Clé API Groq non configurée"

**Symptômes :**
- Message d'erreur : "Clé API Groq non configurée"
- L'assistant ne répond pas

**Solutions :**
1. Vérifiez le fichier `.streamlit/secrets.toml` :
   ```toml
   GROQ_API_KEY = "gsk_votre_clé_api_ici"
   ```

2. Obtenez une clé API gratuite sur [console.groq.com](https://console.groq.com/)

3. Testez votre clé :
   ```bash
   python test_groq_debug.py
   ```

#### 2. ❌ "Erreur de connexion à l'API Groq"

**Symptômes :**
- Messages d'erreur de connexion
- Timeout lors des requêtes

**Solutions :**
1. Vérifiez votre connexion internet
2. Vérifiez votre quota d'utilisation sur [console.groq.com](https://console.groq.com/)
3. Essayez un modèle différent dans le code
4. Vérifiez que la clé API est valide

#### 3. ❌ "Application non accessible"

**Symptômes :**
- Impossible d'accéder à http://localhost:8502
- Erreur de connexion

**Solutions :**
1. Redémarrez l'application :
   ```bash
   streamlit run app.py
   ```

2. Vérifiez que le port 8502 n'est pas utilisé :
   ```bash
   lsof -i :8502
   ```

3. Utilisez un port différent :
   ```bash
   streamlit run app.py --server.port 8503
   ```

#### 4. ❌ "Module groq non trouvé"

**Symptômes :**
- ImportError: No module named 'groq'
- Erreur lors du démarrage

**Solutions :**
1. Activez l'environnement virtuel :
   ```bash
   source venv/bin/activate
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Installez groq manuellement :
   ```bash
   pip install groq
   ```

#### 5. ❌ "L'assistant ne répond pas"

**Symptômes :**
- L'interface fonctionne mais pas de réponse
- Spinner infini

**Solutions :**
1. Vérifiez les logs dans le terminal
2. Testez avec un message simple
3. Vérifiez votre quota d'utilisation Groq
4. Essayez de rafraîchir la page

### 🔧 Scripts de Diagnostic

#### Test complet de l'environnement :
```bash
python start_app_with_checks.py
```

#### Test de l'API Groq :
```bash
python test_groq_debug.py
```

#### Test de l'application :
```bash
python test_ai_in_app.py
```

#### Vérification du statut :
```bash
python check_streamlit_status.py
```

### 📋 Checklist de Dépannage

- [ ] Environnement virtuel activé
- [ ] Dépendances installées (`pip install -r requirements.txt`)
- [ ] Clé API Groq configurée dans `.streamlit/secrets.toml`
- [ ] Clé API valide et active
- [ ] Connexion internet fonctionnelle
- [ ] Application Streamlit démarrée
- [ ] Port 8502 disponible
- [ ] Quota d'utilisation Groq suffisant

### 🆘 Support

Si aucun de ces solutions ne fonctionne :

1. **Vérifiez les logs détaillés :**
   ```bash
   streamlit run app.py --logger.level debug
   ```

2. **Testez avec un message simple :**
   - "Bonjour"
   - "Test"

3. **Vérifiez la console du navigateur :**
   - F12 → Console
   - Recherchez les erreurs JavaScript

4. **Redémarrez complètement :**
   ```bash
   # Arrêtez l'application (Ctrl+C)
   # Redémarrez le terminal
   source venv/bin/activate
   python start_app_with_checks.py
   ```

### 📞 Contact

Si le problème persiste, vérifiez :
- Les logs de l'application
- La console du navigateur
- Les messages d'erreur exacts

### 🔄 Mise à Jour

Pour mettre à jour l'application :
```bash
git pull
pip install -r requirements.txt --upgrade
```

### 📝 Logs Utiles

**Logs Streamlit :**
- Dans le terminal où vous lancez `streamlit run app.py`

**Logs API Groq :**
- Vérifiez votre utilisation sur [console.groq.com](https://console.groq.com/)

**Logs Navigateur :**
- F12 → Console → Erreurs 