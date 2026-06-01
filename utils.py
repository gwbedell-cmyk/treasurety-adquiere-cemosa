import streamlit as st
import os

_LOGO = os.path.join(os.path.dirname(__file__), "assets", "logo.png")
_CSS  = os.path.join(os.path.dirname(__file__), "assets", "css.css")

def load_css():
    with open(_CSS) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def setup_page():
    """Load CSS."""
    load_css()

def nav_bar(current_page):
    """Render navigation bar at top of page using st.page_link."""
    st.markdown('<div class="nav-bar-spacer"></div>', unsafe_allow_html=True)
    cols = st.columns([0.8, 1.5, 1.5, 1.5, 1.2, 1.2, 1.5, 1.2])

    with cols[0]:
        st.markdown('<div class="nav-logo">TREASURETY</div>', unsafe_allow_html=True)

    with cols[1]:
        st.page_link("Main_App.py", label="HOME", use_container_width=True)
    with cols[2]:
        st.page_link("pages/1_Treasurety_Adquiere.py", label="REGISTRO", use_container_width=True)
    with cols[3]:
        st.page_link("pages/2_Cadena_de_Evidencia.py", label="CADENA", use_container_width=True)
    with cols[4]:
        st.page_link("pages/3_Conciliacion.py", label="CONCILIACIÓN", use_container_width=True)
    with cols[5]:
        st.page_link("pages/4_CEC.py", label="CEC", use_container_width=True)
    with cols[6]:
        st.page_link("pages/5_WhatsApp_Demo.py", label="DEMO", use_container_width=True)
    with cols[7]:
        st.page_link("pages/6_Resumen_Ejecutivo.py", label="RESUMEN", use_container_width=True)
