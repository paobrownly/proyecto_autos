import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración de la página para que use todo el ancho
st.set_page_config(page_title="Análisis de Vehículos", layout="wide")

# Agregar título de la app
st.header("Análisis de anuncios de vehículos")

# Cargar datos
data = pd.read_csv("vehicles_us.csv")

# Mostrar Tabla de datos
st.subheader("Vista previa de los datos")
st.write("A continuación, se muestran las primeras filas del conjunto de datos:")
# Mostramos solo las primeras 200 filas para no ralentizar la app
st.dataframe(data.head(200), use_container_width=True)

# Agregar línea divisoria
st.divider()

# Generar gráficos
show_hist = st.checkbox("Mostrar histograma del odómetro")

if show_hist:
    st.write("### Histograma del kilometraje")
    fig = go.Figure(data=[go.Histogram(
        x=data["odometer"],
        marker_color="#52CDFF",
        opacity=0.75
    )])
    fig.update_layout(
        title="Distribución del Odómetro",
        xaxis_title="Kilometraje (millas)",
        yaxis_title="Frecuencia",
        template="plotly_white"  # Agregar fondo blanco para mayor limpieza
    )
    st.plotly_chart(fig, use_container_width=True)

show_scatter = st.checkbox("Mostrar gráfico de dispersión")

if show_scatter:
    st.write("### Relación entre precio y kilometraje")
    fig2 = go.Figure(
        data=[go.Scatter(
            x=data["odometer"],
            y=data["price"],
            mode="markers",
            marker=dict(
                size=7,
                color='#EF553B',
                opacity=0.5,    # Transparencia para ver densidad de puntos
                # Agregar borde blanco fino
                line=dict(width=0.5, color="white")
            )
        )]
    )
    fig2.update_layout(
        title="Precio vs Odómetro",
        xaxis_title="Odómetro",
        yaxis_title="Precio (USD)",
        template="plotly_white"
    )
    st.plotly_chart(fig2, use_container_width=True)
