import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.data_loader import get_inflacion_data

st.set_page_config(page_title="Inflación - Perú", page_icon="💰", layout="wide")

st.title("💰 Inflación en el Perú")
st.markdown("Fuente: **Instituto Nacional de Estadística e Informática (INEI)**")
st.markdown("---")

df = get_inflacion_data()

# Métricas
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Inflación 2023", "3.2%", "-5.3% vs 2022")
with col2:
    st.metric("Pico máximo", "2022", "8.5%")
with col3:
    st.metric("Meta del BCRP", "1% - 3%", "Rango objetivo")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Inflación anual (%)")
    fig1 = px.bar(
        df, x="año", y="inflacion",
        labels={"año": "Año", "inflacion": "Inflación (%)"},
        color="inflacion",
        color_continuous_scale=["green", "yellow", "red"],
        text="inflacion"
    )
    fig1.update_traces(texttemplate="%{text}%", textposition="outside")
    fig1.add_hline(y=3, line_dash="dash", line_color="red",
                   annotation_text="Límite superior BCRP (3%)")
    fig1.add_hline(y=1, line_dash="dash", line_color="green",
                   annotation_text="Límite inferior BCRP (1%)")
    fig1.update_layout(height=400, coloraxis_showscale=False)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Tendencia de inflación")
    fig2 = px.area(
        df, x="año", y="inflacion",
        labels={"año": "Año", "inflacion": "Inflación (%)"},
        markers=True
    )
    fig2.update_traces(line_color="#e63946", fillcolor="rgba(230,57,70,0.2)")
    fig2.update_layout(height=400)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.subheader("Datos completos")
st.dataframe(
    df.rename(columns={"año": "Año", "inflacion": "Inflación (%)"}),
    use_container_width=True,
    hide_index=True
)