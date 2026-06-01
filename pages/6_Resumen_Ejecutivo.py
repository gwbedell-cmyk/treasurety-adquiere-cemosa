import streamlit as st
from utils import load_css

st.set_page_config(page_title="Resumen Ejecutivo · CEMOSA", layout="wide")
load_css()

# ── Page header ───────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-bottom:2rem;">
  <span class="eyebrow">PARA DIRECCIÓN Y COMITÉS EJECUTIVOS</span>
  <h1 style="color:#F0F7FF;font-size:2.2rem;font-weight:800;margin:0.3rem 0 0.6rem;">
    Resumen Ejecutivo
  </h1>
  <p style="color:#8BA3C0;font-size:1rem;max-width:700px;line-height:1.7;">
    Tres preguntas. Respuestas directas.
  </p>
</div>
""", unsafe_allow_html=True)

# ── Question 1 ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="question-card">
  <div class="question-number">01</div>
  <div class="question-title">¿Qué problema resolvemos?</div>
  <div class="question-body">
    En obras de construcción, las recepciones de materiales se anotan en papel.
    El albarán físico puede perderse, alterarse o simplemente no reflejar lo que se entregó
    realmente. La conciliación manual entre albaranes y facturas es lenta, cara y propensa
    a errores. Cuando un auditor interno necesita verificar un pago de hace 18 meses,
    la evidencia ya no existe de forma verificable.
    <br><br>
    CEMOSA procesa miles de albaranes al año. Cada uno es un riesgo no gestionado.
  </div>
</div>
""", unsafe_allow_html=True)

# ── Question 2 ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="question-card">
  <div class="question-number">02</div>
  <div class="question-title">¿Cómo funciona?</div>
  <div class="question-body">
    Cuando un camión de hormigón llega a obra, el Jefe de Obra abre WhatsApp.
    En dos minutos: identifica, fotografía el albarán, atestigua físicamente la entrega,
    y Treasurety genera un CER (Contenedor de Evidencia Registrada) con hash criptográfico,
    GPS y marca temporal.
    <br><br>
    Tres entregas más tarde, Treasurety ensambla automáticamente la Cadena de Evidencia.
    Cuando llega la factura del proveedor, Treasurety la concilia automáticamente contra
    la cadena. Si coincide: CEC emitido, pago autorizado. Si no coincide: excepción
    explicada, pago detenido.
  </div>
</div>
""", unsafe_allow_html=True)

# ── Question 3 ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="question-card">
  <div class="question-number">03</div>
  <div class="question-title">¿Por qué importa?</div>
  <div class="question-body">
    El hash es verificable años después, sin el sistema original. Un auditor puede
    recalcular el hash en 2031 y confirmar que los datos de 2026 no han sido manipulados.
    La conciliación automática detecta sobrefacturación antes de que el pago sea autorizado.
    Cada euro pagado tiene una cadena de evidencia trazable hasta el momento y lugar
    físico de la entrega.
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ── Benefits grid ─────────────────────────────────────────────────────────────
st.markdown("""
<h2 style="color:#F0F7FF;font-size:1.5rem;font-weight:700;margin-bottom:1.5rem;">
  Beneficios Clave
</h2>
""", unsafe_allow_html=True)

benefits = [
    ("01", "Evidencia Digital",
     "Documentos físicos transformados en evidencia verificable e inmutable."),
    ("02", "Trazabilidad",
     "Quién, qué, dónde, cuándo — con documento y atestación."),
    ("03", "Conciliación Automática",
     "Factura ↔ Cadena de Evidencia, con excepciones explicadas."),
    ("04", "Menos Papel",
     "Eliminación de notas manuscritas y archivos físicos en obra."),
    ("05", "Menos Errores",
     "Validación de baja confianza, revisión humana cuando procede."),
    ("06", "Mejor Auditoría",
     "Encadenamiento criptográfico verificable retrospectivamente."),
    ("07", "Autorización Gobernada",
     "Reglas, límites, aprobadores y segregación de funciones."),
    ("08", "Listo para SII",
     "Trazabilidad y evidencia compatibles con el marco normativo español."),
    ("09", "Escalabilidad",
     "Multi-proyecto, multi-proveedor, multi-obra."),
]

rows = [benefits[0:3], benefits[3:6], benefits[6:9]]

for row in rows:
    cols = st.columns(3)
    for col, (num, title, body) in zip(cols, row):
        with col:
            st.markdown(f"""
            <div class="benefit-card">
              <div class="benefit-num">{num}</div>
              <div class="benefit-title">{title}</div>
              <div class="benefit-body">{body}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("<div style='height:0.75rem;'></div>", unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# ── Closing mantra ────────────────────────────────────────────────────────────
st.markdown("""
<div class="mantra-card">
  <div class="mantra-text">
    Sin <span>CER</span> no hay evidencia.<br>
    Sin <span>Cadena de Evidencia</span> no hay contexto.<br>
    Sin <span>Conciliación</span> no hay CEC.<br>
    Sin <span>CEC</span> no hay autorización.<br>
    Sin <span>CPA</span> no hay pago.
  </div>
  <div class="mantra-italic">
    Transformando evidencia operativa en decisiones económicas gobernadas.
  </div>
</div>
""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-footer">
  Treasurety es una filial de iThoth Systems Inc. · Toronto · Canada
</div>
""", unsafe_allow_html=True)
