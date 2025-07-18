# Styles CSS pour l'application
import streamlit as st

def apply_styles():
    """Applique les styles CSS à l'application"""
    st.markdown("""
    <style>
        /* Thème adaptatif - s'adapte au système */
        @media (prefers-color-scheme: dark) {
            /* Mode sombre */
            .stApp {
                background-color: #0e1117;
                color: #fafafa;
            }
            
            .css-1d391kg {
                background-color: #262730;
            }
            
            h1, h2, h3, h4, h5, h6 {
                color: #fafafa !important;
            }
            
            p, div, span {
                color: #fafafa !important;
            }
            
            .metric-container {
                background-color: #262730;
                border-radius: 8px;
                padding: 10px;
                margin: 5px 0;
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
        }
        
        @media (prefers-color-scheme: light) {
            /* Mode clair */
            .stApp {
                background-color: #ffffff;
                color: #262730;
            }
            
            .css-1d391kg {
                background-color: #f0f2f6;
            }
            
            h1, h2, h3, h4, h5, h6 {
                color: #262730 !important;
            }
            
            p, div, span {
                color: #262730 !important;
            }
            
            .metric-container {
                background-color: #f0f2f6;
                border-radius: 8px;
                padding: 10px;
                margin: 5px 0;
            }
            
            .stAlert {
                background-color: #f0f2f6 !important;
                border: 1px solid #e0e0e0 !important;
            }
            
            .dataframe {
                background-color: #ffffff !important;
                color: #262730 !important;
            }
            
            .stTextInput, .stSelectbox, .stNumberInput, .stDateInput, .stTimeInput {
                background-color: #ffffff !important;
                color: #262730 !important;
            }
            
            .stSlider {
                background-color: #f0f2f6 !important;
            }
            
            .stCheckbox {
                background-color: #f0f2f6 !important;
                color: #262730 !important;
            }
            
            .streamlit-expanderHeader {
                background-color: #f0f2f6 !important;
                color: #262730 !important;
            }
            
            .stTabs [data-baseweb="tab-list"] {
                background-color: #f0f2f6 !important;
            }
            
            .stTabs [data-baseweb="tab"] {
                background-color: #f0f2f6 !important;
                color: #262730 !important;
            }
            
            .stInfo {
                background-color: #dbeafe !important;
                border: 1px solid #3b82f6 !important;
            }
            
            .stSuccess {
                background-color: #dcfce7 !important;
                border: 1px solid #22c55e !important;
            }
            
            .stWarning {
                background-color: #fef3c7 !important;
                border: 1px solid #f59e0b !important;
            }
            
            .stError {
                background-color: #fee2e2 !important;
                border: 1px solid #ef4444 !important;
            }
            
            .calendar-card {
                background-color: #f8fafc !important;
                border: 2px solid #4CAF50 !important;
                color: #262730 !important;
            }
            
            .calendar-date {
                color: #2E7D32 !important;
                font-weight: bold !important;
            }
            
            .calendar-day {
                color: #6B7280 !important;
            }
            
            .calendar-city {
                color: #D97706 !important;
                font-weight: bold !important;
            }
            
            .calendar-activities {
                background-color: #eff6ff !important;
                border-left: 4px solid #3b82f6 !important;
                color: #1e293b !important;
            }
            
            .calendar-lodging {
                background-color: #fffbeb !important;
                border-left: 4px solid #f59e0b !important;
                color: #1e293b !important;
            }
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
    </style>
    """, unsafe_allow_html=True) 