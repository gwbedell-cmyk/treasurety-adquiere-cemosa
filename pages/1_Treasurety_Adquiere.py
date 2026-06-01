import streamlit as st
from utils import setup_page

st.set_page_config(page_title="Treasurety Adquiere · CEMOSA", layout="wide")
setup_page()

st.markdown('<div style="margin-bottom:2rem;"><span class="eyebrow">TREASURETY ADQUIERE</span><h1 style="color:#FFFFFF;font-size:2.2rem;font-weight:800;margin:0.3rem 0 0.2rem;">Registro de Evidencia</h1><p style="color:#8BA3C0;font-size:1rem;max-width:700px;line-height:1.7;margin-top:0;">De la entrega física al CER criptográfico. Cada paso es obligatorio y verificable.</p></div>', unsafe_allow_html=True)

# ── PASO 1 · DOCUMENTO ────────────────────────────────────────────────────────
st.markdown('<span class="step-label">PASO 1 · DOCUMENTO</span>', unsafe_allow_html=True)

st.markdown("""
<div class="albaran">
  <div class="albaran-header">
    <div>
      <div class="albaran-company">ÁRIDOS Y HORMIGONES HISPALENSES, S.L.</div>
      <div style="color:rgba(255,255,255,0.65);font-size:0.71rem;margin-top:0.2rem;">Pol. Ind. La Isla · Dos Hermanas (Sevilla) · CIF B-41125405 · Tel. 954 88 12 21</div>
    </div>
    <div class="albaran-number">
      <div style="font-size:0.65rem;letter-spacing:0.08em;text-transform:uppercase;color:rgba(255,255,255,0.60);">ALBARÁN DE ENTREGA</div>
      <div style="font-size:1.3rem;font-weight:900;color:#63B8FF;letter-spacing:0.02em;">Nº 0149185</div>
    </div>
  </div>
  <div class="albaran-body">
    <div class="albaran-section">
      <div class="albaran-section-title">Datos del cliente y obra</div>
      <div class="albaran-info-grid">
        <div class="albaran-info-row"><span class="albaran-info-label">Cliente</span><span class="albaran-info-value">CEMOSA</span></div>
        <div class="albaran-info-row"><span class="albaran-info-label">Obra</span><span class="albaran-info-value">Centro Logístico Levante</span></div>
        <div class="albaran-info-row"><span class="albaran-info-label">Proyecto</span><span class="albaran-info-value">RADIO 5</span></div>
        <div class="albaran-info-row"><span class="albaran-info-label">Dirección</span><span class="albaran-info-value">C/ Avda. Andalucía 101, Málaga</span></div>
        <div class="albaran-info-row"><span class="albaran-info-label">Fecha</span><span class="albaran-info-value">28/05/2026</span></div>
        <div class="albaran-info-row"><span class="albaran-info-label">Hora salida</span><span class="albaran-info-value">09:55</span></div>
        <div class="albaran-info-row"><span class="albaran-info-label">Hora llegada</span><span class="albaran-info-value">10:15</span></div>
      </div>
    </div>
    <div class="albaran-section">
      <div class="albaran-section-title">Detalle del suministro</div>
      <table class="albaran-table">
        <thead><tr><th>Código</th><th>Descripción</th><th style="text-align:right;">Cantidad</th><th style="text-align:center;">U.M.</th></tr></thead>
        <tbody><tr><td><strong>HA-25</strong></td><td>Hormigón HA-25/B/20a</td><td style="text-align:right;font-weight:700;">9,00</td><td style="text-align:center;">m³</td></tr></tbody>
      </table>
    </div>
    <div class="albaran-section">
      <div class="albaran-section-title">Datos del transporte</div>
      <div class="albaran-info-grid">
        <div class="albaran-info-row"><span class="albaran-info-label">Matrícula</span><span class="albaran-info-value">3422 XLM</span></div>
        <div class="albaran-info-row"><span class="albaran-info-label">Conductor</span><span class="albaran-info-value">J. Fernández R.</span></div>
        <div class="albaran-info-row"><span class="albaran-info-label">Planta origen</span><span class="albaran-info-value">Planta Sevilla 2</span></div>
      </div>
    </div>
    <div class="albaran-section">
      <div class="albaran-section-title">Observaciones</div>
      <div class="albaran-obs">Entrega confirmada: Recepción en zona de bombeo nivel 1</div>
    </div>
    <div class="albaran-signatures">
      <div class="albaran-sig-box"><div class="albaran-sig-title">FIRMA CONDUCTOR / TRANSPORTISTA</div><div class="albaran-sig-area"></div></div>
      <div class="albaran-sig-box"><div class="albaran-sig-title">FIRMA RECEPTOR / JEFE DE OBRA</div><div class="albaran-sig-area"></div></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="step-arrow">↓</div>', unsafe_allow_html=True)

# ── PASO 2 · AUTENTICACIÓN ────────────────────────────────────────────────────
st.markdown('<span class="step-label">PASO 2 · AUTENTICACIÓN</span>', unsafe_allow_html=True)

col_left, col_right = st.columns(2)
with col_left:
    st.markdown('<div class="card" style="height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:2rem 1.5rem;"><div class="emp-avatar">PM</div><div class="emp-name">Pedro Martín Luque</div><div class="emp-role">Jefe de Obra · EMP-4821</div></div>', unsafe_allow_html=True)
with col_right:
    st.markdown('<div class="card" style="height:100%;"><div class="card-row"><span class="card-label">Empleado</span><span class="card-value">Pedro Martín Luque</span></div><div class="card-row"><span class="card-label">Código</span><span class="card-value">EMP-4821</span></div><div class="card-row"><span class="card-label">Cargo</span><span class="card-value">Jefe de Obra</span></div><div class="card-row"><span class="card-label">Proyecto</span><span class="card-value">RADIO 5</span></div><div style="margin-top:1.25rem;"><span class="badge-green">&#10003; VERIFICADO</span></div></div>', unsafe_allow_html=True)

st.markdown('<div class="step-arrow">↓</div>', unsafe_allow_html=True)

# ── PASO 3 · EXTRACCIÓN OCR + IA ──────────────────────────────────────────────
st.markdown('<span class="step-label">PASO 3 · EXTRACCIÓN OCR + IA</span>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
  <div class="card-title" style="margin-bottom:1rem;">Campos extraídos del documento</div>
  <div class="ext-row"><span class="ext-field">Proveedor</span><span class="ext-value">Á. y H. Hispalenses</span><span class="ext-conf ok">97%</span></div>
  <div class="ext-row"><span class="ext-field">Nº Albarán</span><span class="ext-value">0149185</span><span class="ext-conf ok">99%</span></div>
  <div class="ext-row"><span class="ext-field">Fecha</span><span class="ext-value">28/05/2026</span><span class="ext-conf ok">98%</span></div>
  <div class="ext-row"><span class="ext-field">Material</span><span class="ext-value">Hormigón HA-25</span><span class="ext-conf ok">96%</span></div>
  <div class="ext-row" style="border-bottom:none;"><span class="ext-field">Cantidad</span><span class="ext-value">9,00 m³</span><span class="ext-conf low">62% · Requiere revisión</span></div>
  <div style="padding:0.5rem 0 0.6rem 0;border-bottom:1px solid rgba(99,184,255,0.08);"><span class="badge-amber" style="font-size:0.72rem;margin-left:120px;">⚠ Confianza 62% — campo marcado para revisión humana</span></div>
  <div class="ext-row" style="border-bottom:none;"><span class="ext-field">Proyecto</span><span class="ext-value">RADIO 5</span><span class="ext-conf ok">95%</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="info-box">El sistema detecta campos con baja confianza y los marca para revisión humana antes de registrar la evidencia.</div>', unsafe_allow_html=True)
st.markdown('<div class="step-arrow">↓</div>', unsafe_allow_html=True)

# ── PASO 4 · ATESTACIONES ─────────────────────────────────────────────────────
st.markdown('<span class="step-label">PASO 4 · ATESTACIONES DEL EMPLEADO</span>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
  <div class="card-title" style="margin-bottom:1rem;">Atestaciones de Pedro Martín Luque</div>
  <div class="atest-row"><div class="atest-check">&#10003;</div><span class="atest-text">Entrega recibida físicamente</span></div>
  <div class="atest-row"><div class="atest-check">&#10003;</div><span class="atest-text">Inspección visual realizada</span></div>
  <div class="atest-row"><div class="atest-check">&#10003;</div><span class="atest-text">Cantidad coincide razonablemente con el documento</span></div>
  <div class="atest-row" style="border-bottom:none;"><div class="atest-check">&#10003;</div><span class="atest-text">Sin incidencias registradas</span></div>
  <div style="margin-top:1.25rem;"><span class="badge-green" style="font-size:0.80rem;padding:0.5rem 1.1rem;">4/4 ATESTACIONES</span></div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="info-box">Pedro Martín Luque ha confirmado personalmente cada condición antes de generar la evidencia.</div>', unsafe_allow_html=True)
st.markdown('<div class="step-arrow">↓</div>', unsafe_allow_html=True)

# ── PASO 5 · CER GENERADO ─────────────────────────────────────────────────────
st.markdown('<span class="step-label">PASO 5 · CER GENERADO</span>', unsafe_allow_html=True)

st.markdown("""
<div class="cer-card">
  <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.75rem;margin-bottom:1.25rem;">
    <div class="cer-id">CER-2026-000184</div>
    <span class="badge-green" style="font-size:0.78rem;padding:0.45rem 1rem;">&#10003; EVIDENCIA REGISTRADA</span>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.1rem 2rem;">
    <div class="card-row"><span class="card-label">Empleado</span><span class="card-value">Pedro Martín Luque</span></div>
    <div class="card-row"><span class="card-label">Albarán</span><span class="card-value">0149185</span></div>
    <div class="card-row"><span class="card-label">GPS</span><span class="card-value">37.3841° N, 5.9927° W</span></div>
    <div class="card-row"><span class="card-label">Fecha</span><span class="card-value">28/05/2026</span></div>
    <div class="card-row" style="border-bottom:none;"><span class="card-label">Hora</span><span class="card-value">10:24</span></div>
  </div>
  <div class="hash-block">
    <div class="hash-label">HASH CRIPTOGRÁFICO · SHA-256</div>
    <div class="hash-value">7F4A8C91E3D5A47B&nbsp;&nbsp;1A1D93C7B5E28D66&nbsp;&nbsp;F91A1B83C2E04751</div>
  </div>
  <div style="margin-top:1rem;font-size:0.78rem;color:#8BA3C0;">Cadena de Evidencia · enlace anterior · hash verificable independientemente</div>
</div>
""", unsafe_allow_html=True)
