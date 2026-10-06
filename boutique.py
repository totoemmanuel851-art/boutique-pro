import streamlit as st
import pandas as pd
from datetime import datetime
st.set_page_config(page_title="Boutique Pro", page_icon="🛒", layout="wide")
st.title("🛒 Boutique Pro - Toumodi")
st.caption(f"Date: {datetime.now().strftime('%d/%m/%Y')} - Toto")
menu = st.sidebar.selectbox("MENU", ["Ventes", "Stock", "Credits", "Bilan"])
if menu == "Ventes":
    st.header("Nouvelle Vente")
    produit = st.text_input("Nom produit")
    prix = st.number_input("Prix FCFA", min_value=0, step=50)
    qte = st.number_input("Quantite", min_value=1, value=1)
    client = st.text_input("Client")
    if st.button("Valider Vente"):
        st.success(f"Vente: {qte} x {produit} = {prix*qte} FCFA")
else:
    st.header("Bilan du Jour")
    c1,c2,c3 = st.columns(3)
    c1.metric("Chiffre", "85 000 FCFA")
    c2.metric("Benefice", "18 500 FCFA")
    c3.metric("Credits", "23 000 FCFA")
