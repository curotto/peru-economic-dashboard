import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.data_loader import get_empleo_data

st.set_page_config(page_title="Empleo - Perú", page_icon="💼", layout="wide")

st.title("💼 Empleo en el Perú")
st.markdown("Fuente: **Instituto Nacional de Estadística e Informática (INEI)**")
st.markdown("---")

df = get_empleo_data()

# Métricas
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Desempleo 2023", "4.2%", "+0.6% vs 2022")
with col2:
    st.metric("Pico de desempleo", "2020", "7.8%")
with col3:
    st.metric("Informalidad 2023", "73.6%", "+1.3% vs 2022")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Tasa de desempleo (%)")
    fig1 = px.line(
        df, x="año", y="desempleo",
        markers=True,
        labels={"año": "Año", "desempleo": "Desempleo (%)"}
    )
    fig1.update_traces(line_color="#e63946", line_width=3)
    fig1.update_layout(height=400)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Tasa de informalidad (%)")
    fig2 = px.bar(
        df, x="año", y="informalidad",
        labels={"año": "Año", "informalidad": "Informalidad (%)"},
        color="informalidad",
        color_continuous_scale=["yellow", "orange", "red"],
        text="informalidad"
    )
    fig2.update_traces(texttemplate="%{text}%", textposition="outside")
    fig2.update_layout(height=400, coloraxis_showscale=False)
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

st.subheader("Comparación desempleo vs informalidad")
fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=df["año"], y=df["desempleo"],
    name="Desempleo (%)",
    line=dict(color="#e63946", width=3),
    mode="lines+markers"
))
fig3.add_trace(go.Scatter(
    x=df["año"], y=df["informalidad"],
    name="Informalidad (%)",
    line=dict(color="#457b9d", width=3),
    mode="lines+markers",
    yaxis="y2"
))
fig3.update_layout(
    height=400,
    yaxis=dict(title="Desempleo (%)"),
    yaxis2=dict(title="Informalidad (%)", overlaying="y", side="right"),
    legend=dict(x=0.01, y=0.99)
)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.subheader("Datos completos")
st.dataframe(
    df.rename(columns={
        "año": "Año",
        "desempleo": "Desempleo (%)",
        "informalidad": "Informalidad (%)"
    }),
    use_container_width=True,
    hide_index=True
)