# Page de gestion du budget
import streamlit as st
import pandas as pd
from data.storage import sync_state
from utils.helpers import format_currency

def display_budget():
    """Affiche la page de gestion du budget"""
    st.header("💰 Gestion du Budget")
    data = st.session_state.data
    
    # Ajout d'une dépense
    with st.form("add_expense"):
        col1, col2, col3 = st.columns(3)
        with col1:
            category = st.selectbox("Catégorie", [
                "Transport", "Hébergement", "Nourriture", "Activités", 
                "Shopping", "Autres"
            ])
        with col2:
            amount = st.number_input("Montant (€)", min_value=0.0, step=0.01)
        with col3:
            date_expense = st.date_input("Date")
        
        description = st.text_input("Description")
        submitted = st.form_submit_button("Ajouter la dépense")
        
        if submitted and amount > 0:
            data["budget"].append({
                "category": category,
                "amount": amount,
                "date": str(date_expense),
                "description": description
            })
            sync_state()
            st.success("Dépense ajoutée !")
            st.rerun()
    
    # Affichage du budget
    if data["budget"]:
        st.subheader("📊 Résumé du Budget")
        
        # Calculs
        total = sum([b["amount"] for b in data["budget"]])
        by_category = {}
        for expense in data["budget"]:
            cat = expense["category"]
            if cat not in by_category:
                by_category[cat] = 0
            by_category[cat] += expense["amount"]
        
        # Métriques
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total dépensé", format_currency(total))
        with col2:
            st.metric("Nombre de dépenses", len(data["budget"]))
        with col3:
            avg_per_expense = total / len(data["budget"]) if data["budget"] else 0
            st.metric("Moyenne par dépense", format_currency(avg_per_expense))
        with col4:
            # Budget par jour depuis le profil
            profile = data.get("travel_profile", {})
            budget_per_day = profile.get("budget_per_day", 150)
            st.metric("Budget cible/jour", format_currency(budget_per_day))
        
        # Graphique par catégorie
        st.subheader("📈 Répartition par Catégorie")
        if by_category:
            chart_data = pd.DataFrame([
                {"Catégorie": cat, "Montant": amount}
                for cat, amount in by_category.items()
            ])
            st.bar_chart(chart_data.set_index("Catégorie"))
        
        # Liste des dépenses
        st.subheader("📋 Détail des Dépenses")
        df = pd.DataFrame(data["budget"])
        df = df.sort_values("date", ascending=False)
        
        for idx, row in df.iterrows():
            with st.expander(f"{row['date']} - {row['category']} - {format_currency(row['amount'])}"):
                st.write(f"**Description :** {row['description']}")
                st.write(f"**Catégorie :** {row['category']}")
                st.write(f"**Montant :** {format_currency(row['amount'])}")
                if st.button(f"Supprimer", key=f"del_budget_{idx}"):
                    data["budget"].pop(idx)
                    sync_state()
                    st.rerun()
    else:
        st.info("Aucune dépense enregistrée pour l'instant.") 