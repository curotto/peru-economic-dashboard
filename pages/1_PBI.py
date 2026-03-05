import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.data_loader import get_pbi_data

st.set_page_config(page_title="PBI - Perú", page_icon="📈", layout="wide")

st.title("📈 Producto Bruto Interno del Perú")
st.markdown("Fuente: **Banco Central de Reserva del Perú (BCRP)**")
st.markdown("---")

df = get_pbi_data()

# Métricas
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("PBI 2023", "S/. 563,500 M", "-0.6%")
with col2:
    st.metric("Mejor año", "2021", "+13.3%")
with col3:
    st.metric("Peor año", "2020", "-11.0%")

st.markdown("---")

# Gráfico de variación
col1, col2 = st.columns(2)

with col1:
    st.subheader("Variación anual del PBI (%)")
    colors = ["red" if x < 0 else "green" for x in df["pbi_variacion"]]
    fig1 = go.Figure(go.Bar(
        x=df["año"],
        y=df["pbi_variacion"],
        marker_color=colors,
        text=df["pbi_variacion"].apply(lambda x: f"{x}%"),
        textposition="outside"
    ))
    fig1.update_layout(
        xaxis_title="Año",
        yaxis_title="Variación (%)",
        showlegend=False,
        height=400
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("PBI en millones de soles")
    fig2 = px.line(
        df, x="año", y="pbi_millones_soles",
        markers=True,
        labels={"año": "Año", "pbi_millones_soles": "Millones de Soles"}
    )
    fig2.update_traces(line_color="#e63946", line_width=3)
    fig2.update_layout(height=400)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.subheader("Datos completos")
st.dataframe(
    df.rename(columns={
        "año": "Año",
        "pbi_variacion": "Variación (%)",
        "pbi_millones_soles": "PBI (Millones S/.)"
    }),
    use_container_width=True,
    hide_index=True
)