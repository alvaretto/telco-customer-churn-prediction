"""
Dashboard de Predicción de Churn de Clientes Telco
Página principal - Inicio y Resumen
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import os

# Configuración de página
st.set_page_config(
    page_title="Dashboard de Predicción de Churn",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar metadata
METADATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'metadata.json')

try:
    with open(METADATA_PATH, 'r') as f:
        metadata = json.load(f)
except Exception as e:
    st.error(f"Error al cargar metadata del modelo: {e}")
    metadata = {}

# Título y descripción
st.title("📊 Dashboard de Predicción de Churn de Clientes Telco")
st.markdown("---")

# Barra lateral
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/phone-disconnected.png", width=80)
    st.title("Navegación")
    st.markdown("""
    Usa las páginas en la barra lateral para navegar:

    - **📊 Resumen**: Resumen del proyecto
    - **🎯 Análisis de Riesgo**: Predecir riesgo de churn
    - **📈 Métricas del Modelo**: Rendimiento del modelo
    - **💰 Simulador ROI**: Calcular ROI
    - **🔍 Monitoreo del Modelo**: Seguimiento del rendimiento
    """)

    st.markdown("---")
    st.markdown("### Información del Modelo")
    if metadata:
        st.metric("Tipo de Modelo", metadata.get('model_type', 'N/A'))
        st.metric("ROC-AUC", f"{metadata.get('metrics', {}).get('roc_auc', 0):.2f}")
        st.metric("Características", metadata.get('n_features', 'N/A'))

# Contenido principal
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Puntuación ROC-AUC",
        value=f"{metadata.get('metrics', {}).get('roc_auc', 0):.2f}",
        delta="0.87"
    )

with col2:
    st.metric(
        label="Recall (Sensibilidad)",
        value=f"{metadata.get('metrics', {}).get('recall', 0):.2f}",
        delta="0.83"
    )

with col3:
    st.metric(
        label="Precisión",
        value=f"{metadata.get('metrics', {}).get('precision', 0):.2f}",
        delta="0.72"
    )

with col4:
    st.metric(
        label="F1-Score",
        value=f"{metadata.get('metrics', {}).get('f1_score', 0):.2f}",
        delta="0.77"
    )

st.markdown("---")

# Descripción del proyecto
st.header("🎯 Acerca de Este Proyecto")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### Sistema de Predicción de Churn de Clientes

    Este dashboard proporciona una interfaz interactiva para predecir y analizar el churn de clientes
    en la industria de telecomunicaciones.

    **Características Principales:**
    - 🎯 **Análisis de Riesgo**: Predecir probabilidad de churn para clientes individuales
    - 📈 **Métricas del Modelo**: Métricas de rendimiento detalladas y visualizaciones
    - 💰 **Simulador ROI**: Calcular retorno de inversión para estrategias de retención
    - 🔍 **Monitoreo**: Seguimiento del rendimiento del modelo a lo largo del tiempo

    **Detalles del Modelo:**
    - **Algoritmo**: Random Forest Classifier
    - **Fecha de Entrenamiento**: {training_date}
    - **Características**: {n_features} atributos de clientes
    - **Muestras de Entrenamiento**: {n_samples} clientes
    """.format(
        training_date=metadata.get('training_date', 'N/A')[:10],
        n_features=metadata.get('n_features', 'N/A'),
        n_samples=metadata.get('n_samples_train', 'N/A')
    ))

with col2:
    st.info("""
    **Inicio Rápido:**

    1. Navega a **Análisis de Riesgo** para predecir churn de un cliente
    2. Revisa **Métricas del Modelo** para entender el rendimiento
    3. Usa **Simulador ROI** para calcular ROI de estrategias de retención
    4. Monitorea la salud del modelo en **Monitoreo del Modelo**
    """)

st.markdown("---")

# Resumen de características
st.header("📋 Características del Modelo")

if metadata.get('features'):
    features = metadata['features']

    # Crear columnas para características
    n_cols = 3
    cols = st.columns(n_cols)

    for i, feature in enumerate(features):
        with cols[i % n_cols]:
            st.markdown(f"✓ {feature}")

st.markdown("---")

# Pie de página
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <p>Dashboard de Predicción de Churn de Clientes Telco v1.0.0</p>
    <p>Construido con Streamlit | Modelo: Random Forest Classifier</p>
</div>
""", unsafe_allow_html=True)

