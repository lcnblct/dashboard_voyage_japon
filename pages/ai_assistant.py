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
    """Affiche la page de l'assistant IA"""
    
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
    
    # CSS personnalisé
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    .ai-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #dbeafe;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        border-left: 4px solid #3b82f6;
    }
    .ai-message {
        background-color: #f3f4f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        border-left: 4px solid #10b981;
    }
    .suggestion-chip {
        display: inline-block;
        background-color: #e5e7eb;
        padding: 0.5rem 1rem;
        border-radius: 2rem;
        margin: 0.25rem;
        cursor: pointer;
        transition: background-color 0.2s;
    }
    .suggestion-chip:hover {
        background-color: #d1d5db;
    }
    .stButton > button {
        border-radius: 0.5rem;
        font-weight: 600;
        padding: 0.5rem 1.5rem;
    }
    .context-info {
        background-color: #fef3c7;
        border: 1px solid #f59e0b;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # En-tête principal
    st.markdown("""
    <div class="main-header">
        <h1>🤖 Assistant IA Voyage Japon</h1>
        <p style="font-size: 1.2rem; color: #6b7280;">Générez des idées personnalisées avec l'IA</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Affichage du contexte du voyage
    display_travel_context(profile)
    
    # Interface de chat
    display_chat_interface(profile)
    
    # Suggestions rapides
    display_quick_suggestions(profile)

def display_travel_context(profile):
    """Affiche le contexte du voyage actuel"""
    st.markdown("""
    <div class="context-info">
        <h4>📋 Contexte de votre voyage :</h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        **👥 Voyageurs :** {profile.get('travelers', 'Non spécifié')}
        
        **📅 Dates :** {profile.get('arrival_date', 'Non spécifié')} → {profile.get('departure_date', 'Non spécifié')}
        
        **💰 Budget :** {profile.get('budget', 'Non spécifié')}
        """)
    
    with col2:
        st.markdown(f"""
        **🎯 Priorité :** {profile.get('priority_1', 'Non spécifié')}
        
        **⚡ Rythme :** {profile.get('travel_rhythm', 'Non spécifié')}/5
        
        **🏨 Hébergement :** {profile.get('accommodation_style', 'Non spécifié')}
        """)
    
    with col3:
        st.markdown(f"""
        **🍜 Cuisine :** {profile.get('cuisine_preferences', 'Non spécifié')}
        
        **⛩️ Temples :** {profile.get('temples_interest', 'Non spécifié')}/5
        
        **📺 Manga/Anime :** {profile.get('manga_anime', 'Non spécifié')}/5
        """)

def display_chat_interface(profile):
    """Affiche l'interface de chat avec l'IA"""
    
    st.markdown("""
    <div class="ai-card">
        <h3>💬 Chat avec l'Assistant IA</h3>
        <p>Posez vos questions sur votre voyage au Japon. L'IA aura accès à votre profil pour des réponses personnalisées.</p>
        <div style="background-color: #eff6ff; border: 1px solid #dbeafe; border-radius: 0.5rem; padding: 0.75rem; margin-top: 1rem;">
            <p style="margin: 0; font-size: 0.9rem; color: #1e40af;">
                <strong>🌐 Capacités web :</strong> L'IA peut rechercher des informations en temps réel (horaires, prix, avis, événements) et exécuter des calculs pour vous aider.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Zone de saisie
    user_input = st.text_area(
        "Votre question :",
        placeholder="Ex: Peux-tu me suggérer un itinéraire pour 3 jours à Tokyo ? Ou: Quels sont les meilleurs restaurants de ramen à Kyoto ?",
        height=100,
        key="user_input"
    )
    
    # Boutons d'action
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🚀 Envoyer", type="primary"):
            if user_input.strip():
                send_message_to_ai(user_input, profile)
                st.rerun()
    
    with col2:
        if st.button("🗑️ Effacer l'historique"):
            st.session_state.ai_messages = []
            st.rerun()
    
    with col3:
        if st.button("📋 Exporter la conversation"):
            export_conversation()
    
    # Affichage de l'historique des messages
    display_chat_history()

def display_quick_suggestions(profile):
    """Affiche des suggestions rapides"""
    
    st.markdown("""
    <div class="ai-card">
        <h3>💡 Suggestions rapides</h3>
        <p>Cliquez sur une suggestion pour l'envoyer automatiquement :</p>
    </div>
    """, unsafe_allow_html=True)
    
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
    
    # Affichage des suggestions en colonnes
    cols = st.columns(3)
    for i, suggestion in enumerate(suggestions):
        with cols[i % 3]:
            if st.button(suggestion, key=f"suggestion_{i}"):
                send_message_to_ai(suggestion, profile)
                st.rerun()

def send_message_to_ai(user_message, profile):
    """Envoie un message à l'IA Groq et récupère la réponse"""
    
    try:
        # Initialisation du client Groq
        if st.session_state.ai_client is None:
            st.session_state.ai_client = groq.Groq(api_key=GROQ_API_KEY)
        
        # Ajout du message utilisateur à l'historique
        st.session_state.ai_messages.append({
            "role": "user",
            "content": user_message,
            "timestamp": datetime.now().strftime("%H:%M")
        })
        
        # Construction du contexte pour l'IA
        context = build_ai_context(profile)
        
        # Préparation des messages pour l'IA
        messages = [
            {
                "role": "system",
                "content": f"""Tu es un expert du voyage au Japon, spécialisé dans la création d'expériences personnalisées. 

Tu as accès aux informations suivantes sur le voyageur :

{context}

CAPACITÉS SPÉCIALES :
- Tu peux rechercher des informations en temps réel sur le web
- Tu peux accéder aux sites officiels japonais, guides de voyage, horaires de transport, etc.
- Tu peux exécuter du code Python pour des calculs (budget, distances, conversions)

UTILISE TES CAPACITÉS WEB POUR :
- Vérifier les horaires actuels des trains et métros
- Trouver les meilleurs restaurants avec des avis récents
- Obtenir des informations sur les événements en cours au Japon
- Vérifier les prix actuels des billets et pass
- Trouver des informations sur les festivals et événements saisonniers
- Obtenir des conseils météo en temps réel

Réponds de manière détaillée, pratique et enthousiaste. Sois créatif et propose des suggestions originales qui correspondent au profil du voyageur. 
Utilise un ton amical et encourageant. Donne des conseils concrets et des recommandations spécifiques.

Si tu utilises des informations trouvées sur le web, cite tes sources."""
            }
        ]
        
        # Ajout de l'historique récent (derniers 10 messages)
        recent_messages = st.session_state.ai_messages[-10:]
        for msg in recent_messages:
            if msg["role"] == "user":
                messages.append({"role": "user", "content": msg["content"]})
            elif msg["role"] == "assistant":
                messages.append({"role": "assistant", "content": msg["content"]})
        
        # Appel à l'API Groq avec compound-beta pour accès web
        with st.spinner("🤖 L'IA réfléchit et recherche des informations en temps réel..."):
            response = st.session_state.ai_client.chat.completions.create(
                model="compound-beta",
                messages=messages,
                temperature=0.7,
                max_tokens=2000,
                search_settings={
                    "include_domains": [
                        "japan-guide.com",
                        "japan.travel",
                        "japanrailpass.net",
                        "hyperdia.com",
                        "tabelog.com",
                        "timeout.com",
                        "lonelyplanet.com",
                        "wikitravel.org",
                        "*.jp"
                    ],
                    "exclude_domains": [
                        "*.wikipedia.org"
                    ]
                }
            )
        
        # Récupération de la réponse
        ai_response = response.choices[0].message.content
        
        # Vérification des outils utilisés
        executed_tools = getattr(response.choices[0].message, 'executed_tools', [])
        tools_used = []
        
        if executed_tools:
            for tool in executed_tools:
                if tool.get('type') == 'web_search':
                    tools_used.append("🔍 Recherche web")
                elif tool.get('type') == 'code_execution':
                    tools_used.append("💻 Exécution de code")
        
        # Ajout de la réponse à l'historique
        st.session_state.ai_messages.append({
            "role": "assistant",
            "content": ai_response,
            "timestamp": datetime.now().strftime("%H:%M"),
            "tools_used": tools_used
        })
        
    except Exception as e:
        st.error(f"Erreur lors de la communication avec l'IA : {str(e)}")
        st.session_state.ai_messages.append({
            "role": "assistant",
            "content": "Désolé, j'ai rencontré une erreur technique. Veuillez réessayer.",
            "timestamp": datetime.now().strftime("%H:%M")
        })

def build_ai_context(profile):
    """Construit le contexte pour l'IA basé sur le profil"""
    
    context = f"""
INFORMATIONS DU VOYAGE :
- Voyageurs : {profile.get('travelers', 'Non spécifié')}
- Dates : {profile.get('arrival_date', 'Non spécifié')} → {profile.get('departure_date', 'Non spécifié')}
- Budget : {profile.get('budget', 'Non spécifié')}
- Expérience : {profile.get('experience', 'Non spécifié')}
- Aéroports : {profile.get('arrival_airport', 'Non spécifié')} → {profile.get('departure_airport', 'Non spécifié')}

PRÉFÉRENCES :
- Orientation géographique : {profile.get('geographic_orientation', 'Non spécifié')}
- Priorité N°1 : {profile.get('priority_1', 'Non spécifié')}
- Rythme du voyage : {profile.get('travel_rhythm', 'Non spécifié')}/5
- Style d'hébergement : {profile.get('accommodation_style', 'Non spécifié')}
- Préférences culinaires : {profile.get('cuisine_preferences', 'Non spécifié')}
- Tolérance à la foule : {profile.get('crowd_tolerance', 'Non spécifié')}/5

CENTRES D'INTÉRÊT :
- Temples et sanctuaires : {profile.get('temples_interest', 'Non spécifié')}/5
- Manga/Anime : {profile.get('manga_anime', 'Non spécifié')}/5
- Jeux vidéo : {profile.get('gaming', 'Non spécifié')}/5
- Nature : {profile.get('nature_importance', 'Non spécifié')}/5
- Musées : {profile.get('museums_interest', 'Non spécifié')}/5
- Photographie : {profile.get('photography', 'Non spécifié')}/5

AUTRES INFORMATIONS :
- Réservations actuelles : {profile.get('current_reservations', 'Aucune')}
- Contraintes : {profile.get('constraints', 'Aucune')}
- Intérêts spécifiques : {profile.get('specific_interests', 'Aucun')}
"""
    
    return context

def display_chat_history():
    """Affiche l'historique des messages"""
    
    if not st.session_state.ai_messages:
        st.info("💬 Commencez la conversation en envoyant un message !")
        return
    
    st.markdown("### 📜 Historique de la conversation")
    
    for message in st.session_state.ai_messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="user-message">
                <strong>👤 Vous ({message['timestamp']}) :</strong><br>
                {message['content']}
            </div>
            """, unsafe_allow_html=True)
        else:
            # Affichage des outils utilisés si disponibles
            tools_info = ""
            if message.get("tools_used"):
                tools_info = f"<br><small style='color: #6b7280;'>🛠️ Outils utilisés : {', '.join(message['tools_used'])}</small>"
            
            st.markdown(f"""
            <div class="ai-message">
                <strong>🤖 Assistant ({message['timestamp']}) :</strong><br>
                {message['content']}
                {tools_info}
            </div>
            """, unsafe_allow_html=True)

def export_conversation():
    """Exporte la conversation en fichier texte"""
    
    if not st.session_state.ai_messages:
        st.warning("Aucune conversation à exporter.")
        return
    
    # Construction du contenu du fichier
    content = "=== Conversation avec l'Assistant IA Voyage Japon ===\n\n"
    content += f"Date : {datetime.now().strftime('%d/%m/%Y à %H:%M')}\n\n"
    
    for message in st.session_state.ai_messages:
        role = "Vous" if message["role"] == "user" else "Assistant IA"
        content += f"[{message['timestamp']}] {role} :\n{message['content']}\n\n"
    
    # Téléchargement
    st.download_button(
        label="📥 Télécharger la conversation",
        data=content,
        file_name=f"conversation-ia-japon-{datetime.now().strftime('%Y%m%d-%H%M%S')}.txt",
        mime="text/plain"
    )

# Fonction pour tester la connexion à l'API
def test_groq_connection():
    """Teste la connexion à l'API Groq"""
    try:
        client = groq.Groq(api_key=GROQ_API_KEY)
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": "Bonjour"}],
            max_tokens=10
        )
        return True
    except Exception as e:
        st.error(f"Erreur de connexion à l'API Groq : {str(e)}")
        return False 