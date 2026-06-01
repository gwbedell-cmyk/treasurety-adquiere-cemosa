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
    """Render navigation bar at top of page. current_page should match button text."""
    nav_html = '''<div class="nav-bar"><div class="nav-container"><a href="/" class="nav-logo">TREASURETY</a><div class="nav-links"><a href="/" class="nav-link {0}">HOME</a><a href="/Treasurety_Adquiere" class="nav-link {1}">REGISTRO</a><a href="/Cadena_de_Evidencia" class="nav-link {2}">CADENA</a><a href="/Conciliacion" class="nav-link {3}">CONCILIACIÓN</a><a href="/CEC" class="nav-link {4}">CEC</a><a href="/WhatsApp_Demo" class="nav-link {5}">DEMO</a><a href="/Resumen_Ejecutivo" class="nav-link {6}">RESUMEN</a></div></div></div>'''.format(
        'active' if current_page == 'HOME' else '',
        'active' if current_page == 'REGISTRO' else '',
        'active' if current_page == 'CADENA' else '',
        'active' if current_page == 'CONCILIACIÓN' else '',
        'active' if current_page == 'CEC' else '',
        'active' if current_page == 'DEMO' else '',
        'active' if current_page == 'RESUMEN' else ''
    )
    st.markdown(nav_html, unsafe_allow_html=True)
