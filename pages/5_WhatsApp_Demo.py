import streamlit as st
from utils import setup_page

st.set_page_config(page_title="Demo WhatsApp · CEMOSA", layout="wide")
setup_page()

st.markdown('<div style="margin-bottom:1.5rem;"><span class="eyebrow">CAPTURA EN SITU</span><div class="page-h1">Demo WhatsApp</div><p style="color:#8BA3C0;font-size:1rem;max-width:760px;line-height:1.7;">El Jefe de Obra captura evidencia desde obra usando WhatsApp. Identidad verificada, atestaciones confirmadas, CER generado.</p></div>', unsafe_allow_html=True)
st.markdown('<div class="info-box" style="max-width:760px;margin-bottom:2rem;">El canal de captura no importa. Lo que importa es la evidencia que genera Treasurety. WhatsApp es simplemente el punto de entrada más natural para el personal en obra.</div>', unsafe_allow_html=True)

col_left, col_right = st.columns(2)

# ── PANEL 1: Captura e identificación ────────────────────────────────────────
with col_left:
    st.markdown('<div style="color:#63B8FF;font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.75rem;">1. Captura e identificación</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="wa-outer">
<div class="wa-container">
<div class="wa-header">
<div class="wa-header-avatar">T</div>
<div class="wa-header-info">
<span class="wa-header-name">Treasurety · CEMOSA Evidencia</span>
<span class="wa-header-status">en línea</span>
</div>
</div>
<div class="wa-chat">
<div>
<div class="wa-bot">Bienvenido a CEMOSA Evidencia.<br>Introduzca su número de empleado.</div>
<div class="wa-bot-time">10:21</div>
</div>
<div style="display:flex;flex-direction:column;align-items:flex-end;">
<div class="wa-user">EMP-4821</div>
<div class="wa-user-time">10:21 ✓✓</div>
</div>
<div>
<div class="wa-bot">Empleado identificado.<br>Nombre: Pedro Martín Luque<br>Cargo: Jefe de Obra<br>Proyecto: RADIO 5<br>¿Es correcta esta información?<br>1. Sí &nbsp; 2. No</div>
<div class="wa-bot-time">10:21</div>
</div>
<div style="display:flex;flex-direction:column;align-items:flex-end;">
<div class="wa-user">Sí</div>
<div class="wa-user-time">10:22 ✓✓</div>
</div>
<div>
<div class="wa-bot">Adjunte fotografía del documento.</div>
<div class="wa-bot-time">10:22</div>
</div>
<div style="display:flex;flex-direction:column;align-items:flex-end;">
<div class="wa-user" style="padding:0.4rem 0.65rem;"><div class="wa-doc-attachment"><span class="wa-doc-icon">📄</span><div><div class="wa-doc-name">Albarán 0149185.jpg</div><div style="font-size:0.68rem;color:#666;">Imagen · 1.2 MB</div></div></div></div>
<div class="wa-user-time">10:23 ✓✓</div>
</div>
<div>
<div class="wa-bot">Documento detectado.<br>Tipo: Albarán de Hormigón<br>Proveedor: Áridos y Hormigones Hispalenses<br>Número: 0149185 · Cantidad: 9 m³ · Proyecto: RADIO 5</div>
<div class="wa-bot-time">10:23</div>
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# ── PANEL 2: Atestación y registro ───────────────────────────────────────────
with col_right:
    st.markdown('<div style="color:#63B8FF;font-size:0.72rem;font-weight:700;text-transform:uppercase;letter-spacing:0.14em;margin-bottom:0.75rem;">2. Atestación y registro</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="wa-outer">
<div class="wa-container">
<div class="wa-header">
<div class="wa-header-avatar">T</div>
<div class="wa-header-info">
<span class="wa-header-name">Treasurety · CEMOSA Evidencia</span>
<span class="wa-header-status">en línea</span>
</div>
</div>
<div class="wa-chat">
<div>
<div class="wa-bot">¿Confirma que ha recibido físicamente la entrega?<br>1. Sí &nbsp; 2. No</div>
<div class="wa-bot-time">10:23</div>
</div>
<div style="display:flex;flex-direction:column;align-items:flex-end;">
<div class="wa-user">Sí</div>
<div class="wa-user-time">10:23 ✓✓</div>
</div>
<div>
<div class="wa-bot">¿Ha inspeccionado visualmente los materiales?<br>1. Sí &nbsp; 2. No</div>
<div class="wa-bot-time">10:23</div>
</div>
<div style="display:flex;flex-direction:column;align-items:flex-end;">
<div class="wa-user">Sí</div>
<div class="wa-user-time">10:23 ✓✓</div>
</div>
<div>
<div class="wa-bot">¿La cantidad recibida coincide razonablemente con el documento?<br>1. Sí &nbsp; 2. No</div>
<div class="wa-bot-time">10:24</div>
</div>
<div style="display:flex;flex-direction:column;align-items:flex-end;">
<div class="wa-user">Sí</div>
<div class="wa-user-time">10:24 ✓✓</div>
</div>
<div>
<div class="wa-bot">¿Desea registrar alguna incidencia?<br>1. No &nbsp; 2. Añadir incidencia</div>
<div class="wa-bot-time">10:24</div>
</div>
<div style="display:flex;flex-direction:column;align-items:flex-end;">
<div class="wa-user">No</div>
<div class="wa-user-time">10:24 ✓✓</div>
</div>
<div>
<div class="wa-bot">Resumen del CER<br>Empleado: Pedro Martín Luque<br>Documento: 0149185<br>Proveedor: Áridos y Hormigones Hispalenses<br>Cantidad: 9 m³ · Proyecto: RADIO 5<br>¿Confirma el envío? 1. Confirmar &nbsp; 2. Cancelar</div>
<div class="wa-bot-time">10:24</div>
</div>
<div style="display:flex;flex-direction:column;align-items:flex-end;">
<div class="wa-user">Confirmar</div>
<div class="wa-user-time">10:24 ✓✓</div>
</div>
<div>
<div class="wa-confirmed">
<div class="wa-confirmed-title">&#10003; EVIDENCIA REGISTRADA</div>
<div class="wa-confirmed-row"><span class="wa-confirmed-label">CER</span><span class="wa-confirmed-value">CER-2026-000184</span></div>
<div class="wa-confirmed-row"><span class="wa-confirmed-label">ESTADO</span><span class="wa-confirmed-value" style="color:#22D3A5;font-weight:700;">Registrado</span></div>
<div class="wa-confirmed-row"><span class="wa-confirmed-label">FECHA</span><span class="wa-confirmed-value">28/05/2026</span></div>
<div class="wa-confirmed-row"><span class="wa-confirmed-label">HORA</span><span class="wa-confirmed-value">10:24</span></div>
<div class="wa-hash-block">
<span class="wa-hash-label">HASH CRIPTOGRÁFICA · SHA-256</span><br>
7F4A8C91E3D5A47B<br>1A1D93C7B5E28D66<br>F91A1B83
</div>
<div style="margin-top:0.3rem;padding:0.28rem 0.5rem;background:rgba(34,211,165,0.08);border:1px solid rgba(34,211,165,0.25);border-radius:6px;font-size:0.68rem;color:#22D3A5;font-weight:600;text-align:center;">Incorporado a la Cadena de Evidencia</div>
</div>
<div class="wa-bot-time">10:24</div>
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

col_why, col_what = st.columns(2)
with col_why:
    st.markdown("""
<div class="card">
  <div class="card-title">¿Por qué WhatsApp?</div>
  <div class="atest-row"><div class="atest-check">&#10003;</div><span class="atest-text">Cualquier smartphone, sin instalar aplicación adicional</span></div>
  <div class="atest-row"><div class="atest-check">&#10003;</div><span class="atest-text">Funciona en obra con señal baja</span></div>
  <div class="atest-row"><div class="atest-check">&#10003;</div><span class="atest-text">Interfaz familiar para el personal de obra</span></div>
  <div class="atest-row" style="border-bottom:none;"><div class="atest-check">&#10003;</div><span class="atest-text">Sin curva de aprendizaje ni formación adicional</span></div>
</div>
""", unsafe_allow_html=True)
with col_what:
    st.markdown("""
<div class="card">
  <div class="card-title">¿Qué genera Treasurety?</div>
  <div class="atest-row"><div class="atest-check">&#10003;</div><span class="atest-text">CER con hash criptográfico SHA-256</span></div>
  <div class="atest-row"><div class="atest-check">&#10003;</div><span class="atest-text">Coordenadas GPS y marca temporal</span></div>
  <div class="atest-row"><div class="atest-check">&#10003;</div><span class="atest-text">Identidad del empleado verificada</span></div>
  <div class="atest-row" style="border-bottom:none;"><div class="atest-check">&#10003;</div><span class="atest-text">Atestaciones físicas firmadas criptográficamente</span></div>
</div>
""", unsafe_allow_html=True)
