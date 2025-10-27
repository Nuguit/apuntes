from click import style
import streamlit as st

st.set_page_config(page_title="Apuntes", page_icon="💻", layout="wide")
st.markdown("""
<style>

html, body, .stApp, .css-1lcbmhc, .block-container, .main, .stApp > main {
    background-color: #890B2E !important;
}


.stApp, .stApp * {
    color: white !important;
}


.stApp h1, .stApp h2, .stApp h3 {
    color: white !important;
    text-align: center !important;
}


.seccion {
    padding-top: 60px;
    padding-bottom: 60px;
    border-bottom: 1px solid rgba(255,255,255,0.18) !important;
}


.stApp a, .stApp a:visited {
    color: #56DB66 !important;
    text-decoration: none !important;
    font-weight: bold !important;
}
.stApp a:hover {
    color: #56DBB2 !important;
}


.stMarkdown, .css-1kyxreq, .css-1e5imcs {
    color: white !important;
    text-align: center;
}


 .css-18e3th9 { visibility: hidden !important; }  
</style>
""", unsafe_allow_html=True)


st.title("💻 Apuntes Dawtásticos")
st.subheader("DAW-Segundo Curso")

# --- SECCIÓN 1: CLIENTE SERVIDOR ---
st.markdown('<div class="seccion" id="cliente-servidor"></div>', unsafe_allow_html=True)
st.header("💾 Cliente Servidor")
st.write("""
**Recursos recomendados:**
         
[📘 Formularios](https://notebooklm.google.com/notebook/2bc85910-0f48-48ed-810c-5f0f0815fe51)

""")

# --- SECCIÓN 2: INTERFACES WEB ---
st.markdown('<div class="seccion" id="interfaces-web"></div>', unsafe_allow_html=True)
st.header("🎨 Interfaces Web")
st.write("""

**Recursos recomendados:**

[🎨 CSS](https://notebooklm.google.com/notebook/32b67cc1-a634-4df9-bde7-2499231aa425)

""")

# --- FOOTER ---
st.markdown("---")
st.caption("© 2025 - Página creada con ❤️ usando Streamlit")
