import streamlit as st
from utils import setup_page

st.set_page_config(
    page_title="Treasurety para CEMOSA",
    page_icon="🏗️",
    layout="wide"
)

setup_page()

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-card">
  <span class="eyebrow">TREASURETY PARA CEMOSA · DOCUMENTO EJECUTIVO</span>
  <h1 class="hero-title">De la evidencia operativa<br>al pago autorizado</h1>
  <p class="hero-subtitle">
    Infraestructura de confianza para ingeniería, construcción e infraestructura.
    Transformando albaranes físicos en evidencia digital verificable.
  </p>
  <blockquote class="hero-blockquote">
    "La factura es una reclamación. La evidencia es la realidad."
  </blockquote>
</div>
""", unsafe_allow_html=True)

# ── Pipeline visual ───────────────────────────────────────────────────────────
st.markdown('<span class="eyebrow">FLUJO DE PROCESO</span>', unsafe_allow_html=True)

c1, arr1, c2, arr2, c3, arr3, c4, arr4, c5 = st.columns([4, 1, 4, 1, 4, 1, 4, 1, 4])

with c1:
    st.markdown("""
    <div class="pipeline-stage">
      <span class="pipeline-icon">📋</span>
      <span class="pipeline-label">REGISTRO</span>
      <span class="pipeline-sub">Albarán → CER</span>
    </div>
    """, unsafe_allow_html=True)

with arr1:
    st.markdown('<div class="pipeline-arrow" style="height:100%;display:flex;align-items:center;justify-content:center;color:rgba(99,184,255,0.45);font-size:1.4rem;">›</div>', unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="pipeline-stage">
      <span class="pipeline-icon">🔗</span>
      <span class="pipeline-label">CADENA</span>
      <span class="pipeline-sub">CERs encadenados</span>
    </div>
    """, unsafe_allow_html=True)

with arr2:
    st.markdown('<div class="pipeline-arrow" style="height:100%;display:flex;align-items:center;justify-content:center;color:rgba(99,184,255,0.45);font-size:1.4rem;">›</div>', unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="pipeline-stage">
      <span class="pipeline-icon">⚖️</span>
      <span class="pipeline-label">CONCILIACIÓN</span>
      <span class="pipeline-sub">Factura vs Evidencia</span>
    </div>
    """, unsafe_allow_html=True)

with arr3:
    st.markdown('<div class="pipeline-arrow" style="height:100%;display:flex;align-items:center;justify-content:center;color:rgba(99,184,255,0.45);font-size:1.4rem;">›</div>', unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="pipeline-stage">
      <span class="pipeline-icon">✅</span>
      <span class="pipeline-label">AUTORIZACIÓN</span>
      <span class="pipeline-sub">Gobernanza aplicada</span>
    </div>
    """, unsafe_allow_html=True)

with arr4:
    st.markdown('<div class="pipeline-arrow" style="height:100%;display:flex;align-items:center;justify-content:center;color:rgba(99,184,255,0.45);font-size:1.4rem;">›</div>', unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="pipeline-stage">
      <span class="pipeline-icon">💳</span>
      <span class="pipeline-label">PAGO</span>
      <span class="pipeline-sub">CPA ejecutado</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ── Case study teaser ─────────────────────────────────────────────────────────
st.markdown("""
<span class="eyebrow">CASO DE USO</span>
<h2 style="color:#FFFFFF !important;font-size:1.55rem;font-weight:800;margin-top:0.2rem;margin-bottom:1.25rem;">
  Recepción de Hormigón en Obra
</h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="case-card">
      <span class="case-card-label">Contexto</span>
      <div class="case-card-item">
        <div class="case-card-dot"></div>
        <span class="case-card-text">CEMOSA · Jefe de Obra en obra</span>
      </div>
      <div class="case-card-item">
        <div class="case-card-dot"></div>
        <span class="case-card-text">Proyecto RADIO 5</span>
      </div>
      <div class="case-card-item">
        <div class="case-card-dot"></div>
        <span class="case-card-text">Hormigón HA-25/B/20a</span>
      </div>
      <div class="case-card-item">
        <div class="case-card-dot"></div>
        <span class="case-card-text">Áridos y Hormigones Hispalenses, S.L.</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="case-card">
      <span class="case-card-label">Resultado</span>
      <div class="case-card-item">
        <div class="case-card-dot"></div>
        <span class="case-card-text"><strong>27 m³</strong> conciliados</span>
      </div>
      <div class="case-card-item">
        <div class="case-card-dot"></div>
        <span class="case-card-text"><strong>3 CERs</strong> en cadena</span>
      </div>
      <div class="case-card-item">
        <div class="case-card-dot"></div>
        <span class="case-card-text"><strong>0 excepciones</strong> detectadas</span>
      </div>
      <div class="case-card-item">
        <div class="case-card-dot"></div>
        <span class="case-card-text">Conciliación 100%</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="case-card">
      <span class="case-card-label">Output</span>
      <div class="case-card-item">
        <div class="case-card-dot"></div>
        <span class="case-card-text">CPA emitido</span>
      </div>
      <div class="case-card-item">
        <div class="case-card-dot"></div>
        <span class="case-card-text"><strong>12.480 €</strong> autorizado</span>
      </div>
      <div class="case-card-item">
        <div class="case-card-dot"></div>
        <span class="case-card-text">Política SOX-OBRA</span>
      </div>
      <div class="case-card-item">
        <div class="case-card-dot"></div>
        <span class="case-card-text">2/2 aprobadores</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ── Closing mantra ────────────────────────────────────────────────────────────
st.markdown("""
<div class="mantra-card">
  <div class="mantra-text">
    Sin <span>CER</span> no hay evidencia. &nbsp;·&nbsp;
    Sin <span>Cadena</span> no hay contexto. &nbsp;·&nbsp;
    Sin <span>Conciliación</span> no hay CEC.<br>
    Sin <span>CEC</span> no hay autorización. &nbsp;·&nbsp;
    Sin <span>CPA</span> no hay pago.
  </div>
</div>
""", unsafe_allow_html=True)
