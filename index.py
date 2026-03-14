import streamlit as st
import os
 
st.set_page_config(
    page_title="GAER Madness 2026",
    page_icon="🏀",
    layout="wide",
    initial_sidebar_state="collapsed"
)
 
# Hide Streamlit default chrome
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        .stApp {background: #0a0c10;}
    </style>
""", unsafe_allow_html=True)
 
html_path = os.path.join(os.path.dirname(__file__), "march_madness_2026.html")
 
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()
 
st.components.v1.html(html_content, height=1200, scrolling=True)
