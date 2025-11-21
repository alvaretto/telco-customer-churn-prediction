"""
Página de Monitoreo del Modelo - Seguimiento del rendimiento del modelo a lo largo del tiempo
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(page_title="Monitoreo del Modelo", page_icon="🔍", layout="wide")

st.title("🔍 Monitoreo del Rendimiento del Modelo")
st.markdown("Seguimiento del rendimiento del modelo y detección de problemas potenciales")
st.markdown("---")

# Generar datos de monitoreo de muestra
np.random.seed(42)
dates = pd.date_range(end=datetime.now(), periods=30, freq='D')

monitoring_data = pd.DataFrame({
    'Date': dates,
    'Accuracy': np.random.normal(0.82, 0.02, 30),
    'Precision': np.random.normal(0.72, 0.03, 30),
    'Recall': np.random.normal(0.83, 0.02, 30),
    'F1_Score': np.random.normal(0.77, 0.02, 30),
    'Predictions': np.random.randint(100, 300, 30)
})

# Métricas actuales
current_metrics = monitoring_data.iloc[-1]

# Indicadores de estado
st.subheader("🎯 Estado Actual")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Exactitud",
        f"{current_metrics['Accuracy']:.3f}",
        delta=f"{(current_metrics['Accuracy'] - monitoring_data['Accuracy'].mean()):.3f}"
    )

with col2:
    st.metric(
        "Precisión",
        f"{current_metrics['Precision']:.3f}",
        delta=f"{(current_metrics['Precision'] - monitoring_data['Precision'].mean()):.3f}"
    )

with col3:
    st.metric(
        "Recall (Sensibilidad)",
        f"{current_metrics['Recall']:.3f}",
        delta=f"{(current_metrics['Recall'] - monitoring_data['Recall'].mean()):.3f}"
    )

with col4:
    st.metric(
        "F1-Score",
        f"{current_metrics['F1_Score']:.3f}",
        delta=f"{(current_metrics['F1_Score'] - monitoring_data['F1_Score'].mean()):.3f}"
    )

st.markdown("---")

# Rendimiento a lo largo del tiempo
st.subheader("📈 Tendencias de Rendimiento")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=monitoring_data['Date'],
    y=monitoring_data['Accuracy'],
    mode='lines+markers',
    name='Exactitud',
    line=dict(color='blue')
))

fig.add_trace(go.Scatter(
    x=monitoring_data['Date'],
    y=monitoring_data['Precision'],
    mode='lines+markers',
    name='Precisión',
    line=dict(color='green')
))

fig.add_trace(go.Scatter(
    x=monitoring_data['Date'],
    y=monitoring_data['Recall'],
    mode='lines+markers',
    name='Recall',
    line=dict(color='orange')
))

fig.add_trace(go.Scatter(
    x=monitoring_data['Date'],
    y=monitoring_data['F1_Score'],
    mode='lines+markers',
    name='F1-Score',
    line=dict(color='red')
))

fig.update_layout(
    title='Métricas del Modelo a lo Largo del Tiempo (Últimos 30 Días)',
    xaxis_title='Fecha',
    yaxis_title='Puntuación',
    hovermode='x unified',
    yaxis=dict(range=[0.6, 0.9])
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Volumen de predicciones
st.subheader("📊 Volumen de Predicciones")

fig = px.bar(
    monitoring_data,
    x='Date',
    y='Predictions',
    title='Predicciones Diarias',
    color='Predictions',
    color_continuous_scale='Blues'
)

fig.update_layout(
    xaxis_title='Fecha',
    yaxis_title='Número de Predicciones',
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Alertas y advertencias
st.subheader("⚠️ Alertas y Advertencias")

# Verificar degradación del rendimiento
accuracy_drop = current_metrics['Accuracy'] < monitoring_data['Accuracy'].mean() - 0.05
recall_drop = current_metrics['Recall'] < monitoring_data['Recall'].mean() - 0.05

if accuracy_drop or recall_drop:
    st.warning("""
    **Degradación del Rendimiento Detectada**

    El rendimiento del modelo ha caído por debajo de umbrales aceptables. Acciones recomendadas:
    - Revisar predicciones recientes en busca de patrones
    - Verificar desviación de datos (data drift)
    - Considerar reentrenamiento del modelo
    """)
else:
    st.success("""
    **Rendimiento del Modelo: Saludable**

    Todas las métricas están dentro de rangos aceptables. No se requiere acción inmediata.
    """)

st.markdown("---")

# Detección de desviación de datos (simulado)
st.subheader("🔄 Detección de Desviación de Datos")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Comparación de Distribución de Características")

    # Desviación de características simulada
    feature_drift = pd.DataFrame({
        'Característica': ['tenure', 'MonthlyCharges', 'TotalCharges', 'Contract', 'InternetService'],
        'Puntuación_Drift': [0.02, 0.15, 0.08, 0.25, 0.18],
        'Estado': ['✅ Estable', '⚠️ Advertencia', '✅ Estable', '🔴 Alerta', '⚠️ Advertencia']
    })

    st.dataframe(feature_drift, use_container_width=True)

with col2:
    fig = px.bar(
        feature_drift,
        x='Característica',
        y='Puntuación_Drift',
        title='Puntuaciones de Desviación de Características',
        color='Puntuación_Drift',
        color_continuous_scale='Reds'
    )

    fig.add_hline(y=0.1, line_dash="dash", line_color="orange",
                  annotation_text="Umbral de Advertencia")
    fig.add_hline(y=0.2, line_dash="dash", line_color="red",
                  annotation_text="Umbral de Alerta")

    fig.update_layout(yaxis_title="Puntuación de Drift", showlegend=False)

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Recomendaciones
st.subheader("💡 Recomendaciones de Monitoreo")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **Revisiones Diarias**
    - Monitorear volumen de predicciones
    - Verificar anomalías
    - Revisar logs de errores
    """)

with col2:
    st.info("""
    **Revisiones Semanales**
    - Analizar tendencias de rendimiento
    - Verificar puntuaciones de drift
    - Revisar falsos positivos/negativos
    """)

with col3:
    st.info("""
    **Acciones Mensuales**
    - Evaluación completa del modelo
    - Reentrenar si es necesario
    - Actualizar documentación
    """)

