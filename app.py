import streamlit as st

st.set_page_config(
    page_title="Dashboard Económico del Perú",
    page_icon="🇵🇪",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🇵🇪 Dashboard de Indicadores Económicos del Perú")
st.markdown("---")

st.markdown("""
### Bienvenido
Este dashboard muestra los principales indicadores económicos del Perú
usando datos públicos del **INEI** y el **BCRP**.

#### Secciones disponibles:
- 📈 **PBI** — Evolución del Producto Bruto Interno
- 💼 **Empleo** — Tasa de desempleo y empleo informal
- 💰 **Inflación** — Índice de Precios al Consumidor
""")

st.sidebar.title("🇵🇪 Indicadores Económicos")
st.sidebar.markdown("Selecciona una sección en el menú de arriba.")