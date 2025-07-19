# Page des informations de vol
import streamlit as st
from data.models import get_default_flight_info
from data.storage import sync_state

def display_flight():
    """Affiche la page des informations de vol"""
    st.header("✈️ Informations de Vol")
    data = st.session_state.data
    flight_info = data.get("flight_info", get_default_flight_info())
    
    # Onglets pour aller et retour
    tab1, tab2 = st.tabs(["🛫 Aller", "🛬 Retour"])
    
    with tab1:
        st.subheader("Vol Aller")
        outbound = flight_info["outbound"]
        
        col1, col2 = st.columns(2)
        with col1:
            outbound["airline"] = st.text_input("Compagnie aérienne", value=outbound["airline"], key="out_airline")
            outbound["flight_number"] = st.text_input("Numéro de vol", value=outbound["flight_number"], key="out_flight")
            outbound["departure_airport"] = st.text_input("Aéroport de départ", value=outbound["departure_airport"], key="out_dep")
            outbound["arrival_airport"] = st.text_input("Aéroport d'arrivée", value=outbound["arrival_airport"], key="out_arr")
            outbound["departure_date"] = st.date_input("Date de départ", value=datetime.strptime(outbound["departure_date"], "%Y-%m-%d").date(), key="out_date")
        
        with col2:
            outbound["departure_time"] = st.time_input("Heure de départ", value=datetime.strptime(outbound["departure_time"], "%H:%M").time(), key="out_dep_time")
            outbound["arrival_time"] = st.time_input("Heure d'arrivée", value=datetime.strptime(outbound["arrival_time"], "%H:%M").time(), key="out_arr_time")
            outbound["terminal_departure"] = st.text_input("Terminal départ", value=outbound["terminal_departure"], key="out_term_dep")
            outbound["terminal_arrival"] = st.text_input("Terminal arrivée", value=outbound["terminal_arrival"], key="out_term_arr")
            outbound["booking_reference"] = st.text_input("Référence réservation", value=outbound["booking_reference"], key="out_ref")
        
        col1, col2 = st.columns(2)
        with col1:
            outbound["checked_in"] = st.checkbox("Check-in effectué", value=outbound["checked_in"], key="out_checkin")
        with col2:
            outbound["boarding_pass"] = st.checkbox("Carte d'embarquement", value=outbound["boarding_pass"], key="out_boarding")
    
    with tab2:
        st.subheader("Vol Retour")
        return_flight = flight_info["return"]
        
        col1, col2 = st.columns(2)
        with col1:
            return_flight["airline"] = st.text_input("Compagnie aérienne", value=return_flight["airline"], key="ret_airline")
            return_flight["flight_number"] = st.text_input("Numéro de vol", value=return_flight["flight_number"], key="ret_flight")
            return_flight["departure_airport"] = st.text_input("Aéroport de départ", value=return_flight["departure_airport"], key="ret_dep")
            return_flight["arrival_airport"] = st.text_input("Aéroport d'arrivée", value=return_flight["arrival_airport"], key="ret_arr")
            return_flight["departure_date"] = st.date_input("Date de départ", value=datetime.strptime(return_flight["departure_date"], "%Y-%m-%d").date(), key="ret_date")
        
        with col2:
            return_flight["departure_time"] = st.time_input("Heure de départ", value=datetime.strptime(return_flight["departure_time"], "%H:%M").time(), key="ret_dep_time")
            return_flight["arrival_time"] = st.time_input("Heure d'arrivée", value=datetime.strptime(return_flight["arrival_time"], "%H:%M").time(), key="ret_arr_time")
            return_flight["terminal_departure"] = st.text_input("Terminal départ", value=return_flight["terminal_departure"], key="ret_term_dep")
            return_flight["terminal_arrival"] = st.text_input("Terminal arrivée", value=return_flight["terminal_arrival"], key="ret_term_arr")
            return_flight["booking_reference"] = st.text_input("Référence réservation", value=return_flight["booking_reference"], key="ret_ref")
        
        col1, col2 = st.columns(2)
        with col1:
            return_flight["checked_in"] = st.checkbox("Check-in effectué", value=return_flight["checked_in"], key="ret_checkin")
        with col2:
            return_flight["boarding_pass"] = st.checkbox("Carte d'embarquement", value=return_flight["boarding_pass"], key="ret_boarding")
    
    # Informations générales
    st.subheader("📋 Informations Générales")
    col1, col2 = st.columns(2)
    with col1:
        flight_info["baggage_allowance"] = st.text_input("Franchise bagage", value=flight_info["baggage_allowance"])
        flight_info["meal_preference"] = st.text_input("Préférence repas", value=flight_info["meal_preference"])
    with col2:
        flight_info["seat_selection"] = st.checkbox("Sélection de siège", value=flight_info["seat_selection"])
        flight_info["special_assistance"] = st.text_input("Assistance spéciale", value=flight_info["special_assistance"])
    
    flight_info["notes"] = st.text_area("Notes", value=flight_info["notes"])
    
    # Bouton de sauvegarde
    if st.button("💾 Sauvegarder les informations de vol", type="primary"):
        sync_state()
        st.success("Informations de vol sauvegardées !") 