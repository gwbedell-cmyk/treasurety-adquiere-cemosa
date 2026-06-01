import streamlit as st
from utils import load_css

st.set_page_config(page_title="CEC · CEMOSA", layout="wide")
load_css()

# ── Page header ───────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-bottom:2rem;">
  <span class="eyebrow">CEC · CONTENEDOR DE EXPEDIENTE CONCILIADO</span>
  <h1 style="color:#F0F7FF;font-size:2.2rem;font-weight:800;margin:0.3rem 0 0.6rem;">
    Expediente listo para autorización
  </h1>
  <p style="color:#8BA3C0;font-size:1rem;max-width:760px;line-height:1.7;">
    El CEC encapsula la factura, los CERs, el resultado de conciliación y un hash
    verificable. Es la entrada al proceso de autorización de pago.
  </p>
</div>
""", unsafe_allow_html=True)

col_main, col_side = st.columns([2, 1])

# ── Left — CEC main card ──────────────────────────────────────────────────────
with col_main:
    st.markdown("""
    <div class="cer-card">

      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.75rem;margin-bottom:1.5rem;">
        <div>
          <div style="font-size:0.7rem;font-weight:700;text-transform:uppercase;letter-spacing:0.15em;color:#8BA3C0;margin-bottom:0.2rem;">
            CONTENEDOR DE EXPEDIENTE CONCILIADO
          </div>
          <div class="cer-id">CEC-2026-000041</div>
        </div>
        <span class="badge-green badge-large">&#10003; EXPEDIENTE CONCILIADO</span>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.1rem 2rem;margin-bottom:1.25rem;">
        <div class="card-row">
          <span class="card-label">Factura</span>
          <span class="card-value">F-2026/8721</span>
        </div>
        <div class="card-row">
          <span class="card-label">Proveedor</span>
          <span class="card-value">Áridos y Hormigones Hispalenses, S.L.</span>
        </div>
        <div class="card-row">
          <span class="card-label">Obra</span>
          <span class="card-value">Centro Logístico Levante · RADIO 5</span>
        </div>
        <div class="card-row">
          <span class="card-label">CERs asociados</span>
          <span class="card-value">3 (CER-184, CER-208, CER-214)</span>
        </div>
        <div class="card-row">
          <span class="card-label">Volumen conciliado</span>
          <span class="card-value" style="color:#F0F7FF;font-weight:700;">27,00 m³</span>
        </div>
        <div class="card-row">
          <span class="card-label">Importe</span>
          <span class="card-value" style="color:#F0F7FF;font-weight:800;font-size:1.05rem;">12.480,00 €</span>
        </div>
        <div class="card-row">
          <span class="card-label">Resultado conciliación</span>
          <span class="card-value" style="color:#22D3A5;font-weight:700;">100% · 0 excepciones</span>
        </div>
        <div class="card-row" style="border-bottom:none;">
          <span class="card-label">Fecha CEC</span>
          <span class="card-value">30/05/2026 · 14:32</span>
        </div>
      </div>

      <div class="hash-block">
        <span class="hash-label">HASH CEC · SHA-256</span>
        B84D912ACF18E772&nbsp;&nbsp;91C3D5F7A2E84B1C&nbsp;&nbsp;3F6A9D2E08B47F5A
      </div>

    </div>
    """, unsafe_allow_html=True)

# ── Right — What happens next ─────────────────────────────────────────────────
with col_side:
    st.markdown("""
    <div class="card" style="margin-bottom:1rem;">
      <div class="card-title">Siguiente paso: CPA</div>
      <p style="color:#8BA3C0;font-size:0.85rem;line-height:1.65;margin-bottom:1rem;">
        El CEC se envía al proceso de autorización de pago. Se aplica la política
        de gobernanza correspondiente a la obra y al importe.
      </p>
      <div class="card-row">
        <span class="card-label">Política aplicada</span>
        <span class="card-value">SOX-OBRA</span>
      </div>
      <div class="card-row">
        <span class="card-label">Aprobadores requeridos</span>
        <span class="card-value">2 de 2</span>
      </div>
    </div>

    <div class="card" style="margin-bottom:1rem;">
      <div class="card-title" style="font-size:0.85rem;">Flujo de autorización</div>
      <div class="flow-arrow-box" style="flex-direction:column;align-items:flex-start;gap:0.35rem;padding:0.5rem 0;">
        <div style="display:flex;align-items:center;gap:0.5rem;">
          <div class="flow-step">CEC</div>
          <span class="flow-arrow">→</span>
          <div class="flow-step">Políticas</div>
        </div>
        <div style="display:flex;align-items:center;gap:0.5rem;margin-left:1.5rem;">
          <span class="flow-arrow">↓</span>
        </div>
        <div style="display:flex;align-items:center;gap:0.5rem;">
          <div class="flow-step">CPA</div>
          <span class="flow-arrow">→</span>
          <div class="flow-step">Pago</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # CPA preview
    st.markdown("""
    <div class="cer-card" style="border-color:rgba(34,211,165,0.4);">
      <div style="font-size:0.65rem;font-weight:700;text-transform:uppercase;letter-spacing:0.15em;color:#8BA3C0;margin-bottom:0.2rem;">
        CONTENEDOR DE PAGO AUTORIZADO
      </div>
      <div style="font-size:1.2rem;font-weight:800;color:#22D3A5;margin-bottom:0.75rem;">
        CPA-2026-000019
      </div>
      <div style="text-align:center;margin-bottom:1rem;">
        <span class="badge-green">&#10003; PAGO AUTORIZADO</span>
      </div>

      <div class="card-row">
        <span class="card-label">Importe</span>
        <span class="card-value" style="color:#F0F7FF;font-weight:800;">12.480,00 €</span>
      </div>
      <div class="card-row">
        <span class="card-label">Aprobadores</span>
        <span class="card-value" style="color:#22D3A5;font-weight:700;">2/2</span>
      </div>
      <div class="card-row" style="border-bottom:none;">
        <span class="card-label">Política</span>
        <span class="card-value">SOX-OBRA</span>
      </div>

      <div class="hash-block" style="font-size:0.7rem;margin-top:0.75rem;">
        <span class="hash-label">HASH CPA · SHA-256</span>
        D912A77BE4F1C385...<br>
        ...6D1F5C2B9E04A7F1
      </div>
    </div>
    """, unsafe_allow_html=True)
