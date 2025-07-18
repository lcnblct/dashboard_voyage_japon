# Styles CSS pour l'application - Mode sombre forcé
import streamlit as st

def apply_styles():
    """Applique les styles CSS à l'application en mode sombre forcé"""
    st.markdown("""
    <style>
        /* Mode sombre forcé - pas de media queries */
        .stApp {
            background-color: #0e1117 !important;
            color: #fafafa !important;
        }
        
        .css-1d391kg {
            background-color: #262730 !important;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #fafafa !important;
        }
        
        p, div, span {
            color: #fafafa !important;
        }
        
        .metric-container {
            background-color: #262730 !important;
            border-radius: 8px !important;
            padding: 10px !important;
            margin: 5px 0 !important;
        }
        
        .stAlert {
            background-color: #262730 !important;
            border: 1px solid #4a4a4a !important;
        }
        
        .dataframe {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        .stTextInput, .stSelectbox, .stNumberInput, .stDateInput, .stTimeInput {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        .stSlider {
            background-color: #262730 !important;
        }
        
        .stCheckbox {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        .streamlit-expanderHeader {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            background-color: #262730 !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        .stInfo {
            background-color: #1e3a8a !important;
            border: 1px solid #3b82f6 !important;
        }
        
        .stSuccess {
            background-color: #166534 !important;
            border: 1px solid #22c55e !important;
        }
        
        .stWarning {
            background-color: #92400e !important;
            border: 1px solid #f59e0b !important;
        }
        
        .stError {
            background-color: #991b1b !important;
            border: 1px solid #ef4444 !important;
        }
        
        .calendar-card {
            background-color: #262730 !important;
            border: 2px solid #4CAF50 !important;
            color: #fafafa !important;
        }
        
        .calendar-date {
            color: #4CAF50 !important;
            font-weight: bold !important;
        }
        
        .calendar-day {
            color: #9CA3AF !important;
        }
        
        .calendar-city {
            color: #f97316 !important;
            font-weight: bold !important;
        }
        
        .calendar-activities {
            background-color: #1e293b !important;
            border-left: 4px solid #3b82f6 !important;
            color: #fafafa !important;
        }
        
        .calendar-lodging {
            background-color: #1e293b !important;
            border-left: 4px solid #f59e0b !important;
            color: #fafafa !important;
        }
        
        /* Styles communs */
        .stButton > button {
            background-color: #4CAF50 !important;
            color: white !important;
            border: none !important;
        }
        
        .stButton > button:hover {
            background-color: #45a049 !important;
        }
        
        .stProgress > div > div > div > div {
            background-color: #4CAF50 !important;
        }
        
        /* Styles supplémentaires pour assurer la cohérence sombre */
        .stMarkdown {
            color: #fafafa !important;
        }
        
        .stDataFrame {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        .stSelectbox > div > div {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        .stTextInput > div > div > input {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        .stNumberInput > div > div > input {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        .stDateInput > div > div > input {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        .stTimeInput > div > div > input {
            background-color: #262730 !important;
            color: #fafafa !important;
        }
        
        /* Override des couleurs de Streamlit */
        .stApp > header {
            background-color: #0e1117 !important;
        }
        
        .stApp > footer {
            background-color: #0e1117 !important;
        }
        
        /* Styles pour les graphiques et visualisations */
        .js-plotly-plot {
            background-color: #262730 !important;
        }
        
        .plotly-graph-div {
            background-color: #262730 !important;
        }
    </style>
    """, unsafe_allow_html=True) 