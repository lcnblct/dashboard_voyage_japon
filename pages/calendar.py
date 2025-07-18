# Page du calendrier
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import locale

def display_calendar():
    """Affiche la page du calendrier"""
    st.header("📅 Calendrier du Voyage")
    data = st.session_state.data
    itinerary = data.get("itinerary", [])
    
    if not itinerary:
        st.info("Ajoutez des étapes à l'itinéraire pour voir le calendrier.")
        return
    
    # Trier l'itinéraire par date
    sorted_itinerary = sorted(itinerary, key=lambda x: x["date"])
    
    # Créer un DataFrame pour l'affichage
    df_data = []
    for step in sorted_itinerary:
        date_obj = datetime.strptime(step["date"], "%Y-%m-%d")
        df_data.append({
            "date": step["date"],
            "date_formatted": date_obj.strftime("%d/%m/%Y"),
            "jour_semaine_fr": date_obj.strftime("%A").capitalize(),
            "city": step["city"],
            "activities": step["activities"],
            "lodging": step["lodging"]
        })
    
    df = pd.DataFrame(df_data)
    
    # Affichage en cartes
    st.subheader("📋 Vue Calendrier")
    
    for idx, row in df.iterrows():
        # Carte pour chaque jour
        with st.container():
            st.markdown(f"""
            <div class="calendar-card" style="
                border: 2px solid #4CAF50;
                border-radius: 10px;
                padding: 15px;
                margin: 10px 0;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            ">
                <h4 class="calendar-date" style="margin: 0; font-weight: bold;">{row['date_formatted']}</h4>
                <p class="calendar-day" style="margin: 5px 0; font-size: 0.9em; font-weight: 500;">{row['jour_semaine_fr']}</p>
                <h5 class="calendar-city" style="margin: 10px 0; font-weight: bold;">🏙️ {row['city']}</h5>
                <div class="calendar-activities" style="padding: 10px; border-radius: 5px; margin: 10px 0; border-left: 4px solid #3B82F6;">
                    <strong>📋 Activités :</strong><br>
                    <span>{row['activities'] if row['activities'] else 'Aucune activité prévue'}</span>
                </div>
                <div class="calendar-lodging" style="padding: 10px; border-radius: 5px; border-left: 4px solid #F59E0B;">
                    <strong>🏨 Hébergement :</strong><br>
                    <span>{row['lodging'] if row['lodging'] else 'Non défini'}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Affichage en tableau pour une vue plus compacte
    st.subheader("📊 Vue Tableau")
    
    # Créer un tableau stylisé
    table_data = []
    for idx, row in df.iterrows():
        table_data.append({
            "📅 Date": row["date_formatted"],
            "📆 Jour": row["jour_semaine_fr"],
            "🏙️ Ville": row["city"],
            "📋 Activités": row["activities"][:100] + "..." if len(row["activities"]) > 100 else row["activities"],
            "🏨 Hébergement": row["lodging"][:50] + "..." if len(row["lodging"]) > 50 else row["lodging"]
        })
    
    table_df = pd.DataFrame(table_data)
    st.dataframe(table_df, use_container_width=True, hide_index=True)
    
    # Statistiques du voyage
    st.subheader("📈 Statistiques du Voyage")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📅 Durée", f"{len(sorted_itinerary)} jours")
    
    with col2:
        unique_cities = len(set(step["city"] for step in sorted_itinerary))
        st.metric("🏙️ Villes visitées", unique_cities)
    
    with col3:
        start_date = sorted_itinerary[0]["date"]
        end_date = sorted_itinerary[-1]["date"]
        st.metric("🗓️ Période", f"{start_date} → {end_date}")
    
    with col4:
        # Compter les types d'hébergement
        accommodations = [step["lodging"] for step in sorted_itinerary if step["lodging"]]
        hotel_count = sum(1 for acc in accommodations if "hôtel" in acc.lower() or "hotel" in acc.lower())
        ryokan_count = sum(1 for acc in accommodations if "ryokan" in acc.lower())
        st.metric("🏨 Types d'hébergement", f"{hotel_count} hôtels, {ryokan_count} ryokan") 