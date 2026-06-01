import streamlit as st
from utils import setup_page, nav_bar

st.set_page_config(page_title="Conciliación · CEMOSA", layout="wide")
setup_page()
nav_bar("CONCILIACIÓN")

st.markdown('<div style="margin-bottom:2rem;"><span class="eyebrow">CONCILIACIÓN</span><div class="page-h1">Factura vs Cadena de Evidencia</div><p style="color:#8BA3C0;font-size:1rem;max-width:760px;line-height:1.7;">Treasurety compara automáticamente lo que el proveedor factura con lo que el equipo en obra evidenció.</p></div>', unsafe_allow_html=True)

# ── EJEMPLO 1 ─────────────────────────────────────────────────────────────────
st.markdown('<span class="eyebrow" style="margin-bottom:0.75rem;display:block;">EJEMPLO 1 · CONCILIACIÓN EXITOSA</span>', unsafe_allow_html=True)

col_inv1, col_cmp1 = st.columns(2)

with col_inv1:
    st.markdown("""
<div class="conc-card">
  <div class="conc-card-title">📄 FACTURA F-2026/8721</div>
  <div class="card-row"><span class="card-label">Proveedor</span><span class="card-value">Áridos y Hormigones Hispalenses, S.L.</span></div>
  <div class="card-row"><span class="card-label">Fecha</span><span class="card-value">30/05/2026</span></div>
  <div class="card-row"><span class="card-label">Obra</span><span class="card-value">Centro Logístico Levante · RADIO 5</span></div>
  <div class="card-row"><span class="card-label">Concepto</span><span class="card-value">Suministro Hormigón HA-25/B/20a</span></div>
  <div class="card-row"><span class="card-label">Cantidad facturada</span><span class="card-value" style="color:#F0F7FF;font-weight:700;">27,00 m³</span></div>
  <div class="card-row"><span class="card-label">Precio unitario</span><span class="card-value">462,22 €/m³</span></div>
  <div class="card-row" style="border-bottom:none;"><span class="card-label">Importe total</span><span class="card-value" style="color:#F0F7FF;font-size:1.05rem;font-weight:800;">12.480,00 €</span></div>
</div>
""", unsafe_allow_html=True)

with col_cmp1:
    st.markdown("""
<div class="conc-card">
  <div class="conc-card-title">⚖️ Comparación automática</div>
  <div class="conc-row-wrap">
    <div class="conc-row"><span class="conc-row-label">Facturado &nbsp; 27 m³</span><div class="conc-bar-track"><div class="conc-bar-fill" style="width:100%;"></div></div></div>
    <div class="conc-row"><span class="conc-row-label">Evidenciado &nbsp; 27 m³</span><div class="conc-bar-track"><div class="conc-bar-fill" style="width:100%;"></div></div></div>
  </div>
  <div style="display:flex;flex-direction:column;gap:0.25rem;margin-bottom:1.25rem;">
    <div class="conc-match-row"><span class="conc-match-ok">&#10003;</span><span>Proveedor coincide</span></div>
    <div class="conc-match-row"><span class="conc-match-ok">&#10003;</span><span>Obra coincide</span></div>
    <div class="conc-match-row"><span class="conc-match-ok">&#10003;</span><span>Material coincide</span></div>
    <div class="conc-match-row"><span class="conc-match-ok">&#10003;</span><span>Cantidad coincide</span></div>
  </div>
  <div style="text-align:center;margin-bottom:0.75rem;"><span class="badge-green" style="font-size:0.82rem;padding:0.5rem 1.2rem;">&#10003; CONCILIADO</span></div>
  <div style="text-align:center;font-size:0.82rem;color:#8BA3C0;">0 excepciones · Pago promovido a CEC</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ── EJEMPLO 2 ─────────────────────────────────────────────────────────────────
st.markdown('<span class="eyebrow" style="margin-bottom:0.75rem;display:block;">EJEMPLO 2 · EXCEPCIÓN DETECTADA</span>', unsafe_allow_html=True)

col_inv2, col_cmp2 = st.columns(2)

with col_inv2:
    st.markdown("""
<div class="conc-card" style="border-color:rgba(245,166,35,0.30);">
  <div class="conc-card-title">📄 FACTURA F-2026/8854</div>
  <div class="card-row"><span class="card-label">Proveedor</span><span class="card-value">Áridos y Hormigones Hispalenses, S.L.</span></div>
  <div class="card-row"><span class="card-label">Fecha</span><span class="card-value">02/06/2026</span></div>
  <div class="card-row"><span class="card-label">Obra</span><span class="card-value">Centro Logístico Levante · RADIO 5</span></div>
  <div class="card-row"><span class="card-label">Cantidad facturada</span><span class="card-value" style="color:#F5A623;font-weight:700;">36,00 m³</span></div>
  <div class="card-row" style="border-bottom:none;"><span class="card-label">Importe total</span><span class="card-value" style="color:#F5A623;font-size:1.05rem;font-weight:800;">16.640,00 €</span></div>
</div>
""", unsafe_allow_html=True)

with col_cmp2:
    st.markdown("""
<div class="conc-card" style="border-color:rgba(245,166,35,0.30);">
  <div class="conc-card-title">⚖️ Comparación automática</div>
  <div class="conc-row-wrap">
    <div class="conc-row"><span class="conc-row-label" style="color:#F5A623;">Facturado &nbsp; 36 m³</span><div class="conc-bar-track"><div class="conc-bar-fill amber" style="width:100%;"></div></div></div>
    <div class="conc-row"><span class="conc-row-label">Evidenciado &nbsp; 27 m³</span><div class="conc-bar-track"><div class="conc-bar-fill" style="width:75%;"></div></div></div>
  </div>
  <div class="conc-diff-box">&#8722;9 m³ no evidenciados &nbsp;·&nbsp; Diferencia: <strong>4.160 €</strong></div>
  <div style="text-align:center;margin-bottom:0.75rem;"><span class="badge-amber" style="font-size:0.82rem;padding:0.5rem 1.2rem;">&#9888; EXCEPCIÓN</span></div>
  <div style="text-align:center;font-size:0.82rem;color:#8BA3C0;margin-bottom:0.75rem;">El sistema ha detenido el pago. Se requiere revisión antes de continuar.</div>
  <div class="info-box" style="border-color:rgba(245,166,35,0.2);background:rgba(245,166,35,0.04);">Treasurety no genera CEC para esta factura hasta resolver la excepción.</div>
</div>
""", unsafe_allow_html=True)
