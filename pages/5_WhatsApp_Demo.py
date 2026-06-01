import streamlit as st
from utils import load_css

st.set_page_config(page_title="Demo WhatsApp · CEMOSA", layout="wide")
load_css()

# ── Page header ───────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-bottom:1.5rem;">
  <span class="eyebrow">CAPTURA EN SITU</span>
  <h1 style="color:#F0F7FF;font-size:2.2rem;font-weight:800;margin:0.3rem 0 0.6rem;">
    Demo WhatsApp
  </h1>
  <p style="color:#8BA3C0;font-size:1rem;max-width:760px;line-height:1.7;">
    El Jefe de Obra captura evidencia desde obra usando WhatsApp. Identidad verificada,
    atestaciones confirmadas, CER generado.
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-box" style="max-width:760px;margin-bottom:2rem;">
  El canal de captura no importa. Lo que importa es la evidencia que genera Treasurety.
  WhatsApp es simplemente el punto de entrada más natural para el personal en obra.
</div>
""", unsafe_allow_html=True)

# ── WhatsApp phone UI ─────────────────────────────────────────────────────────
col_phone, col_spacer = st.columns([1, 1])

with col_phone:
    st.markdown("""
<div class="wa-outer">
<div class="wa-container">

  <!-- Header -->
  <div class="wa-header">
    <div class="wa-header-avatar">T</div>
    <div class="wa-header-info">
      <span class="wa-header-name">Treasurety · CEMOSA Evidencia</span>
      <span class="wa-header-status">en línea</span>
    </div>
  </div>

  <!-- Chat -->
  <div class="wa-chat">

    <!-- 1. Bot welcome -->
    <div>
      <div class="wa-bot">Bienvenido a CEMOSA Evidencia. Introduzca su número de empleado.</div>
      <div class="wa-bot-time">10:21</div>
    </div>

    <!-- 2. User EMP -->
    <div style="align-self:flex-end;display:flex;flex-direction:column;align-items:flex-end;">
      <div class="wa-user">EMP-4821</div>
      <div class="wa-user-time">10:21 ✓✓</div>
    </div>

    <!-- 3. Bot identification -->
    <div>
      <div class="wa-bot">Empleado identificado.

Nombre: Pedro Martín Luque
Cargo: Jefe de Obra
Proyecto: RADIO 5

¿Es correcta esta información?
1. Sí &nbsp; 2. No</div>
      <div class="wa-bot-time">10:21</div>
    </div>

    <!-- 4. User confirm -->
    <div style="align-self:flex-end;display:flex;flex-direction:column;align-items:flex-end;">
      <div class="wa-user">Sí</div>
      <div class="wa-user-time">10:22 ✓✓</div>
    </div>

    <!-- 5. Bot photo request -->
    <div>
      <div class="wa-bot">Adjunte fotografía del documento.</div>
      <div class="wa-bot-time">10:22</div>
    </div>

    <!-- 6. User doc attachment -->
    <div style="align-self:flex-end;display:flex;flex-direction:column;align-items:flex-end;">
      <div class="wa-user" style="padding:0.4rem 0.65rem;">
        <div class="wa-doc-attachment">
          <span class="wa-doc-icon">📄</span>
          <div>
            <div class="wa-doc-name">Albarán 0149185.jpg</div>
            <div style="font-size:0.68rem;color:#666;">Imagen · 1.2 MB</div>
          </div>
        </div>
      </div>
      <div class="wa-user-time">10:23 ✓✓</div>
    </div>

    <!-- 7. Bot document detected -->
    <div>
      <div class="wa-bot">Documento detectado.

Tipo: Albarán de Hormigón
Proveedor: Áridos y Hormigones Hispalenses
Número: 0149185 · Cantidad: 9 m³ · Proyecto: RADIO 5</div>
      <div class="wa-bot-time">10:23</div>
    </div>

    <!-- 8. Bot attestation 1 -->
    <div>
      <div class="wa-bot">¿Confirma que ha recibido físicamente la entrega?
1. Sí &nbsp; 2. No</div>
      <div class="wa-bot-time">10:23</div>
    </div>

    <!-- 9. User yes -->
    <div style="align-self:flex-end;display:flex;flex-direction:column;align-items:flex-end;">
      <div class="wa-user">Sí</div>
      <div class="wa-user-time">10:23 ✓✓</div>
    </div>

    <!-- 10. Bot attestation 2 -->
    <div>
      <div class="wa-bot">¿Ha inspeccionado visualmente los materiales?
1. Sí &nbsp; 2. No</div>
      <div class="wa-bot-time">10:23</div>
    </div>

    <!-- 11. User yes -->
    <div style="align-self:flex-end;display:flex;flex-direction:column;align-items:flex-end;">
      <div class="wa-user">Sí</div>
      <div class="wa-user-time">10:23 ✓✓</div>
    </div>

    <!-- 12. Bot attestation 3 -->
    <div>
      <div class="wa-bot">¿La cantidad recibida coincide razonablemente con el documento?
1. Sí &nbsp; 2. No</div>
      <div class="wa-bot-time">10:24</div>
    </div>

    <!-- 13. User yes -->
    <div style="align-self:flex-end;display:flex;flex-direction:column;align-items:flex-end;">
      <div class="wa-user">Sí</div>
      <div class="wa-user-time">10:24 ✓✓</div>
    </div>

    <!-- 14. Bot attestation 4 -->
    <div>
      <div class="wa-bot">¿Desea registrar alguna incidencia?
1. No &nbsp; 2. Añadir incidencia</div>
      <div class="wa-bot-time">10:24</div>
    </div>

    <!-- 15. User no -->
    <div style="align-self:flex-end;display:flex;flex-direction:column;align-items:flex-end;">
      <div class="wa-user">No</div>
      <div class="wa-user-time">10:24 ✓✓</div>
    </div>

    <!-- 16. Bot summary -->
    <div>
      <div class="wa-bot">Resumen del CER

Empleado: Pedro Martín Luque
Documento: 0149185 · Proveedor: Áridos y Hormigones Hispalenses
Cantidad: 9 m³ · Proyecto: RADIO 5

¿Confirma el envío?
1. Confirmar &nbsp; 2. Cancelar</div>
      <div class="wa-bot-time">10:24</div>
    </div>

    <!-- 17. User confirm -->
    <div style="align-self:flex-end;display:flex;flex-direction:column;align-items:flex-end;">
      <div class="wa-user">Confirmar</div>
      <div class="wa-user-time">10:24 ✓✓</div>
    </div>

    <!-- 18. EVIDENCIA REGISTRADA card -->
    <div>
      <div class="wa-confirmed">
        <div class="wa-confirmed-title">&#10003; EVIDENCIA REGISTRADA</div>

        <div class="wa-confirmed-row">
          <span class="wa-confirmed-label">CER</span>
          <span class="wa-confirmed-value">CER-2026-000184</span>
        </div>
        <div class="wa-confirmed-row">
          <span class="wa-confirmed-label">ESTADO</span>
          <span class="wa-confirmed-value" style="color:#22D3A5;">Registrado</span>
        </div>
        <div class="wa-confirmed-row">
          <span class="wa-confirmed-label">FECHA</span>
          <span class="wa-confirmed-value">28/05/2026</span>
        </div>
        <div class="wa-confirmed-row">
          <span class="wa-confirmed-label">HORA</span>
          <span class="wa-confirmed-value">10:24</span>
        </div>

        <div class="wa-hash-block">
          <span class="wa-hash-label">HASH CRIPTOGRÁFICA · SHA-256</span>
          7F4A8C91E3D5A47B 1A1D93C7B5E28D66<br>
          F91A1B83C2E04751
        </div>

        <div style="margin-top:0.5rem;font-size:0.68rem;color:#8BA3C0;">
          Cadena de Evidencia · enlace anterior
        </div>
      </div>
      <div class="wa-bot-time">10:24</div>
    </div>

  </div><!-- /wa-chat -->
</div><!-- /wa-container -->
</div><!-- /wa-outer -->
""", unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ── Callout columns ───────────────────────────────────────────────────────────
col_why, col_what = st.columns(2)

with col_why:
    st.markdown("""
    <div class="card">
      <div class="card-title">¿Por qué WhatsApp?</div>
      <div class="atest-row">
        <div class="atest-check">&#10003;</div>
        <span class="atest-text">Cualquier smartphone, sin instalar aplicación adicional</span>
      </div>
      <div class="atest-row">
        <div class="atest-check">&#10003;</div>
        <span class="atest-text">Funciona en obra con señal baja</span>
      </div>
      <div class="atest-row">
        <div class="atest-check">&#10003;</div>
        <span class="atest-text">Interfaz familiar para el personal de obra</span>
      </div>
      <div class="atest-row">
        <div class="atest-check">&#10003;</div>
        <span class="atest-text">Sin curva de aprendizaje ni formación adicional</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_what:
    st.markdown("""
    <div class="card">
      <div class="card-title">¿Qué genera Treasurety?</div>
      <div class="atest-row">
        <div class="atest-check">&#10003;</div>
        <span class="atest-text">CER con hash criptográfico SHA-256</span>
      </div>
      <div class="atest-row">
        <div class="atest-check">&#10003;</div>
        <span class="atest-text">Coordenadas GPS y marca temporal</span>
      </div>
      <div class="atest-row">
        <div class="atest-check">&#10003;</div>
        <span class="atest-text">Identidad del empleado verificada</span>
      </div>
      <div class="atest-row">
        <div class="atest-check">&#10003;</div>
        <span class="atest-text">Atestaciones físicas firmadas criptográficamente</span>
      </div>
    </div>
    """, unsafe_allow_html=True)
