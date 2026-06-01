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
