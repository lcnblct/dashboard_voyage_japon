# Page des ressources utiles
import streamlit as st

def display_resources():
    """Affiche la page des ressources utiles"""
    st.header("🔗 Ressources Utiles")
    
    st.subheader("Convertisseur EUR → JPY")
    taux = 165  # Taux fixe, à ajuster ou automatiser
    eur = st.number_input("Montant en EUR", min_value=0.0, step=1.0, key="eur_input")
    jpy = eur * taux
    st.write(f"≈ {jpy:.0f} ¥ (taux : 1€ = {taux}¥)")
    
    st.subheader("Phrases utiles 🇯🇵")
    st.markdown("""
- Bonjour : こんにちは (Konnichiwa)
- Merci : ありがとう (Arigatou)
- Excusez-moi : すみません (Sumimasen)
- Oui : はい (Hai)
- Non : いいえ (Iie)
- Où sont les toilettes ? : トイREはどこですか？ (Toire wa doko desu ka?)
    """)
    
    st.subheader("Liens importants")
    st.markdown("""
- [Ambassade du Japon en France](https://www.fr.emb-japan.go.jp/)
- [Japan Rail Pass](https://www.japan-rail-pass.fr/)
- [Hyperdia (trains)](https://www.hyperdia.com/)
- [JR East](https://www.jreast.co.jp/e/)
    """) 