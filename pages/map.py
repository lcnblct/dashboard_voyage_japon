# Page de la carte interactive
import streamlit as st
import folium
from streamlit_folium import st_folium
from data.cities import get_city_coords, get_supported_cities

def display_map():
    """Affiche la carte interactive de l'itinéraire"""
    st.header("🗾 Carte Interactive de l'itinéraire")
    data = st.session_state.data
    itinerary = data.get("itinerary", [])
    
    if not itinerary:
        st.info("Ajoutez des étapes à l'itinéraire pour voir la carte.")
        return
    
    # Récupérer les villes uniques
    cities = {}
    cities_not_found = []
    
    for step in itinerary:
        city = step["city"]
        if city not in cities:
            lat, lon = get_city_coords(city)
            if lat and lon:
                cities[city] = {"lat": lat, "lon": lon, "steps": []}
            else:
                cities_not_found.append(city)
        if city in cities:
            cities[city]["steps"].append(step)
    
    # Afficher les villes non trouvées
    if cities_not_found:
        st.warning(f"Coordonnées non trouvées pour : {', '.join(set(cities_not_found))}")
    
    if not cities:
        st.error("Aucune coordonnée trouvée pour les villes de l'itinéraire.")
        supported_cities = get_supported_cities()
        st.info(f"Villes supportées : {', '.join(supported_cities[:10])}...")
        return
    
    # Centrer la carte sur la première ville
    first_city = next(iter(cities.values()))
    m = folium.Map(location=[first_city["lat"], first_city["lon"]], zoom_start=5)
    
    # Ajouter les marqueurs
    for city, info in cities.items():
        popup = f"<b>{city}</b><br>"
        for step in info["steps"]:
            popup += f"<b>{step['date']}</b> : {step['activities']}<br>"
        
        folium.Marker(
            [info["lat"], info["lon"]],
            popup=folium.Popup(popup, max_width=300),
            tooltip=city,
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(m)
    
    st_folium(m, width=700, height=500) 