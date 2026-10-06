import streamlit as st
import json, os, time
from datetime import datetime

st.set_page_config(page_title="TOTO CHAT ULTRA", page_icon="⚡", layout="centered")

def charger():
    if os.path.exists("ultra.json"):
        try:
            with open("ultra.json","r",encoding="utf-8") as f:
                return json.load(f)
        except:
            return {"posts":[]}
    return {"posts":[]}

def sauver(d):
    with open("ultra.json","w",encoding="utf-8") as f:
        json.dump(d,f,ensure_ascii=False)

st.markdown("""
<h2 style='text-align:center'>⚡ TOTO CHAT ULTRA</h2>
<p style='text-align:center'>Bouaké - Rapide | Numéros directs | Annuaire</p>
""", unsafe_allow_html=True)

data = charger()

with st.sidebar:
    st.header("Connexion")
    pseudo = st.text_input("Ton pseudo", max_chars=15)
    tel = st.text_input("Ton WhatsApp", placeholder="07XXXXXXXX")
    st.write(f"Messages: {len(data['posts'])}")
    st.divider()
    st.subheader("📞 Annuaire")
    nums = {}
    for p in data["posts"]:
        if p.get("tel"):
            nums[p["pseudo"]] = p["tel"]
    for nom, num in list(nums.items())[-10:]:
        st.write(f"{nom}: {num}")

if pseudo:
    msg = st.text_input("Ton message", placeholder="Ecris ici...")
    if st.button("⚡ Envoyer", use_container_width=True):
        if msg:
            data["posts"].append({
                "pseudo": pseudo,
                "tel": tel,
                "texte": msg,
                "heure": datetime.now().strftime("%H:%M"),
                "date": datetime.now().strftime("%d/%m"),
                "id": time.time()
            })
            if len(data["posts"]) > 100:
                data["posts"] = data["posts"][-100:]
            sauver(data)
            st.rerun()
    
    st.divider()
    for p in reversed(data["posts"][-50:]):
        st.markdown(f"**{p['pseudo']}** - {p['date']} {p['heure']}")
        st.write(p['texte'])
        if p.get("tel"):
            st.markdown(f"[💬 WhatsApp](https://wa.me/225{p['tel']}) | [📞 Appeler](tel:{p['tel']})")
            st.write("---")
else:
    st.warning("👈 Entre ton pseudo à gauche pour commencer")
    st.info("✅ Ultra rapide (<1s) | ✅ Numéros directs | ✅ Annuaire Bouaké | ✅ Mode hors-ligne")
