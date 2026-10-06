import streamlit as st
import json, os, time
from datetime import datetime

st.set_page_config(page_title="TOTO WORLD", page_icon="🌍", layout="centered")

def charger():
    if os.path.exists("ultra.json"):
        try:
            with open("ultra.json","r",encoding="utf-8") as f: return json.load(f)
        except: return {"posts":[]}
    return {"posts":[]}
def sauver(d):
    with open("ultra.json","w",encoding="utf-8") as f: json.dump(d,f,ensure_ascii=False)

st.markdown("""
<style>
.stApp{background:#ECE5DD;}
.header{background:linear-gradient(135deg,#075E54,#25D366); color:white; padding:18px; border-radius:18px; text-align:center}
.bubble{max-width:82%; padding:11px 15px; border-radius:16px; margin:8px 0; box-shadow:0 1px 2px rgba(0,0,0,.1); font-size:14px}
.bubble-me{background:#DCF8C6; margin-left:auto; border-bottom-right-radius:4px}
.bubble-other{background:white; margin-right:auto; border-bottom-left-radius:4px}
</style>
<div class='header'><h2>👑 TOTO WORLD 🌍</h2><p>De Toumodi au Monde Entier</p><p style='font-size:11px'>🇨🇮 Toumodi | 🌍 Afrique | 🌎 Monde</p></div>
""", unsafe_allow_html=True)

data=charger()
with st.sidebar:
    st.markdown("### 👑 TOTO WORLD")
    pseudo=st.text_input("Ton nom", placeholder="Toto")
    tel=st.text_input("WhatsApp", placeholder="07XXXXXXXX")
    pays=st.selectbox("Pays", ["🇨🇮 CI","🇲🇱 Mali","🇧🇫 Burkina","🇸🇳 Senegal","🇫🇷 France","🌍 Monde"])

if pseudo:
    for p in data["posts"][-50:]:
        cls="bubble-me" if p["pseudo"]==pseudo else "bubble-other"
        st.markdown(f"<div class='bubble {cls}'><b>{p['pseudo']} {p.get('pays','')}</b><br>{p['texte']}<br><small>{p['heure']} ✓✓</small></div>", unsafe_allow_html=True)
    c1,c2=st.columns([4,1])
    with c1: msg=st.text_input("m", placeholder="Message pour le monde...", label_visibility="collapsed", key="w")
    with c2: send=st.button("🚀", use_container_width=True)
    if send and msg:
        data["posts"].append({"pseudo":pseudo,"tel":tel,"pays":pays,"texte":msg,"heure":datetime.now().strftime("%H:%M"),"date":datetime.now().strftime("%d/%m"),"id":time.time()})
        if len(data["posts"])>300: data["posts"]=data["posts"][-300:]
        sauver(data); st.rerun()
else:
    st.info("👈 Clique sur >> et entre ton nom pour commencer - TOTO WORLD t'attend !")
