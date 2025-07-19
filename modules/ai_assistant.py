# Page de l'assistant IA avec Groq
import streamlit as st
import groq
import json
from datetime import datetime
from data.models import get_default_travel_profile
from data.storage import sync_state

# Configuration de l'API Groq depuis les secrets Streamlit
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", "")

def display_ai_assistant():
    """Affiche la page de l'assistant IA moderne et lisible"""
    
    # Vérification de la clé API
    if not GROQ_API_KEY:
        st.error("❌ Clé API Groq non configurée. Veuillez ajouter GROQ_API_KEY dans .streamlit/secrets.toml")
        st.stop()
    
    # Initialisation de l'état
    if 'ai_messages' not in st.session_state:
        st.session_state.ai_messages = []
        st.session_state.ai_client = None
    
    data = st.session_state.data
    profile = data.get("travel_profile", get_default_travel_profile())
    
    # En-tête moderne avec gradient
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="margin: 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
            🤖 Assistant IA Voyage Japon
        </h1>
        <p style="color: #94a3b8; font-size: 1.1rem; margin-top: 0.5rem;">
            Votre compagnon intelligent pour organiser votre voyage
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Informations du profil en métriques modernes
    st.markdown("### 📊 Contexte de votre voyage")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "👥 Voyageurs", 
            profile.get('travelers', 'Non spécifié'),
            help="Nombre de personnes qui voyagent"
        )
    
    with col2:
        st.metric(
            "💰 Budget/jour", 
            f"{profile.get('budget_per_day', 0)}€",
            help="Budget quotidien défini dans votre profil"
        )
    
    with col3:
        st.metric(
            "⚡ Rythme", 
            f"{profile.get('travel_rhythm', 3)}/5",
            help="Intensité de votre rythme de voyage"
        )
    
    with col4:
        st.metric(
            "🎯 Priorité", 
            profile.get('priority_1', 'Non définie')[:15] + "..." if len(profile.get('priority_1', '')) > 15 else profile.get('priority_1', 'Non définie'),
            help="Votre priorité principale pour ce voyage"
        )
    
    # Interface de chat moderne
    st.markdown("### 💬 Chat avec l'Assistant IA")
    
    # Zone de saisie moderne
    user_input = st.text_area(
        "Posez votre question :",
        placeholder="Ex: Peux-tu me suggérer un itinéraire pour 3 jours à Tokyo ? Ou: Quels sont les meilleurs restaurants de ramen à Kyoto ?",
        height=120,
        key="user_input"
    )
    
    # Boutons d'action avec style moderne
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🚀 Envoyer", type="primary", use_container_width=True):
            if user_input.strip():
                send_message_to_ai(user_input, profile)
                st.rerun()
    
    with col2:
        if st.button("🗑️ Effacer l'historique", use_container_width=True):
            st.session_state.ai_messages = []
            st.rerun()
    
    with col3:
        if st.button("📋 Exporter", use_container_width=True):
            export_conversation()
    
    # Affichage de l'historique des messages
    display_chat_history()
    
    # Suggestions rapides modernes
    display_quick_suggestions(profile)

def send_message_to_ai(user_message, profile):
    """Envoie un message à l'IA et récupère la réponse"""
    try:
        # Initialisation du client Groq
        if st.session_state.ai_client is None:
            st.session_state.ai_client = groq.Groq(api_key=GROQ_API_KEY)
        
        # Ajout du message utilisateur à l'historique
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.ai_messages.append({
            "role": "user",
            "content": user_message,
            "timestamp": timestamp
        })
        
        # Construction du contexte avec le profil
        context = build_ai_context(profile)
        
        # Préparation des messages pour l'IA
        messages = [
            {
                "role": "system",
                "content": context
            }
        ]
        
        # Ajout de l'historique récent (derniers 10 messages)
        recent_messages = st.session_state.ai_messages[-10:]
        for msg in recent_messages:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        
        # Appel à l'API Groq
        with st.spinner("🤖 L'assistant réfléchit..."):
            response = st.session_state.ai_client.chat.completions.create(
                model="llama3-70b-8192",
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
        
        # Récupération de la réponse
        ai_response = response.choices[0].message.content
        
        # Ajout de la réponse à l'historique
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.ai_messages.append({
            "role": "assistant",
            "content": ai_response,
            "timestamp": timestamp
        })
        
        st.success("✅ Réponse reçue !")
        
    except Exception as e:
        st.error(f"❌ Erreur lors de la communication avec l'IA : {str(e)}")
        
        # Ajout d'un message d'erreur à l'historique
        timestamp = datetime.now().strftime("%H:%M")
        st.session_state.ai_messages.append({
            "role": "assistant",
            "content": "Désolé, j'ai rencontré une erreur technique. Veuillez réessayer.",
            "timestamp": timestamp
        })

def build_ai_context(profile):
    """Construit le contexte pour l'IA basé sur le profil de voyage"""
    
    context = f"""Tu es un assistant IA spécialisé dans les voyages au Japon. Tu as accès au profil de voyage suivant :

INFORMATIONS DU VOYAGEUR :
- Voyageurs : {profile.get('travelers', 'Non spécifié')}
- Date d'arrivée : {profile.get('arrival_date', 'Non spécifié')}
- Budget par jour : {profile.get('budget_per_day', 0)}€
- Expérience au Japon : {profile.get('experience', 'Non spécifié')}
- Priorité principale : {profile.get('priority_1', 'Non spécifiée')}

PRÉFÉRENCES :
- Rythme de voyage : {profile.get('travel_rhythm', 3)}/5 (1=relaxé, 5=intense)
- Style d'hébergement : {profile.get('accommodation_style', 'Non spécifié')}
- Préférences culinaires : {profile.get('cuisine_preferences', 'Non spécifiées')}
- Intérêt pour les temples : {profile.get('temples_interest', 3)}/5
- Intérêt pour la pop culture : {profile.get('manga_anime', 3)}/5
- Intérêt pour les musées : {profile.get('museums_interest', 3)}/5
- Intérêt pour la nature : {profile.get('hiking_interest', 3)}/5

CONTRAINTES : {profile.get('constraints', 'Aucune contrainte spécifiée')}

INSTRUCTIONS :
1. Réponds toujours en français
2. Sois précis et pratique dans tes conseils
3. Prends en compte le budget et les préférences du voyageur
4. Suggère des activités adaptées au rythme de voyage
5. Donne des conseils concrets et actionnables
6. Si tu as des doutes, demande des précisions

Tu peux aussi rechercher des informations en temps réel si nécessaire."""
    
    return context

def display_chat_history():
    """Affiche l'historique des messages de manière moderne"""
    
    if not st.session_state.ai_messages:
        st.info("💡 Commencez par poser une question à l'assistant IA !")
        return
    
    st.markdown("### 📝 Historique de la conversation")
    
    for i, message in enumerate(st.session_state.ai_messages):
        if message["role"] == "user":
            # Message utilisateur
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(59, 130, 246, 0.05) 100%); border: 1px solid rgba(59, 130, 246, 0.2); border-left: 4px solid #3b82f6; padding: 1.25rem; border-radius: 16px; margin: 0.5rem 0;">
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <span style="font-size: 1.2rem; margin-right: 0.5rem;">👤</span>
                    <strong style="color: #f8fafc;">Vous ({message['timestamp']})</strong>
                </div>
                <div style="color: #cbd5e1;">{message['content']}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            # Message assistant
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%); border: 1px solid rgba(16, 185, 129, 0.2); border-left: 4px solid #10b981; padding: 1.25rem; border-radius: 16px; margin: 0.5rem 0;">
                <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                    <span style="font-size: 1.2rem; margin-right: 0.5rem;">🤖</span>
                    <strong style="color: #f8fafc;">Assistant ({message['timestamp']})</strong>
                </div>
                <div style="color: #cbd5e1;">{message['content']}</div>
            </div>
            """, unsafe_allow_html=True)

def display_quick_suggestions(profile):
    """Affiche des suggestions rapides modernes"""
    
    st.markdown("### 💡 Suggestions rapides")
    st.info("Cliquez sur une suggestion pour l'envoyer automatiquement.")
    
    suggestions = [
        "Peux-tu me proposer un itinéraire optimisé pour mon profil ?",
        "Quels sont les meilleurs moments pour visiter les temples de Kyoto ?",
        "Suggère-moi des restaurants authentiques à Tokyo avec des avis récents",
        "Comment optimiser mon budget pour ce voyage ?",
        "Quelles sont les activités incontournables selon mes goûts ?",
        "Peux-tu me conseiller sur les transports au Japon ?",
        "Suggère-moi des activités en cas de pluie",
        "Quels sont les quartiers à ne pas manquer à Osaka ?",
        "Vérifie les horaires actuels du Shinkansen Tokyo-Kyoto",
        "Trouve des informations sur les festivals au Japon en mai",
        "Quels sont les prix actuels du JR Pass ?",
        "Suggère-moi des ryokan avec onsen près de Tokyo"
    ]
    
    # Affichage en grille 3x4
    cols = st.columns(3)
    for i, suggestion in enumerate(suggestions):
        with cols[i % 3]:
            if st.button(suggestion, key=f"suggestion_{i}", use_container_width=True):
                # Simulation de l'envoi du message
                st.session_state.user_input = suggestion
                send_message_to_ai(suggestion, profile)
                st.rerun()

def export_conversation():
    """Exporte la conversation en format texte"""
    if not st.session_state.ai_messages:
        st.warning("Aucune conversation à exporter.")
        return
    
    # Création du contenu d'export
    export_content = "=== Conversation avec l'Assistant IA Voyage Japon ===\n\n"
    export_content += f"Date d'export : {datetime.now().strftime('%d/%m/%Y à %H:%M')}\n\n"
    
    for message in st.session_state.ai_messages:
        role = "Vous" if message["role"] == "user" else "Assistant"
        export_content += f"[{message['timestamp']}] {role} :\n{message['content']}\n\n"
    
    # Téléchargement
    st.download_button(
        label="📥 Télécharger la conversation",
        data=export_content,
        file_name=f"conversation_ia_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
        mime="text/plain"
    )

def test_groq_connection():
    """Teste la connexion à l'API Groq"""
    try:
        client = groq.Groq(api_key=GROQ_API_KEY)
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": "Test"}],
            max_tokens=10
        )
        return True
    except Exception as e:
        st.error(f"Erreur de connexion à Groq : {str(e)}")
        return False 