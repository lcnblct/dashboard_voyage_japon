# Styles CSS pour l'application - Design moderne et élégant
import streamlit as st

def apply_styles():
    """Applique les styles CSS modernes à l'application"""
    st.markdown("""
    <style>
        /* Variables CSS pour la cohérence */
        :root {
            --primary-color: #6366f1;
            --primary-hover: #4f46e5;
            --secondary-color: #10b981;
            --accent-color: #f59e0b;
            --danger-color: #ef4444;
            --warning-color: #f97316;
            --info-color: #3b82f6;
            
            --bg-primary: #0f172a;
            --bg-secondary: #1e293b;
            --bg-card: #334155;
            --bg-elevated: #475569;
            
            --text-primary: #f8fafc;
            --text-secondary: #cbd5e1;
            --text-muted: #94a3b8;
            
            --border-color: #475569;
            --border-radius: 16px;
            --border-radius-sm: 8px;
            --border-radius-lg: 24px;
            
            --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
            --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
            --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
            
            --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --gradient-secondary: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            --gradient-success: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            --gradient-warning: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        }
        
        /* Reset et base */
        * {
            box-sizing: border-box;
        }
        
        /* Application principale */
        .stApp {
            background: var(--bg-primary) !important;
            color: var(--text-primary) !important;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        }
        
        /* Header et navigation */
        .stApp > header {
            background: var(--bg-secondary) !important;
            backdrop-filter: blur(10px) !important;
            border-bottom: 1px solid var(--border-color) !important;
            box-shadow: var(--shadow) !important;
        }
        
        /* Titres modernes */
        h1, h2, h3, h4, h5, h6 {
            color: var(--text-primary) !important;
            font-weight: 600 !important;
            letter-spacing: -0.025em !important;
            margin-bottom: 1rem !important;
        }
        
        h1 {
            font-size: 2.5rem !important;
            background: var(--gradient-primary) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
            text-align: center !important;
            margin-bottom: 2rem !important;
        }
        
        h2 {
            font-size: 1.875rem !important;
            color: var(--text-primary) !important;
            position: relative !important;
            padding-left: 1rem !important;
        }
        
        h2::before {
            content: '' !important;
            position: absolute !important;
            left: 0 !important;
            top: 50% !important;
            transform: translateY(-50%) !important;
            width: 4px !important;
            height: 24px !important;
            background: var(--gradient-primary) !important;
            border-radius: 2px !important;
        }
        
        /* Métriques modernes */
        .metric-container {
            background: var(--bg-card) !important;
            border-radius: var(--border-radius) !important;
            padding: 1.5rem !important;
            margin: 0.5rem 0 !important;
            border: 1px solid var(--border-color) !important;
            box-shadow: var(--shadow) !important;
            transition: all 0.3s ease !important;
            position: relative !important;
            overflow: hidden !important;
        }
        
        .metric-container::before {
            content: '' !important;
            position: absolute !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            height: 3px !important;
            background: var(--gradient-primary) !important;
        }
        
        .metric-container:hover {
            transform: translateY(-2px) !important;
            box-shadow: var(--shadow-lg) !important;
        }
        
        /* Boutons modernes */
        .stButton > button {
            background: var(--gradient-primary) !important;
            color: white !important;
            border: none !important;
            border-radius: var(--border-radius) !important;
            padding: 0.75rem 1.5rem !important;
            font-weight: 600 !important;
            font-size: 0.875rem !important;
            transition: all 0.3s ease !important;
            box-shadow: var(--shadow) !important;
            position: relative !important;
            overflow: hidden !important;
        }
        
        .stButton > button::before {
            content: '' !important;
            position: absolute !important;
            top: 0 !important;
            left: -100% !important;
            width: 100% !important;
            height: 100% !important;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent) !important;
            transition: left 0.5s !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-1px) !important;
            box-shadow: var(--shadow-lg) !important;
        }
        
        .stButton > button:hover::before {
            left: 100% !important;
        }
        
        /* Cartes et conteneurs */
        .stAlert {
            background: var(--bg-card) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: var(--border-radius) !important;
            padding: 1.25rem !important;
            box-shadow: var(--shadow) !important;
            margin: 0.5rem 0 !important;
            transition: all 0.3s ease !important;
        }
        
        .stAlert:hover {
            transform: translateY(-1px) !important;
            box-shadow: var(--shadow-lg) !important;
        }
        
        /* Formulaires modernes */
        .stTextInput, .stSelectbox, .stNumberInput, .stDateInput, .stTimeInput {
            background: var(--bg-secondary) !important;
            color: var(--text-primary) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: var(--border-radius-sm) !important;
            padding: 0.75rem !important;
            transition: all 0.3s ease !important;
        }
        
        .stTextInput:focus, .stSelectbox:focus, .stNumberInput:focus, .stDateInput:focus, .stTimeInput:focus {
            border-color: var(--primary-color) !important;
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
            outline: none !important;
        }
        
        /* Onglets modernes */
        .stTabs [data-baseweb="tab-list"] {
            background: var(--bg-secondary) !important;
            border-radius: var(--border-radius) !important;
            padding: 0.25rem !important;
            gap: 0.25rem !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            background: transparent !important;
            color: var(--text-secondary) !important;
            border-radius: var(--border-radius-sm) !important;
            padding: 0.75rem 1rem !important;
            transition: all 0.3s ease !important;
            border: none !important;
        }
        
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: var(--gradient-primary) !important;
            color: white !important;
            box-shadow: var(--shadow) !important;
        }
        
        /* Messages d'alerte stylisés */
        .stInfo {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(59, 130, 246, 0.05) 100%) !important;
            border: 1px solid rgba(59, 130, 246, 0.2) !important;
            border-left: 4px solid var(--info-color) !important;
        }
        
        .stSuccess {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%) !important;
            border: 1px solid rgba(16, 185, 129, 0.2) !important;
            border-left: 4px solid var(--secondary-color) !important;
        }
        
        .stWarning {
            background: linear-gradient(135deg, rgba(249, 115, 22, 0.1) 0%, rgba(249, 115, 22, 0.05) 100%) !important;
            border: 1px solid rgba(249, 115, 22, 0.2) !important;
            border-left: 4px solid var(--warning-color) !important;
        }
        
        .stError {
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(239, 68, 68, 0.05) 100%) !important;
            border: 1px solid rgba(239, 68, 68, 0.2) !important;
            border-left: 4px solid var(--danger-color) !important;
        }
        
        /* Calendrier stylisé */
        .calendar-card {
            background: var(--bg-card) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: var(--border-radius) !important;
            color: var(--text-primary) !important;
            padding: 1.5rem !important;
            margin: 0.5rem 0 !important;
            box-shadow: var(--shadow) !important;
            transition: all 0.3s ease !important;
        }
        
        .calendar-card:hover {
            transform: translateY(-2px) !important;
            box-shadow: var(--shadow-lg) !important;
        }
        
        .calendar-date {
            color: var(--secondary-color) !important;
            font-weight: 700 !important;
            font-size: 1.25rem !important;
        }
        
        .calendar-day {
            color: var(--text-muted) !important;
            font-size: 0.875rem !important;
        }
        
        .calendar-city {
            color: var(--accent-color) !important;
            font-weight: 600 !important;
            font-size: 1.125rem !important;
        }
        
        .calendar-activities {
            background: var(--bg-secondary) !important;
            border-left: 4px solid var(--info-color) !important;
            color: var(--text-primary) !important;
            padding: 1rem !important;
            border-radius: var(--border-radius-sm) !important;
            margin: 0.5rem 0 !important;
        }
        
        .calendar-lodging {
            background: var(--bg-secondary) !important;
            border-left: 4px solid var(--accent-color) !important;
            color: var(--text-primary) !important;
            padding: 1rem !important;
            border-radius: var(--border-radius-sm) !important;
            margin: 0.5rem 0 !important;
        }
        
        /* Barre de progression */
        .stProgress > div > div > div > div {
            background: var(--gradient-success) !important;
            border-radius: var(--border-radius-sm) !important;
        }
        
        /* Tableaux modernes */
        .dataframe {
            background: var(--bg-card) !important;
            color: var(--text-primary) !important;
            border-radius: var(--border-radius) !important;
            overflow: hidden !important;
            box-shadow: var(--shadow) !important;
        }
        
        .dataframe th {
            background: var(--bg-elevated) !important;
            color: var(--text-primary) !important;
            font-weight: 600 !important;
            padding: 1rem !important;
        }
        
        .dataframe td {
            padding: 0.75rem 1rem !important;
            border-bottom: 1px solid var(--border-color) !important;
        }
        
        /* Checkbox stylisée */
        .stCheckbox {
            background: var(--bg-secondary) !important;
            color: var(--text-primary) !important;
            border-radius: var(--border-radius-sm) !important;
            padding: 0.5rem !important;
        }
        
        /* Expander stylisé */
        .streamlit-expanderHeader {
            background: var(--bg-card) !important;
            color: var(--text-primary) !important;
            border-radius: var(--border-radius-sm) !important;
            padding: 1rem !important;
            border: 1px solid var(--border-color) !important;
            transition: all 0.3s ease !important;
        }
        
        .streamlit-expanderHeader:hover {
            background: var(--bg-elevated) !important;
            transform: translateY(-1px) !important;
        }
        
        /* Graphiques et visualisations */
        .js-plotly-plot, .plotly-graph-div {
            background: var(--bg-card) !important;
            border-radius: var(--border-radius) !important;
            padding: 1rem !important;
            box-shadow: var(--shadow) !important;
        }
        
        /* Animations d'entrée */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .stAlert, .metric-container, .calendar-card {
            animation: fadeInUp 0.6s ease-out;
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            h1 {
                font-size: 2rem !important;
            }
            
            .metric-container {
                padding: 1rem !important;
            }
            
            .stButton > button {
                padding: 0.5rem 1rem !important;
                font-size: 0.8rem !important;
            }
        }
        
        /* Scrollbar personnalisée */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: var(--bg-secondary);
        }
        
        ::-webkit-scrollbar-thumb {
            background: var(--gradient-primary);
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: var(--primary-hover);
        }
        
        /* Override des couleurs de Streamlit */
        .stApp > footer {
            background: var(--bg-secondary) !important;
            border-top: 1px solid var(--border-color) !important;
        }
        
        /* Styles pour les métriques Streamlit */
        [data-testid="metric-container"] {
            background: var(--bg-card) !important;
            border-radius: var(--border-radius) !important;
            padding: 1.5rem !important;
            border: 1px solid var(--border-color) !important;
            box-shadow: var(--shadow) !important;
            transition: all 0.3s ease !important;
        }
        
        [data-testid="metric-container"]:hover {
            transform: translateY(-2px) !important;
            box-shadow: var(--shadow-lg) !important;
        }
        
        [data-testid="metric-container"]::before {
            content: '' !important;
            position: absolute !important;
            top: 0 !important;
            left: 0 !important;
            right: 0 !important;
            height: 3px !important;
            background: var(--gradient-primary) !important;
        }
    </style>
    """, unsafe_allow_html=True) 