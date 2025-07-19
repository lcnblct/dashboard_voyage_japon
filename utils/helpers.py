# Fonctions utilitaires pour l'application
import streamlit as st
from datetime import datetime, date
import re

def check_password():
    """Vérifie le code à 4 chiffres de l'application avec pavé numérique virtuel"""
    
    # Initialisation du code saisi
    if "code_input" not in st.session_state:
        st.session_state.code_input = ""
    
    def add_digit(digit):
        """Ajoute un chiffre au code"""
        if len(st.session_state.code_input) < 4:
            st.session_state.code_input += str(digit)
    
    def delete_digit():
        """Supprime le dernier chiffre du code"""
        if st.session_state.code_input:
            st.session_state.code_input = st.session_state.code_input[:-1]
    
    def validate_code():
        """Valide le code saisi"""
        code_input = st.session_state.code_input
        
        # Vérifier que c'est un code à 4 chiffres
        if re.match(r'^\d{4}$', code_input):
            if code_input == st.secrets["ACCESS_CODE"]:
                st.session_state["code_correct"] = True
                st.session_state.code_input = ""  # Efface le code de la session
            else:
                st.session_state["code_correct"] = False
        else:
            st.session_state["code_correct"] = False

    # Interface pour le code à 4 chiffres
    if "code_correct" not in st.session_state:
        st.markdown("""
        <div style="text-align: center; padding: 2rem 0;">
            <h2 style="margin: 0; color: #fafafa;">
                🔐 Accès à l'Application
            </h2>
            <p style="color: #94a3b8; font-size: 1.1rem; margin-top: 0.5rem;">
                Entrez votre code à 4 chiffres
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Affichage du code saisi (avec des points)
        code_display = "•" * len(st.session_state.code_input) + "_" * (4 - len(st.session_state.code_input))
        st.markdown(f"""
        <div style="text-align: center; margin: 2rem 0;">
            <div style="font-family: 'Courier New', monospace; font-size: 2rem; letter-spacing: 1rem; color: #fafafa; margin-bottom: 1rem;">
                {code_display}
            </div>
            <p style="color: #94a3b8; font-size: 0.9rem;">
                {len(st.session_state.code_input)}/4 chiffres
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Pavé numérique virtuel
        st.markdown("""
        <style>
        .numpad-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.5rem;
            margin: 2rem 0;
        }
        .numpad-row {
            display: flex;
            gap: 0.5rem;
        }
        .numpad-button {
            width: 60px;
            height: 60px;
            border: 2px solid #4a5568;
            border-radius: 12px;
            background: linear-gradient(135deg, #2d3748 0%, #4a5568 100%);
            color: #fafafa;
            font-size: 1.5rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            user-select: none;
        }
        .numpad-button:hover {
            background: linear-gradient(135deg, #4a5568 0%, #718096 100%);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        .numpad-button:active {
            transform: translateY(0);
        }
        .numpad-button.delete {
            background: linear-gradient(135deg, #e53e3e 0%, #c53030 100%);
        }
        .numpad-button.delete:hover {
            background: linear-gradient(135deg, #c53030 0%, #a0aec0 100%);
        }
        .numpad-button.enter {
            background: linear-gradient(135deg, #38a169 0%, #2f855a 100%);
        }
        .numpad-button.enter:hover {
            background: linear-gradient(135deg, #2f855a 0%, #276749 100%);
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Première rangée : 1, 2, 3
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("1", key="btn_1", use_container_width=True):
                add_digit(1)
        with col2:
            if st.button("2", key="btn_2", use_container_width=True):
                add_digit(2)
        with col3:
            if st.button("3", key="btn_3", use_container_width=True):
                add_digit(3)
        
        # Deuxième rangée : 4, 5, 6
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("4", key="btn_4", use_container_width=True):
                add_digit(4)
        with col2:
            if st.button("5", key="btn_5", use_container_width=True):
                add_digit(5)
        with col3:
            if st.button("6", key="btn_6", use_container_width=True):
                add_digit(6)
        
        # Troisième rangée : 7, 8, 9
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("7", key="btn_7", use_container_width=True):
                add_digit(7)
        with col2:
            if st.button("8", key="btn_8", use_container_width=True):
                add_digit(8)
        with col3:
            if st.button("9", key="btn_9", use_container_width=True):
                add_digit(9)
        
        # Quatrième rangée : Effacer, 0, Valider
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("⌫", key="btn_delete", use_container_width=True):
                delete_digit()
        with col2:
            if st.button("0", key="btn_0", use_container_width=True):
                add_digit(0)
        with col3:
            if st.button("✓", key="btn_enter", use_container_width=True):
                validate_code()
        
        # Champ de saisie caché pour la compatibilité clavier
        st.text_input(
            "Code d'accès (clavier)", 
            value=st.session_state.code_input,
            type="password", 
            max_chars=4,
            key="code_input_hidden",
            help="Saisie clavier alternative",
            label_visibility="collapsed"
        )
        
        # Validation en temps réel
        if st.session_state.code_input:
            if not re.match(r'^\d{4}$', st.session_state.code_input):
                st.warning("⚠️ Le code doit contenir exactement 4 chiffres")
            elif "code_correct" in st.session_state and not st.session_state["code_correct"]:
                st.error("❌ Code incorrect")
        
        # Auto-validation quand 4 chiffres sont saisis
        if len(st.session_state.code_input) == 4:
            validate_code()
        
        st.stop()
        
    elif not st.session_state["code_correct"]:
        st.markdown("""
        <div style="text-align: center; padding: 2rem 0;">
            <h2 style="margin: 0; color: #fafafa;">
                🔐 Accès à l'Application
            </h2>
            <p style="color: #94a3b8; font-size: 1.1rem; margin-top: 0.5rem;">
                Entrez votre code à 4 chiffres
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Affichage du code saisi (avec des points)
        code_display = "•" * len(st.session_state.code_input) + "_" * (4 - len(st.session_state.code_input))
        st.markdown(f"""
        <div style="text-align: center; margin: 2rem 0;">
            <div style="font-family: 'Courier New', monospace; font-size: 2rem; letter-spacing: 1rem; color: #fafafa; margin-bottom: 1rem;">
                {code_display}
            </div>
            <p style="color: #94a3b8; font-size: 0.9rem;">
                {len(st.session_state.code_input)}/4 chiffres
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Pavé numérique virtuel (même que ci-dessus)
        # Première rangée : 1, 2, 3
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("1", key="btn_1_retry", use_container_width=True):
                add_digit(1)
        with col2:
            if st.button("2", key="btn_2_retry", use_container_width=True):
                add_digit(2)
        with col3:
            if st.button("3", key="btn_3_retry", use_container_width=True):
                add_digit(3)
        
        # Deuxième rangée : 4, 5, 6
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("4", key="btn_4_retry", use_container_width=True):
                add_digit(4)
        with col2:
            if st.button("5", key="btn_5_retry", use_container_width=True):
                add_digit(5)
        with col3:
            if st.button("6", key="btn_6_retry", use_container_width=True):
                add_digit(6)
        
        # Troisième rangée : 7, 8, 9
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("7", key="btn_7_retry", use_container_width=True):
                add_digit(7)
        with col2:
            if st.button("8", key="btn_8_retry", use_container_width=True):
                add_digit(8)
        with col3:
            if st.button("9", key="btn_9_retry", use_container_width=True):
                add_digit(9)
        
        # Quatrième rangée : Effacer, 0, Valider
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("⌫", key="btn_delete_retry", use_container_width=True):
                delete_digit()
        with col2:
            if st.button("0", key="btn_0_retry", use_container_width=True):
                add_digit(0)
        with col3:
            if st.button("✓", key="btn_enter_retry", use_container_width=True):
                validate_code()
        
        # Champ de saisie caché pour la compatibilité clavier
        st.text_input(
            "Code d'accès (clavier)", 
            value=st.session_state.code_input,
            type="password", 
            max_chars=4,
            key="code_input_hidden_retry",
            help="Saisie clavier alternative",
            label_visibility="collapsed"
        )
        
        if st.session_state.code_input:
            if not re.match(r'^\d{4}$', st.session_state.code_input):
                st.warning("⚠️ Le code doit contenir exactement 4 chiffres")
            else:
                st.error("❌ Code incorrect")
        
        # Auto-validation quand 4 chiffres sont saisis
        if len(st.session_state.code_input) == 4:
            validate_code()
        
        st.stop()

def format_currency(amount):
    """Formate un montant en euros"""
    return f"{amount:.2f} €"

def calculate_days_until_departure(departure_date):
    """Calcule le nombre de jours jusqu'au départ"""
    if not departure_date:
        return None
    
    if isinstance(departure_date, str):
        departure_date = datetime.strptime(departure_date, "%Y-%m-%d").date()
    
    days_left = (departure_date - date.today()).days
    return days_left

def get_progress_percentage(completed, total):
    """Calcule le pourcentage de progression"""
    if total == 0:
        return 0
    return (completed / total) * 100

def format_date_for_display(date_str):
    """Formate une date pour l'affichage"""
    if not date_str:
        return "Non définie"
    
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d/%m/%Y")
    except:
        return date_str 