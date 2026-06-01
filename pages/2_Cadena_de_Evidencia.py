import streamlit as st
from utils import setup_page

st.set_page_config(page_title="Cadena de Evidencia · CEMOSA", layout="wide")
setup_page()

st.markdown('<div style="margin-bottom:2rem;"><span class="eyebrow">CADENA DE EVIDENCIA</span><div class="page-h1">Tres entregas. Una cadena criptográfica.</div><p style="color:#8BA3C0;font-size:1rem;max-width:760px;line-height:1.7;margin-top:0;">Cada CER se encadena con el anterior mediante hash. La cadena reconstruye la historia completa de las entregas.</p></div>', unsafe_allow_html=True)

col_chain, col_summary = st.columns([2, 1])

with col_chain:
    st.markdown("""
<div class="chain-container">
  <div class="chain-item">
    <div class="chain-dot"></div>
    <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;">
      <div class="chain-item-id">CER-2026-000184</div>
      <span class="badge-green" style="font-size:0.7rem;">REGISTRADO</span>
    </div>
    <div class="chain-item-meta">
      <strong>28/05/2026 · 10:24</strong><br>
      Albarán 0149185 · Áridos y Hormigones Hispalenses, S.L.<br>
      9,00 m³ &nbsp;·&nbsp; Hormigón HA-25/B/20a<br>
      Pedro Martín Luque · GPS 37.3841° N, 5.9927° W
    </div>
    <div class="chain-hash-small">SHA-256 &nbsp;·&nbsp; 7F4A8C91...C2E04751</div>
  </div>
  <div class="chain-connector"></div>
  <div class="chain-item">
    <div class="chain-dot"></div>
    <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;">
      <div class="chain-item-id">CER-2026-000208</div>
      <span class="badge-green" style="font-size:0.7rem;">REGISTRADO</span>
    </div>
    <div class="chain-item-meta">
      <strong>28/05/2026 · 11:47</strong><br>
      Albarán 0149223 · Áridos y Hormigones Hispalenses, S.L.<br>
      9,00 m³ &nbsp;·&nbsp; Hormigón HA-25/B/20a
    </div>
    <div class="chain-hash-small">SHA-256 &nbsp;·&nbsp; 3B8D2E5F...C9D0E5F3</div>
  </div>
  <div class="chain-connector"></div>
  <div class="chain-item" style="margin-bottom:0;">
    <div class="chain-dot"></div>
    <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;">
      <div class="chain-item-id">CER-2026-000214</div>
      <span class="badge-green" style="font-size:0.7rem;">REGISTRADO</span>
    </div>
    <div class="chain-item-meta">
      <strong>28/05/2026 · 13:09</strong><br>
      Albarán 0149261 · Áridos y Hormigones Hispalenses, S.L.<br>
      9,00 m³ &nbsp;·&nbsp; Hormigón HA-25/B/20a
    </div>
    <div class="chain-hash-small">SHA-256 &nbsp;·&nbsp; A9C3E7D1...9E2B4051</div>
  </div>
</div>
""", unsafe_allow_html=True)

with col_summary:
    st.markdown("""
<div class="card" style="margin-bottom:1rem;text-align:center;padding:1.5rem;">
  <div style="font-size:2rem;font-weight:900;color:#F0F7FF;">3 entregas</div>
  <div style="font-size:1.4rem;font-weight:700;color:#63B8FF;">27 m³ totales</div>
</div>
""", unsafe_allow_html=True)
    st.markdown("""
<div class="card" style="margin-bottom:1rem;">
  <div class="card-title">Línea de tiempo</div>
  <div class="card-row"><span class="card-label">Primera recepción</span><span class="card-value">10:24</span></div>
  <div class="card-row"><span class="card-label">Segunda recepción</span><span class="card-value">11:47</span></div>
  <div class="card-row"><span class="card-label">Última recepción</span><span class="card-value">13:09</span></div>
  <div class="card-row" style="border-bottom:none;"><span class="card-label">Duración total</span><span class="card-value">2h 45min</span></div>
</div>
""", unsafe_allow_html=True)
    st.markdown("""
<div class="card" style="margin-bottom:1rem;">
  <div class="card-title">Hash de la Cadena</div>
  <div class="hash-block" style="font-size:0.72rem;">
    <div class="hash-label">SHA-256 · CADENA COMPLETA</div>
    <div class="hash-value">2E8F4A1D7C3B590E<br>6A2D481F9C5E207B<br>4F1A3C8D2E9B0F6A</div>
  </div>
  <div style="margin-top:1rem;text-align:center;"><span class="badge-green">&#10003; CADENA ÍNTEGRA</span></div>
</div>
""", unsafe_allow_html=True)
    st.markdown('<div class="info-box">El hash de la Cadena de Evidencia encapsula los tres CERs. Si cualquier dato cambia, el hash cambia. Cualquier auditor puede verificarlo años después.</div>', unsafe_allow_html=True)
