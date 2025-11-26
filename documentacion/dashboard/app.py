"""
Dashboard de Predicción de Churn de Clientes Telco
Página principal - Inicio y Resumen
"""

import streamlit as st
import sys
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import os

# Agregar el directorio config al path
sys.path.append(os.path.join(os.path.dirname(__file__)))
from config.colors import CUSTOM_CSS

# Configuración de página
st.set_page_config(
    page_title="Dashboard de Predicción de Churn",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aplicar CSS personalizado
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Cargar metadata
METADATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'metadata.json')

try:
    with open(METADATA_PATH, 'r') as f:
        metadata = json.load(f)
except Exception as e:
    st.error(f"Error al cargar metadata del modelo: {e}")
    metadata = {}

# Hero Section
st.markdown("""
<div class="hero">
    <h1>📊 Dashboard de Predicción de Churn</h1>
    <p>Sistema inteligente para predecir y prevenir el abandono de clientes en telecomunicaciones</p>
    <p style="font-size: 1rem; margin-top: 1rem;">
        ✨ Modelo de Machine Learning con <strong>87% de precisión (ROC-AUC)</strong>
    </p>
</div>
""", unsafe_allow_html=True)

# Sección "Cómo funciona"
st.markdown("## 🚀 Cómo Funciona")
st.markdown("Sigue estos 3 simples pasos para predecir el riesgo de churn de tus clientes:")

col_step1, col_step2, col_step3 = st.columns(3)

with col_step1:
    st.markdown("""
    <div class="feature-box">
        <h3 style="text-align: center;">1️⃣ Ingresa Datos</h3>
        <p style="text-align: center;">
            Ve a la página <strong>Análisis de Riesgo</strong> y completa el formulario
            con la información del cliente.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_step2:
    st.markdown("""
    <div class="feature-box">
        <h3 style="text-align: center;">2️⃣ Obtén Predicción</h3>
        <p style="text-align: center;">
            El modelo de Machine Learning analiza los datos y calcula la
            probabilidad de churn en segundos.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_step3:
    st.markdown("""
    <div class="feature-box">
        <h3 style="text-align: center;">3️⃣ Toma Acción</h3>
        <p style="text-align: center;">
            Recibe recomendaciones personalizadas para retener al cliente
            según su nivel de riesgo.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Barra lateral simplificada
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/phone-disconnected.png", width=80)
    st.title("📍 Navegación")
    st.markdown("""
    **Páginas disponibles:**

    - 🏠 **Inicio** (estás aquí)
    - 📊 **Resumen** - Análisis exploratorio
    - 🎯 **Análisis de Riesgo** - Predicciones
    - 📈 **Métricas del Modelo** - Rendimiento
    - 💰 **Simulador ROI** - Retorno de inversión
    - 🔍 **Monitoreo** - Seguimiento
    """)

    st.markdown("---")
    st.markdown("### 📊 Información del Modelo")
    if metadata:
        st.metric("Tipo", metadata.get('model_type', 'N/A'))
        st.metric("ROC-AUC", f"{metadata.get('metrics', {}).get('roc_auc', 0):.2f}")
        st.metric("Features", metadata.get('n_features', 'N/A'))

    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; font-size: 0.8rem; color: #666;">
        <p>💡 <strong>Tip:</strong> Comienza por la página de <strong>Análisis de Riesgo</strong>
        para hacer tu primera predicción.</p>
    </div>
    """, unsafe_allow_html=True)

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

    # Diccionario de traducción de características
    feature_translations = {
        'gender': 'Género (gender)',
        'SeniorCitizen': 'Adulto Mayor (SeniorCitizen)',
        'Partner': 'Tiene Pareja (Partner)',
        'Dependents': 'Tiene Dependientes (Dependents)',
        'tenure': 'Antigüedad en Meses (tenure)',
        'PhoneService': 'Servicio Telefónico (PhoneService)',
        'MultipleLines': 'Múltiples Líneas (MultipleLines)',
        'InternetService': 'Servicio de Internet (InternetService)',
        'OnlineSecurity': 'Seguridad Online (OnlineSecurity)',
        'OnlineBackup': 'Respaldo Online (OnlineBackup)',
        'DeviceProtection': 'Protección de Dispositivo (DeviceProtection)',
        'TechSupport': 'Soporte Técnico (TechSupport)',
        'StreamingTV': 'Streaming TV (StreamingTV)',
        'StreamingMovies': 'Streaming Películas (StreamingMovies)',
        'Contract': 'Tipo de Contrato (Contract)',
        'PaperlessBilling': 'Facturación sin Papel (PaperlessBilling)',
        'PaymentMethod': 'Método de Pago (PaymentMethod)',
        'MonthlyCharges': 'Cargos Mensuales (MonthlyCharges)',
        'TotalCharges': 'Cargos Totales (TotalCharges)',
        'ChargeRatio': 'Ratio de Cargos (ChargeRatio)',
        'AvgMonthlyCharges': 'Promedio Cargos Mensuales (AvgMonthlyCharges)',
        'TenureGroup': 'Grupo de Antigüedad (TenureGroup)',
        'TotalServices': 'Total de Servicios (TotalServices)',
        'SeniorWithDependents': 'Adulto Mayor con Dependientes (SeniorWithDependents)',
        'HighValueContract': 'Contrato de Alto Valor (HighValueContract)'
    }

    # Crear columnas para características
    n_cols = 3
    cols = st.columns(n_cols)

    for i, feature in enumerate(features):
        with cols[i % n_cols]:
            # Usar traducción si existe, sino mostrar el nombre original
            translated_name = feature_translations.get(feature, feature)
            st.markdown(f"✓ {translated_name}")

st.markdown("---")

# Pie de página
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <p>Dashboard de Predicción de Churn de Clientes Telco v1.0.0</p>
    <p>Construido con Streamlit | Modelo: Random Forest Classifier</p>
</div>
""", unsafe_allow_html=True)

