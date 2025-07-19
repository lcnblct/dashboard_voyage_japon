# Fonctions utilitaires pour l'application
import streamlit as st
from datetime import datetime, date
import re

def check_password():
    """Vérifie le code à 4 chiffres de l'application avec pavé numérique virtuel élégant"""
    
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
        <div style="text-align: center; padding: 1rem 0;">
            <h2 style="margin: 0; color: #fafafa; font-size: 2rem; font-weight: 300;">
                🔐 Accès à l'Application
            </h2>
            <p style="color: #94a3b8; font-size: 1rem; margin-top: 0.5rem; font-weight: 300;">
                Entrez votre code à 4 chiffres
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Affichage du code saisi (avec des points)
        code_display = "•" * len(st.session_state.code_input) + "_" * (4 - len(st.session_state.code_input))
        st.markdown(f"""
        <div style="text-align: center; margin: 1.5rem 0;">
            <div style="font-family: 'Courier New', monospace; font-size: 2rem; letter-spacing: 1rem; color: #fafafa; margin-bottom: 1rem; font-weight: 600;">
                {code_display}
            </div>
            <p style="color: #94a3b8; font-size: 0.9rem; font-weight: 300;">
                {len(st.session_state.code_input)}/4 chiffres
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # CSS pour le clavier numérique élégant
        st.markdown("""
        <style>
        .numpad-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.5rem;
            margin: 1rem auto;
            max-width: 300px;
            padding: 0 1rem;
        }
        .numpad-row {
            display: flex;
            gap: 0.5rem;
            justify-content: center;
            width: 100%;
        }
        .numpad-button {
            width: 60px;
            height: 60px;
            border: none;
            border-radius: 12px;
            background: linear-gradient(145deg, #2d3748, #1a202c);
            color: #fafafa;
            font-size: 1.5rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            align-items: center;
            justify-content: center;
            user-select: none;
            box-shadow: 
                0 2px 4px -1px rgba(0, 0, 0, 0.1),
                0 1px 2px -1px rgba(0, 0, 0, 0.06),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
            flex: 1;
            max-width: 60px;
        }
        .numpad-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(145deg, rgba(255,255,255,0.1), transparent);
            opacity: 0;
            transition: opacity 0.2s ease;
        }
        .numpad-button:hover {
            background: linear-gradient(145deg, #4a5568, #2d3748);
            transform: translateY(-2px) scale(1.02);
            box-shadow: 
                0 4px 8px -2px rgba(0, 0, 0, 0.2),
                0 2px 4px -1px rgba(0, 0, 0, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
        }
        .numpad-button:hover::before {
            opacity: 1;
        }
        .numpad-button:active {
            transform: translateY(0) scale(0.98);
            box-shadow: 
                0 1px 2px -1px rgba(0, 0, 0, 0.2),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
        }
        .numpad-button.delete {
            background: linear-gradient(145deg, #e53e3e, #c53030);
            font-size: 1.3rem;
        }
        .numpad-button.delete:hover {
            background: linear-gradient(145deg, #f56565, #e53e3e);
        }
        .numpad-button.enter {
            background: linear-gradient(145deg, #38a169, #2f855a);
            font-size: 1.3rem;
        }
        .numpad-button.enter:hover {
            background: linear-gradient(145deg, #48bb78, #38a169);
        }
        
        /* Responsive pour mobile */
        @media (max-width: 768px) {
            .numpad-container {
                max-width: 280px;
                gap: 0.4rem;
                margin: 0.5rem auto;
            }
            .numpad-row {
                gap: 0.4rem;
            }
            .numpad-button {
                width: 50px;
                height: 50px;
                font-size: 1.3rem;
                border-radius: 10px;
                max-width: 50px;
            }
            .numpad-button.delete, .numpad-button.enter {
                font-size: 1.1rem;
            }
        }
        
        /* Très petits écrans */
        @media (max-width: 480px) {
            .numpad-container {
                max-width: 240px;
                gap: 0.3rem;
            }
            .numpad-row {
                gap: 0.3rem;
            }
            .numpad-button {
                width: 45px;
                height: 45px;
                font-size: 1.2rem;
                border-radius: 8px;
                max-width: 45px;
            }
            .numpad-button.delete, .numpad-button.enter {
                font-size: 1rem;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Container pour le clavier
        st.markdown('<div class="numpad-container">', unsafe_allow_html=True)
        
        # Première rangée : 1, 2, 3
        col1, col2, col3 = st.columns([1, 1, 1])
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
        col1, col2, col3 = st.columns([1, 1, 1])
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
        col1, col2, col3 = st.columns([1, 1, 1])
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
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("⌫", key="btn_delete", use_container_width=True):
                delete_digit()
        with col2:
            if st.button("0", key="btn_0", use_container_width=True):
                add_digit(0)
        with col3:
            if st.button("✓", key="btn_enter", use_container_width=True):
                validate_code()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Validation en temps réel
        if st.session_state.code_input:
            if not re.match(r'^\d{4}$', st.session_state.code_input):
                st.warning("⚠️ Le code doit contenir exactement 4 chiffres")
            elif "code_correct" in st.session_state and not st.session_state["code_correct"]:
                st.error("❌ Code incorrect")
        
        # Auto-validation quand 4 chiffres sont saisis
        if len(st.session_state.code_input) == 4:
            validate_code()
            st.rerun()
        
        st.stop()
        
    elif not st.session_state["code_correct"]:
        st.markdown("""
        <div style="text-align: center; padding: 1rem 0;">
            <h2 style="margin: 0; color: #fafafa; font-size: 2rem; font-weight: 300;">
                🔐 Accès à l'Application
            </h2>
            <p style="color: #94a3b8; font-size: 1rem; margin-top: 0.5rem; font-weight: 300;">
                Entrez votre code à 4 chiffres
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Affichage du code saisi (avec des points)
        code_display = "•" * len(st.session_state.code_input) + "_" * (4 - len(st.session_state.code_input))
        st.markdown(f"""
        <div style="text-align: center; margin: 1.5rem 0;">
            <div style="font-family: 'Courier New', monospace; font-size: 2rem; letter-spacing: 1rem; color: #fafafa; margin-bottom: 1rem; font-weight: 600;">
                {code_display}
            </div>
            <p style="color: #94a3b8; font-size: 0.9rem; font-weight: 300;">
                {len(st.session_state.code_input)}/4 chiffres
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # CSS pour le clavier numérique élégant (même style)
        st.markdown("""
        <style>
        .numpad-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.5rem;
            margin: 1rem auto;
            max-width: 300px;
            padding: 0 1rem;
        }
        .numpad-row {
            display: flex;
            gap: 0.5rem;
            justify-content: center;
            width: 100%;
        }
        .numpad-button {
            width: 60px;
            height: 60px;
            border: none;
            border-radius: 12px;
            background: linear-gradient(145deg, #2d3748, #1a202c);
            color: #fafafa;
            font-size: 1.5rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            align-items: center;
            justify-content: center;
            user-select: none;
            box-shadow: 
                0 2px 4px -1px rgba(0, 0, 0, 0.1),
                0 1px 2px -1px rgba(0, 0, 0, 0.06),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
            flex: 1;
            max-width: 60px;
        }
        .numpad-button::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(145deg, rgba(255,255,255,0.1), transparent);
            opacity: 0;
            transition: opacity 0.2s ease;
        }
        .numpad-button:hover {
            background: linear-gradient(145deg, #4a5568, #2d3748);
            transform: translateY(-2px) scale(1.02);
            box-shadow: 
                0 4px 8px -2px rgba(0, 0, 0, 0.2),
                0 2px 4px -1px rgba(0, 0, 0, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
        }
        .numpad-button:hover::before {
            opacity: 1;
        }
        .numpad-button:active {
            transform: translateY(0) scale(0.98);
            box-shadow: 
                0 1px 2px -1px rgba(0, 0, 0, 0.2),
                inset 0 1px 0 rgba(255, 255, 255, 0.1);
        }
        .numpad-button.delete {
            background: linear-gradient(145deg, #e53e3e, #c53030);
            font-size: 1.3rem;
        }
        .numpad-button.delete:hover {
            background: linear-gradient(145deg, #f56565, #e53e3e);
        }
        .numpad-button.enter {
            background: linear-gradient(145deg, #38a169, #2f855a);
            font-size: 1.3rem;
        }
        .numpad-button.enter:hover {
            background: linear-gradient(145deg, #48bb78, #38a169);
        }
        
        /* Responsive pour mobile */
        @media (max-width: 768px) {
            .numpad-container {
                max-width: 280px;
                gap: 0.4rem;
                margin: 0.5rem auto;
            }
            .numpad-row {
                gap: 0.4rem;
            }
            .numpad-button {
                width: 50px;
                height: 50px;
                font-size: 1.3rem;
                border-radius: 10px;
                max-width: 50px;
            }
            .numpad-button.delete, .numpad-button.enter {
                font-size: 1.1rem;
            }
        }
        
        /* Très petits écrans */
        @media (max-width: 480px) {
            .numpad-container {
                max-width: 240px;
                gap: 0.3rem;
            }
            .numpad-row {
                gap: 0.3rem;
            }
            .numpad-button {
                width: 45px;
                height: 45px;
                font-size: 1.2rem;
                border-radius: 8px;
                max-width: 45px;
            }
            .numpad-button.delete, .numpad-button.enter {
                font-size: 1rem;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Container pour le clavier
        st.markdown('<div class="numpad-container">', unsafe_allow_html=True)
        
        # Première rangée : 1, 2, 3
        col1, col2, col3 = st.columns([1, 1, 1])
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
        col1, col2, col3 = st.columns([1, 1, 1])
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
        col1, col2, col3 = st.columns([1, 1, 1])
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
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("⌫", key="btn_delete_retry", use_container_width=True):
                delete_digit()
        with col2:
            if st.button("0", key="btn_0_retry", use_container_width=True):
                add_digit(0)
        with col3:
            if st.button("✓", key="btn_enter_retry", use_container_width=True):
                validate_code()
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.session_state.code_input:
            if not re.match(r'^\d{4}$', st.session_state.code_input):
                st.warning("⚠️ Le code doit contenir exactement 4 chiffres")
            else:
                st.error("❌ Code incorrect")
        
        # Auto-validation quand 4 chiffres sont saisis
        if len(st.session_state.code_input) == 4:
            validate_code()
            st.rerun()
        
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